"""Unit tests for the subscription API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.subscription import (
    delete_events_id,
    get_subscriptions_0_analytics,
    get_subscriptions_0_dashboard,
    get_subscriptions_0_dashboard_sources,
    get_subscriptions_tag_is_user_subscribed_to_tag,
    post_events_id_read_all,
    post_subscriptions_tag_set_subscribe_state,
)


def test_delete_events_id_kwargs() -> None:
    kwargs = delete_events_id._get_kwargs(id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/events/42"


def test_get_subscriptions_0_analytics_kwargs() -> None:
    kwargs = get_subscriptions_0_analytics._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/subscriptions/0/analytics"


def test_get_subscriptions_0_dashboard_kwargs() -> None:
    from thingiverse_client.models.get_subscriptions_0_dashboard_type import (
        GetSubscriptions0DashboardType,
    )

    kwargs = get_subscriptions_0_dashboard._get_kwargs(
        type_=GetSubscriptions0DashboardType.ALL_ACTIVITY
    )
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/subscriptions/0/dashboard"
    assert kwargs["params"]["type"] == "all-activity"


def test_get_subscriptions_0_dashboard_sources_kwargs() -> None:
    kwargs = get_subscriptions_0_dashboard_sources._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/subscriptions/0/dashboard-sources"


def test_get_subscriptions_tag_is_user_subscribed_to_tag_kwargs() -> None:
    kwargs = get_subscriptions_tag_is_user_subscribed_to_tag._get_kwargs(tag="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/subscriptions/test-value/is-user-subscribed-to-tag"


def test_post_events_id_read_all_kwargs() -> None:
    kwargs = post_events_id_read_all._get_kwargs(id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/events/42/read-all"


def test_post_subscriptions_tag_set_subscribe_state_kwargs() -> None:
    kwargs = post_subscriptions_tag_set_subscribe_state._get_kwargs(tag="test-value")
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/subscriptions/test-value/set-subscribe-state"


def test_get_subscriptions_tag_is_user_subscribed_to_tag_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_subscriptions_tag_is_user_subscribed_to_tag.sync_detailed(
        tag="test", client=client
    )
    assert response.status_code == 200
    assert response.content is not None
