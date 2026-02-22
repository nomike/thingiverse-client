"""Unit tests for the email API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.email import (
    post_email,
    post_email_thingiverse_enqueue_support,
    post_email_type_enqueue_dmca,
)


def test_post_email_kwargs() -> None:
    kwargs = post_email._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/email"


def test_post_email_thingiverse_enqueue_support_kwargs() -> None:
    kwargs = post_email_thingiverse_enqueue_support._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/email/thingiverse/enqueue-support"


def test_post_email_type_enqueue_dmca_kwargs() -> None:
    from thingiverse_client.models.post_email_type_enqueue_dmca_type import (
        PostEmailTypeEnqueueDmcaType,
    )

    kwargs = post_email_type_enqueue_dmca._get_kwargs(type_=PostEmailTypeEnqueueDmcaType.COPYRIGHT)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/email/copyright/enqueue-dmca"


def test_post_email_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = post_email.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.content is not None
