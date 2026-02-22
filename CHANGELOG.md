# Changelog

All notable changes to this project will be documented in this file. This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0](https://github.com/nomike/thingiverse-client/compare/v0.1.0...v0.2.0) (2026-02-22)


### Features

* regenerate full SDK from complete Thingiverse OpenAPI spec ([#4](https://github.com/nomike/thingiverse-client/issues/4)) ([6c0b1ff](https://github.com/nomike/thingiverse-client/commit/6c0b1ffb45e5b7aa16aa307db4d95bd9acabbc87))

## 0.1.0 (2026-02-22)


### Features

* initial Thingiverse Python SDK ([02da182](https://github.com/nomike/thingiverse-client/commit/02da1821bb4a45a01ad8962c32978ff35e9ca965))

## [0.1.0] - Initial release

- Python SDK generated from Thingiverse OpenAPI spec
- Production and staging base URL constants (`BASE_URL_PRODUCTION`, `BASE_URL_STAGING`)
- `Client` and `AuthenticatedClient` with configurable `base_url`
- Unit tests (mocked) and optional integration/destructive tests
- Pre-commit (commitlint, check-mkdocs, Ruff, markdown, yaml)
- CI: tests, pre-commit, release-please, docs to GitHub Pages
