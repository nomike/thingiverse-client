"""Unit tests for the comment API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.comment import (
    delete_comments_comment_id,
    get_comments,
    get_comments_comment_id,
    get_comments_comment_id_replies,
    patch_comments_comment_id,
    post_comments,
    post_comments_0_markdown,
    post_comments_comment_id_reply,
    post_comments_comment_id_restore,
    post_comments_comment_id_spam,
)


def test_delete_comments_comment_id_kwargs() -> None:
    kwargs = delete_comments_comment_id._get_kwargs(comment_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/comments/42/"


def test_get_comments_kwargs() -> None:
    kwargs = get_comments._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/comments/"


def test_get_comments_comment_id_kwargs() -> None:
    kwargs = get_comments_comment_id._get_kwargs(comment_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/comments/42/"


def test_get_comments_comment_id_replies_kwargs() -> None:
    kwargs = get_comments_comment_id_replies._get_kwargs(comment_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/comments/42/replies"


def test_patch_comments_comment_id_kwargs() -> None:
    kwargs = patch_comments_comment_id._get_kwargs(comment_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/comments/42/"


def test_post_comments_kwargs() -> None:
    kwargs = post_comments._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/comments/"


def test_post_comments_0_markdown_kwargs() -> None:
    kwargs = post_comments_0_markdown._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/comments/0/markdown"


def test_post_comments_comment_id_reply_kwargs() -> None:
    kwargs = post_comments_comment_id_reply._get_kwargs(comment_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/comments/42/reply"


def test_post_comments_comment_id_restore_kwargs() -> None:
    kwargs = post_comments_comment_id_restore._get_kwargs(comment_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/comments/42/restore"


def test_post_comments_comment_id_spam_kwargs() -> None:
    kwargs = post_comments_comment_id_spam._get_kwargs(comment_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/comments/42/spam"


def test_get_comments_comment_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_comments_comment_id.sync_detailed(comment_id=42, client=client)
    assert response.status_code == 200
    assert response.content is not None
