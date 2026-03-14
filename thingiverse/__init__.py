"""A client library for accessing API documentation"""

from ._constants import BASE_URL_PRODUCTION, BASE_URL_STAGING
from .client import AuthenticatedClient, Client

__all__ = (
    "BASE_URL_PRODUCTION",
    "BASE_URL_STAGING",
    "AuthenticatedClient",
    "Client",
)
