from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_search_term_typeusers_response_200 import GetSearchTermTypeusersResponse200
from ...models.get_search_term_typeusers_response_401 import GetSearchTermTypeusersResponse401
from ...models.get_search_term_typeusers_response_403 import GetSearchTermTypeusersResponse403
from ...models.get_search_term_typeusers_response_404 import GetSearchTermTypeusersResponse404
from ...models.get_search_term_typeusers_skill_level import GetSearchTermTypeusersSkillLevel
from ...models.get_search_term_typeusers_sort import GetSearchTermTypeusersSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: str,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypeusersSort | Unset = UNSET,
    users_thing_count: int | Unset = UNSET,
    users_user_types: int | Unset = UNSET,
    skill_level: GetSearchTermTypeusersSkillLevel | Unset = UNSET,
    programs: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["users_thing_count"] = users_thing_count

    params["users_user_types"] = users_user_types

    json_skill_level: str | Unset = UNSET
    if not isinstance(skill_level, Unset):
        json_skill_level = skill_level.value

    params["skill_level"] = json_skill_level

    params["programs"] = programs

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search/{term}/?type=users".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSearchTermTypeusersResponse200
    | GetSearchTermTypeusersResponse401
    | GetSearchTermTypeusersResponse403
    | GetSearchTermTypeusersResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetSearchTermTypeusersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSearchTermTypeusersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSearchTermTypeusersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSearchTermTypeusersResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSearchTermTypeusersResponse200
    | GetSearchTermTypeusersResponse401
    | GetSearchTermTypeusersResponse403
    | GetSearchTermTypeusersResponse404
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypeusersSort | Unset = UNSET,
    users_thing_count: int | Unset = UNSET,
    users_user_types: int | Unset = UNSET,
    skill_level: GetSearchTermTypeusersSkillLevel | Unset = UNSET,
    programs: int | Unset = UNSET,
) -> Response[
    GetSearchTermTypeusersResponse200
    | GetSearchTermTypeusersResponse401
    | GetSearchTermTypeusersResponse403
    | GetSearchTermTypeusersResponse404
]:
    """Search for Users

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypeusersSort | Unset):
        users_thing_count (int | Unset):
        users_user_types (int | Unset):  Example: 4.
        skill_level (GetSearchTermTypeusersSkillLevel | Unset):
        programs (int | Unset):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSearchTermTypeusersResponse200 | GetSearchTermTypeusersResponse401 | GetSearchTermTypeusersResponse403 | GetSearchTermTypeusersResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
        page=page,
        per_page=per_page,
        sort=sort,
        users_thing_count=users_thing_count,
        users_user_types=users_user_types,
        skill_level=skill_level,
        programs=programs,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypeusersSort | Unset = UNSET,
    users_thing_count: int | Unset = UNSET,
    users_user_types: int | Unset = UNSET,
    skill_level: GetSearchTermTypeusersSkillLevel | Unset = UNSET,
    programs: int | Unset = UNSET,
) -> (
    GetSearchTermTypeusersResponse200
    | GetSearchTermTypeusersResponse401
    | GetSearchTermTypeusersResponse403
    | GetSearchTermTypeusersResponse404
    | None
):
    """Search for Users

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypeusersSort | Unset):
        users_thing_count (int | Unset):
        users_user_types (int | Unset):  Example: 4.
        skill_level (GetSearchTermTypeusersSkillLevel | Unset):
        programs (int | Unset):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSearchTermTypeusersResponse200 | GetSearchTermTypeusersResponse401 | GetSearchTermTypeusersResponse403 | GetSearchTermTypeusersResponse404
    """

    return sync_detailed(
        term=term,
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        users_thing_count=users_thing_count,
        users_user_types=users_user_types,
        skill_level=skill_level,
        programs=programs,
    ).parsed


async def asyncio_detailed(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypeusersSort | Unset = UNSET,
    users_thing_count: int | Unset = UNSET,
    users_user_types: int | Unset = UNSET,
    skill_level: GetSearchTermTypeusersSkillLevel | Unset = UNSET,
    programs: int | Unset = UNSET,
) -> Response[
    GetSearchTermTypeusersResponse200
    | GetSearchTermTypeusersResponse401
    | GetSearchTermTypeusersResponse403
    | GetSearchTermTypeusersResponse404
]:
    """Search for Users

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypeusersSort | Unset):
        users_thing_count (int | Unset):
        users_user_types (int | Unset):  Example: 4.
        skill_level (GetSearchTermTypeusersSkillLevel | Unset):
        programs (int | Unset):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSearchTermTypeusersResponse200 | GetSearchTermTypeusersResponse401 | GetSearchTermTypeusersResponse403 | GetSearchTermTypeusersResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
        page=page,
        per_page=per_page,
        sort=sort,
        users_thing_count=users_thing_count,
        users_user_types=users_user_types,
        skill_level=skill_level,
        programs=programs,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypeusersSort | Unset = UNSET,
    users_thing_count: int | Unset = UNSET,
    users_user_types: int | Unset = UNSET,
    skill_level: GetSearchTermTypeusersSkillLevel | Unset = UNSET,
    programs: int | Unset = UNSET,
) -> (
    GetSearchTermTypeusersResponse200
    | GetSearchTermTypeusersResponse401
    | GetSearchTermTypeusersResponse403
    | GetSearchTermTypeusersResponse404
    | None
):
    """Search for Users

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypeusersSort | Unset):
        users_thing_count (int | Unset):
        users_user_types (int | Unset):  Example: 4.
        skill_level (GetSearchTermTypeusersSkillLevel | Unset):
        programs (int | Unset):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSearchTermTypeusersResponse200 | GetSearchTermTypeusersResponse401 | GetSearchTermTypeusersResponse403 | GetSearchTermTypeusersResponse404
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            users_thing_count=users_thing_count,
            users_user_types=users_user_types,
            skill_level=skill_level,
            programs=programs,
        )
    ).parsed
