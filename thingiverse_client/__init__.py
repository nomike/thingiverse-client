"""Python SDK for the Thingiverse API."""

from ._config import BASE_URL_PRODUCTION, BASE_URL_STAGING
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "BASE_URL_PRODUCTION",
    "BASE_URL_STAGING",
)
