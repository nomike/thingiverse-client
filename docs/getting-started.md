# Getting started

## Authentication

The Thingiverse API uses Bearer token authentication. Obtain a token from the [Thingiverse developer settings](https://www.thingiverse.com/apps) or from browser network requests to `api.thingiverse.com`.

```python
from thingiverse_client import AuthenticatedClient, BASE_URL_PRODUCTION

client = AuthenticatedClient(
    base_url=BASE_URL_PRODUCTION,
    token="your_token_here",
)
```

## Production vs staging

- **Production:** `https://api.thingiverse.com` — use `BASE_URL_PRODUCTION`
- **Staging:** `https://api-staging.thingiverse.com` — use `BASE_URL_STAGING`

## Making requests

Use the generated API modules under `thingiverse_client.api`:

```python
from thingiverse_client import AuthenticatedClient, BASE_URL_PRODUCTION
from thingiverse_client.api.default import get_things

client = AuthenticatedClient(base_url=BASE_URL_PRODUCTION, token="...")
response = get_things.sync_detailed(client=client)
```

## File uploads

File uploads (designs and images) follow a specific flow. See the [Thingiverse upload guide](https://www.thingiverse.com/developers/upload-guide) and the SDK's file upload documentation.
