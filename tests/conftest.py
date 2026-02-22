"""Pytest configuration and shared fixtures."""
import os

import pytest


def _get_base_url() -> str:
    """Base URL from env (staging or production)."""
    url = os.environ.get("THINGIVERSE_BASE_URL", "").strip()
    if url:
        return url.rstrip("/")
    if os.environ.get("THINGIVERSE_ENVIRONMENT") == "staging":
        return "https://api-staging.thingiverse.com"
    return "https://api.thingiverse.com"


def _get_token() -> str | None:
    return os.environ.get("THINGIVERSE_TOKEN") or None


@pytest.fixture
def base_url() -> str:
    return _get_base_url()


@pytest.fixture
def token() -> str | None:
    return _get_token()


@pytest.fixture
def skip_without_token():
    """Skip test if THINGIVERSE_TOKEN is not set (for integration tests)."""
    if not _get_token():
        pytest.skip("THINGIVERSE_TOKEN not set")
