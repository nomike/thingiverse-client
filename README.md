# Thingiverse Python SDK

A Python SDK for the [Thingiverse API](https://www.thingiverse.com/developers/).

## Installation

```bash
pip install thingiverse-client
```

Or from source:

```bash
pip install .
# or for development
pip install -e ".[dev]"
```

## Quick start

```python
from thingiverse import AuthenticatedClient, BASE_URL_PRODUCTION
from thingiverse.api.thing import get_things_thing_id

client = AuthenticatedClient(
    base_url=BASE_URL_PRODUCTION,
    token="YOUR_ACCESS_TOKEN",
)

response = get_things_thing_id.sync_detailed(thing_id=123, client=client)
```

## Using the staging API

Use `BASE_URL_STAGING` to target the staging environment:

```python
from thingiverse import AuthenticatedClient, BASE_URL_STAGING

client = AuthenticatedClient(base_url=BASE_URL_STAGING, token="...")
```

## Authentication

The Thingiverse API uses Bearer token authentication. You can obtain a token from [Thingiverse app settings](https://www.thingiverse.com/apps) or from browser network requests to `api.thingiverse.com`.

## File uploads

File uploads (designs and images) use a specific flow. See the [Thingiverse upload guide](https://www.thingiverse.com/developers/upload-guide) for details. The SDK exposes the generated `uploadFile` and `FinalizeFiles` endpoints; you may use a thin helper for the full upload flow (see docs).

## Development setup

1. Clone the repository and create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -e ".[dev]"
   ```

2. Install pre-commit hooks (including commit message format):

   ```bash
   pre-commit install
   pre-commit install --hook-type commit-msg
   ```

3. Commit messages must follow [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `feat: add X`, `fix: Y`). The commit-msg hook enforces this.

## Running tests

Use the virtual environment’s Python so that dependencies (e.g. `httpx`) are found. Either activate the venv first (`source .venv/bin/activate` then `pytest`) or run:

```bash
.venv/bin/python -m pytest tests/unit tests/integration -v
```

- **Unit tests** (default, no API calls):

  ```bash
  pytest tests/unit -v
  ```

- **Integration tests** (read-only, real API). Set `THINGIVERSE_TOKEN`; optionally set `THINGIVERSE_BASE_URL` for staging:

  ```bash
  THINGIVERSE_TOKEN=... pytest tests/unit tests/integration -v
  ```

- **Destructive tests** (optional; modify data). Not run in CI. Use a dedicated test account and prefer staging:

  ```bash
  THINGIVERSE_BASE_URL=https://api-staging.thingiverse.com THINGIVERSE_TOKEN=... pytest -m destructive
  ```

## Updating the API spec

To refresh the SDK from the upstream Thingiverse OpenAPI spec:

1. Run the fetch script (downloads the full spec; the docs URL may be behind Cloudflare—see script docstring):

   ```bash
   python scripts/fetch_openapi_spec.py
   ```

2. Bundle, run the upstream-spec fix script, and regenerate the client (see [OpenAPI upstream notes](docs/openapi-upstream.md)):

   ```bash
   ./scripts/generate_client.sh
   ```

3. Commit changes and open a PR; merging can trigger a new release via release-please.

## Documentation

Documentation is built with [Zensical](https://zensical.org/) (reads `mkdocs.yml`) and published to GitHub Pages. Build locally:

```bash
pip install -e ".[dev]"
zensical serve
```

## Publishing to PyPI

Publishing is automated via the [Publish to PyPI](.github/workflows/publish-pypi.yml) workflow. When a GitHub release is published (e.g. by merging a release-please release PR), the workflow builds the package and uploads it to PyPI.

**One-time setup:**

1. Create a [PyPI](https://pypi.org) account and register the project name `thingiverse-client` if needed.
2. Configure [trusted publishing](https://docs.pypi.org/trusted-publishers/) for this repository:
   - PyPI: [Add a new trusted publisher](https://pypi.org/trusted-publishers/add/) for the project.
   - Set **Owner** and **Repository name** to this repo, **Workflow name** to `publish-pypi.yml`.
   - No secrets or API tokens are required; PyPI uses OIDC to verify the workflow.

After that, each new release will be published to PyPI automatically. Optionally, add a GitHub Actions environment (e.g. `pypi`) and set `environment: pypi` in the workflow for approval or protection rules.

## License

MIT.
