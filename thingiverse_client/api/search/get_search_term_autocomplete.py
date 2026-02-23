from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_search_term_autocomplete_response_401 import GetSearchTermAutocompleteResponse401
from ...models.get_search_term_autocomplete_response_403 import GetSearchTermAutocompleteResponse403
from ...models.get_search_term_autocomplete_response_404 import GetSearchTermAutocompleteResponse404
from ...types import Response


def _get_kwargs(
    term: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search/{term}/autocomplete".format(
            term=quote(str(term), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSearchTermAutocompleteResponse401
    | GetSearchTermAutocompleteResponse403
    | GetSearchTermAutocompleteResponse404
    | None
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = GetSearchTermAutocompleteResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSearchTermAutocompleteResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSearchTermAutocompleteResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSearchTermAutocompleteResponse401
    | GetSearchTermAutocompleteResponse403
    | GetSearchTermAutocompleteResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | GetSearchTermAutocompleteResponse401
    | GetSearchTermAutocompleteResponse403
    | GetSearchTermAutocompleteResponse404
]:
    """Search data by term for autocomplete

    Args:
        term (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchTermAutocompleteResponse401 | GetSearchTermAutocompleteResponse403 | GetSearchTermAutocompleteResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | GetSearchTermAutocompleteResponse401
    | GetSearchTermAutocompleteResponse403
    | GetSearchTermAutocompleteResponse404
    | None
):
    """Search data by term for autocomplete

    Args:
        term (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchTermAutocompleteResponse401 | GetSearchTermAutocompleteResponse403 | GetSearchTermAutocompleteResponse404
    """

    return sync_detailed(
        term=term,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | GetSearchTermAutocompleteResponse401
    | GetSearchTermAutocompleteResponse403
    | GetSearchTermAutocompleteResponse404
]:
    """Search data by term for autocomplete

    Args:
        term (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchTermAutocompleteResponse401 | GetSearchTermAutocompleteResponse403 | GetSearchTermAutocompleteResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | GetSearchTermAutocompleteResponse401
    | GetSearchTermAutocompleteResponse403
    | GetSearchTermAutocompleteResponse404
    | None
):
    """Search data by term for autocomplete

    Args:
        term (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchTermAutocompleteResponse401 | GetSearchTermAutocompleteResponse403 | GetSearchTermAutocompleteResponse404
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
        )
    ).parsed
