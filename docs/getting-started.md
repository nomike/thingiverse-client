# Getting started

## Authentication

The Thingiverse API uses Bearer token authentication. Obtain a token from the [Thingiverse developer settings](https://www.thingiverse.com/apps) or from browser network requests to `api.thingiverse.com`.

```python
from thingiverse import AuthenticatedClient, BASE_URL_PRODUCTION

client = AuthenticatedClient(
    base_url=BASE_URL_PRODUCTION,
    token="your_token_here",
)
```

## Production vs staging

- **Production:** `https://api.thingiverse.com` — use `BASE_URL_PRODUCTION`
- **Staging:** `https://api-staging.thingiverse.com` — use `BASE_URL_STAGING`

## Making requests

Use the generated API modules under `thingiverse.api`:

```python
from thingiverse import AuthenticatedClient, BASE_URL_PRODUCTION
from thingiverse.api.thing import get_things_thing_id

client = AuthenticatedClient(base_url=BASE_URL_PRODUCTION, token="...")
response = get_things_thing_id.sync_detailed(thing_id=123, client=client)
```

## File uploads

File uploads (designs and images) follow a specific flow. See the [Thingiverse upload guide](https://www.thingiverse.com/developers/upload-guide) and the SDK's file upload documentation.
