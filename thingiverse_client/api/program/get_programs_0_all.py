from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_programs_0_all_response_200 import GetPrograms0AllResponse200
from ...models.get_programs_0_all_response_401 import GetPrograms0AllResponse401
from ...models.get_programs_0_all_response_403 import GetPrograms0AllResponse403
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/programs/0/all",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403 | None:
    if response.status_code == 200:
        response_200 = GetPrograms0AllResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetPrograms0AllResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetPrograms0AllResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403]:
    """Get a list of programs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403 | None:
    """Get a list of programs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403]:
    """Get a list of programs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403 | None:
    """Get a list of programs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrograms0AllResponse200 | GetPrograms0AllResponse401 | GetPrograms0AllResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
