# OpenAPI spec: upstream source and known issues

The files under `openapi/` (except `generator-config.yaml` and `.gitkeep`) are **downloaded from Thingiverse** via `scripts/fetch_openapi_spec.py`. We do not manually edit those downloaded files, because any changes would be overwritten the next time the spec is re-fetched.

## Upstream spec issues

The Thingiverse OpenAPI spec has compliance issues that strict OpenAPI 3.0 consumers (including openapi-python-client) do not accept:

- **Missing `description` on response objects** — In OpenAPI 3.0, every [Response Object](https://spec.openapis.org/oas/v3.0.0#response-object) must have a `description` field. Several endpoints define a `200` response with `content` but no `description`, which causes the generator to fail.

Other upstream issues (arrays without `items`, path parameters optional or not matching the path, etc.) are fixed automatically by the patch script (see below).

## Our approach: patch the bundled spec with a script

We keep the **downloaded source spec untouched**. After Redocly produces a single bundled file (`openapi/bundled.yaml`), we run **`scripts/patch_bundled_spec_full.py`**, which applies all fixes so the generator can build the SDK. The pipeline is:

1. **Fetch** — `scripts/fetch_openapi_spec.py` → pristine files from Thingiverse.
2. **Bundle** — Redocly → `openapi/bundled.yaml`.
3. **Patch** — `scripts/patch_bundled_spec_full.py` → fix bundled spec in place.
4. **Generate** — openapi-python-client → `thingiverse_client/`.

The script adds missing response `description`s, adds `items` to array schemas, sets path parameters to `required: true`, fixes path templating, and moves parameters that are in path but not in the path template to `query`. If the generator reports new issues after a fetch, extend the script and re-run.

## Updating the fix script

When the upstream spec changes and new generator errors appear, edit `scripts/patch_bundled_spec_full.py` to add or adjust fixes. Run `./scripts/generate_client.sh` to verify. The following steps are only needed if you want to recreate a diff-based patch (optional):

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

The **update script** (i.e. the flow used in normal development) is: fetch → bundle → run `patch_bundled_spec_full.py` → generate. See `scripts/generate_client.sh` and the “Updating the API spec” section in the README.

## Alternatives considered

- **Manually editing downloaded files** — Rejected: changes are lost on next fetch.
- **Forking the spec in our repo** — Rejected: we’d have to merge upstream changes by hand.
- **A single diff patch file** — Replaced by a script so we can fix many structural issues without a huge, fragile patch.
- **Reporting upstream** — Still recommended (e.g. open an issue or PR with Thingiverse) so the official spec becomes compliant; the patch can be simplified or removed once upstream is fixed.
