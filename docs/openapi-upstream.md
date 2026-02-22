# OpenAPI spec: upstream source and known issues

The files under `openapi/` (except `generator-config.yaml`, `bundled.patch`, and `.gitkeep`) are **downloaded from Thingiverse** via `scripts/fetch_openapi_spec.py`. We do not manually edit those downloaded files, because any changes would be overwritten the next time the spec is re-fetched.

## Upstream spec issues

The Thingiverse OpenAPI spec has compliance issues that strict OpenAPI 3.0 consumers (including openapi-python-client) do not accept:

- **Missing `description` on response objects** — In OpenAPI 3.0, every [Response Object](https://spec.openapis.org/oas/v3.0.0#response-object) must have a `description` field. Several endpoints define a `200` response with `content` but no `description`, which causes the generator to fail.

Other upstream issues that affect code generation include duplicate schema names (Redocly renames them), arrays without `items`, and schemas that the generator cannot process (so some endpoints are omitted from the generated client). The patch we apply addresses the missing response `description` requirement; further fixes can be added to the patch as needed.

## Our approach: apply a diff patch to the bundled spec

We keep the **downloaded source spec untouched**. After Redocly produces a single bundled file (`openapi/bundled.yaml`), we **apply a unified-diff patch** (`openapi/bundled.patch`) that encodes the minimal edits needed for the generator to accept the spec. The patch is version-controlled; the pipeline is:

1. **Fetch** — `scripts/fetch_openapi_spec.py` → pristine files from Thingiverse.
2. **Bundle** — Redocly → `openapi/bundled.yaml`.
3. **Apply patch** — `patch -p0 < openapi/bundled.patch` → fix bundled spec in place.
4. **Generate** — openapi-python-client → `thingiverse_client/`.

If the patch no longer applies (e.g. upstream changed the spec), the generate script fails and instructs you to update the patch (see below).

## How to create or update the patch (steps 1–8)

When you need to (re)create or update `openapi/bundled.patch` (e.g. after a fresh fetch, or because upstream fixed some things and you want to add more fixes):

1. **Fetch the API spec freshly from Thingiverse**

   ```bash
   python scripts/fetch_openapi_spec.py
   ```

2. **Bundle it** (merge into a single file)

   ```bash
   npx --yes @redocly/cli bundle openapi/openapi.yaml -o openapi/bundled.yaml
   ```

3. **Create a copy of that merged file**

   ```bash
   cp openapi/bundled.yaml openapi/bundled.orig.yaml
   ```

4. **Try to generate the SDK**

   ```bash
   openapi-python-client generate --path openapi/bundled.yaml --config openapi/generator-config.yaml --output-path thingiverse_client --overwrite
   ```

5. **Manually address all the issues that are reported**
   Edit `openapi/bundled.yaml` (e.g. add missing `description` under responses, fix schema issues). You can use `scripts/add_response_descriptions_in_place.py openapi/bundled.yaml` to insert missing response descriptions without reordering the file.

6. **Repeat from step 4** until the generator runs without errors (warnings about omitted endpoints/schemas are acceptable if you can’t fix them).

7. **Diff the copy from step 3 with the fixed version**

   ```bash
   diff -u openapi/bundled.orig.yaml openapi/bundled.yaml > openapi/bundled.patch
   ```

   Then edit the first two lines of `openapi/bundled.patch` so both paths are `openapi/bundled.yaml` (the patch must apply to the file that will be produced by the bundle step):
   - Change `--- openapi/bundled.orig.yaml ...` to `--- openapi/bundled.yaml`
   - Change `+++ openapi/bundled.yaml ...` to `+++ openapi/bundled.yaml`

8. **Commit the updated patch** (and remove `openapi/bundled.orig.yaml` from the repo if it was added; it’s only for creating the diff).

The **update script** (i.e. the flow used in normal development) is: fetch → bundle → apply `openapi/bundled.patch` → generate. See `scripts/generate_client.sh` and the “Updating the API spec” section in the README.

## Alternatives considered

- **Manually editing downloaded files** — Rejected: changes are lost on next fetch.
- **Forking the spec in our repo** — Rejected: we’d have to merge upstream changes by hand.
- **A custom Python script that fixes the bundled file** — Replaced by a diff patch so fixes are explicit, reviewable, and easy to update when upstream changes.
- **Reporting upstream** — Still recommended (e.g. open an issue or PR with Thingiverse) so the official spec becomes compliant; the patch can be simplified or removed once upstream is fixed.
