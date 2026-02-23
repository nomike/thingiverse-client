from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_things_thing_id_publish_response_200 import PostThingsThingIdPublishResponse200
from ...models.post_things_thing_id_publish_response_403 import PostThingsThingIdPublishResponse403
from ...models.post_things_thing_id_publish_response_404 import PostThingsThingIdPublishResponse404
from ...types import Response


def _get_kwargs(
    thing_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/things/{thing_id}/publish".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostThingsThingIdPublishResponse200
    | PostThingsThingIdPublishResponse403
    | PostThingsThingIdPublishResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostThingsThingIdPublishResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = PostThingsThingIdPublishResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostThingsThingIdPublishResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostThingsThingIdPublishResponse200
    | PostThingsThingIdPublishResponse403
    | PostThingsThingIdPublishResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    PostThingsThingIdPublishResponse200
    | PostThingsThingIdPublishResponse403
    | PostThingsThingIdPublishResponse404
]:
    r"""Publish a thing

     If the Thing cannot be published (for example, because the Thing's name or description is blank),
    returns an HTTP status of 400 Bad Request and a body containing a JSON object of the form:
    {\"errors\":[\"<%= reason %>\", ...]}

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingsThingIdPublishResponse200 | PostThingsThingIdPublishResponse403 | PostThingsThingIdPublishResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    PostThingsThingIdPublishResponse200
    | PostThingsThingIdPublishResponse403
    | PostThingsThingIdPublishResponse404
    | None
):
    r"""Publish a thing

     If the Thing cannot be published (for example, because the Thing's name or description is blank),
    returns an HTTP status of 400 Bad Request and a body containing a JSON object of the form:
    {\"errors\":[\"<%= reason %>\", ...]}

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingsThingIdPublishResponse200 | PostThingsThingIdPublishResponse403 | PostThingsThingIdPublishResponse404
    """

    return sync_detailed(
        thing_id=thing_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    PostThingsThingIdPublishResponse200
    | PostThingsThingIdPublishResponse403
    | PostThingsThingIdPublishResponse404
]:
    r"""Publish a thing

     If the Thing cannot be published (for example, because the Thing's name or description is blank),
    returns an HTTP status of 400 Bad Request and a body containing a JSON object of the form:
    {\"errors\":[\"<%= reason %>\", ...]}

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingsThingIdPublishResponse200 | PostThingsThingIdPublishResponse403 | PostThingsThingIdPublishResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    PostThingsThingIdPublishResponse200
    | PostThingsThingIdPublishResponse403
    | PostThingsThingIdPublishResponse404
    | None
):
    r"""Publish a thing

     If the Thing cannot be published (for example, because the Thing's name or description is blank),
    returns an HTTP status of 400 Bad Request and a body containing a JSON object of the form:
    {\"errors\":[\"<%= reason %>\", ...]}

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingsThingIdPublishResponse200 | PostThingsThingIdPublishResponse403 | PostThingsThingIdPublishResponse404
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
        )
    ).parsed
