# Destructive tests

These tests create, update, or delete data on Thingiverse. They are **not** run in CI.

To run them (optional):

```bash
pytest -m destructive
```

Use a dedicated test account and token. Prefer running against staging:

```bash
THINGIVERSE_BASE_URL=https://api-staging.thingiverse.com THINGIVERSE_TOKEN=... pytest -m destructive
```
