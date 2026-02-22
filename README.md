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
from thingiverse_client import AuthenticatedClient, BASE_URL_PRODUCTION
from thingiverse_client.api.thing import get_things_thing_id

client = AuthenticatedClient(
    base_url=BASE_URL_PRODUCTION,
    token="YOUR_ACCESS_TOKEN",
)

response = get_things_thing_id.sync_detailed(thing_id=123, client=client)
```

## Using the staging API

Use `BASE_URL_STAGING` to target the staging environment:

```python
from thingiverse_client import AuthenticatedClient, BASE_URL_STAGING

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

When ready to publish:

1. Create a PyPI account and configure [trusted publishing](https://docs.pypi.org/trusted-publishers/) (e.g. OIDC with GitHub Actions) or use an API token.
2. Add a workflow that runs on release (e.g. when the release-please release is published) to run `python -m build` and `twine upload dist/*`.

## License

MIT.
