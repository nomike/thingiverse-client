# Changelog

All notable changes to this project will be documented in this file. This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - Initial release

- Python SDK generated from Thingiverse OpenAPI spec
- Production and staging base URL constants (`BASE_URL_PRODUCTION`, `BASE_URL_STAGING`)
- `Client` and `AuthenticatedClient` with configurable `base_url`
- Unit tests (mocked) and optional integration/destructive tests
- Pre-commit (commitlint, check-mkdocs, Ruff, markdown, yaml)
- CI: tests, pre-commit, release-please, docs to GitHub Pages
