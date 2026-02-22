# Thingiverse Python SDK

A Python SDK for the [Thingiverse API](https://www.thingiverse.com/developers/).

## Installation

```bash
pip install thingiverse-client
```

## Quick start

```python
from thingiverse_client import AuthenticatedClient, BASE_URL_PRODUCTION

client = AuthenticatedClient(
    base_url=BASE_URL_PRODUCTION,
    token="YOUR_ACCESS_TOKEN",
)
# Use client with the generated API modules
```

## Using the staging API

```python
from thingiverse_client import AuthenticatedClient, BASE_URL_STAGING

client = AuthenticatedClient(base_url=BASE_URL_STAGING, token="...")
```

See [Getting started](getting-started.md) for more details.
