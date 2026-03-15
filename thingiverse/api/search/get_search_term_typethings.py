from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_search_term_typethings_has_makes import GetSearchTermTypethingsHasMakes
from ...models.get_search_term_typethings_is_derivative import GetSearchTermTypethingsIsDerivative
from ...models.get_search_term_typethings_is_featured import GetSearchTermTypethingsIsFeatured
from ...models.get_search_term_typethings_is_fis_challenge_winnereatured import (
    GetSearchTermTypethingsIsFisChallengeWinnereatured,
)
from ...models.get_search_term_typethings_response_200 import GetSearchTermTypethingsResponse200
from ...models.get_search_term_typethings_response_401 import GetSearchTermTypethingsResponse401
from ...models.get_search_term_typethings_response_403 import GetSearchTermTypethingsResponse403
from ...models.get_search_term_typethings_response_404 import GetSearchTermTypethingsResponse404
from ...models.get_search_term_typethings_sort import GetSearchTermTypethingsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: str,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypethingsSort | Unset = UNSET,
    posted_before: str | Unset = UNSET,
    posted_after: str | Unset = UNSET,
    is_edu_approved: str | Unset = UNSET,
    subjects: str | Unset = UNSET,
    grades: str | Unset = UNSET,
    standards: str | Unset = UNSET,
    license_: str | Unset = UNSET,
    customizable: str | Unset = UNSET,
    show_customized: str | Unset = UNSET,
    has_makes: GetSearchTermTypethingsHasMakes | Unset = UNSET,
    is_featured: GetSearchTermTypethingsIsFeatured | Unset = UNSET,
    is_fis_challenge_winnereatured: GetSearchTermTypethingsIsFisChallengeWinnereatured
    | Unset = UNSET,
    liked_by: str | Unset = UNSET,
    made_by: str | Unset = UNSET,
    is_derivative: GetSearchTermTypethingsIsDerivative | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["posted_before"] = posted_before

    params["posted_after"] = posted_after

    params["is_edu_approved"] = is_edu_approved

    params["subjects"] = subjects

    params["grades"] = grades

    params["standards"] = standards

    params["license"] = license_

    params["customizable"] = customizable

    params["show_customized"] = show_customized

    json_has_makes: int | Unset = UNSET
    if not isinstance(has_makes, Unset):
        json_has_makes = has_makes.value

    params["has_makes"] = json_has_makes

    json_is_featured: int | Unset = UNSET
    if not isinstance(is_featured, Unset):
        json_is_featured = is_featured.value

    params["is_featured"] = json_is_featured

    json_is_fis_challenge_winnereatured: int | Unset = UNSET
    if not isinstance(is_fis_challenge_winnereatured, Unset):
        json_is_fis_challenge_winnereatured = is_fis_challenge_winnereatured.value

    params["is_fis_challenge_winnereatured"] = json_is_fis_challenge_winnereatured

    params["liked_by"] = liked_by

    params["made_by"] = made_by

    json_is_derivative: int | Unset = UNSET
    if not isinstance(is_derivative, Unset):
        json_is_derivative = is_derivative.value

    params["is_derivative"] = json_is_derivative

    params["category_id"] = category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search/{term}/?type=things".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSearchTermTypethingsResponse200
    | GetSearchTermTypethingsResponse401
    | GetSearchTermTypethingsResponse403
    | GetSearchTermTypethingsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetSearchTermTypethingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSearchTermTypethingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSearchTermTypethingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSearchTermTypethingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSearchTermTypethingsResponse200
    | GetSearchTermTypethingsResponse401
    | GetSearchTermTypethingsResponse403
    | GetSearchTermTypethingsResponse404
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
    sort: GetSearchTermTypethingsSort | Unset = UNSET,
    posted_before: str | Unset = UNSET,
    posted_after: str | Unset = UNSET,
    is_edu_approved: str | Unset = UNSET,
    subjects: str | Unset = UNSET,
    grades: str | Unset = UNSET,
    standards: str | Unset = UNSET,
    license_: str | Unset = UNSET,
    customizable: str | Unset = UNSET,
    show_customized: str | Unset = UNSET,
    has_makes: GetSearchTermTypethingsHasMakes | Unset = UNSET,
    is_featured: GetSearchTermTypethingsIsFeatured | Unset = UNSET,
    is_fis_challenge_winnereatured: GetSearchTermTypethingsIsFisChallengeWinnereatured
    | Unset = UNSET,
    liked_by: str | Unset = UNSET,
    made_by: str | Unset = UNSET,
    is_derivative: GetSearchTermTypethingsIsDerivative | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> Response[
    GetSearchTermTypethingsResponse200
    | GetSearchTermTypethingsResponse401
    | GetSearchTermTypethingsResponse403
    | GetSearchTermTypethingsResponse404
]:
    """Search for Things

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypethingsSort | Unset):
        posted_before (str | Unset):
        posted_after (str | Unset):
        is_edu_approved (str | Unset):
        subjects (str | Unset):
        grades (str | Unset):
        standards (str | Unset):
        license_ (str | Unset):
        customizable (str | Unset):
        show_customized (str | Unset):
        has_makes (GetSearchTermTypethingsHasMakes | Unset):
        is_featured (GetSearchTermTypethingsIsFeatured | Unset):
        is_fis_challenge_winnereatured (GetSearchTermTypethingsIsFisChallengeWinnereatured |
            Unset):
        liked_by (str | Unset):
        made_by (str | Unset):
        is_derivative (GetSearchTermTypethingsIsDerivative | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSearchTermTypethingsResponse200 | GetSearchTermTypethingsResponse401 | GetSearchTermTypethingsResponse403 | GetSearchTermTypethingsResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
        page=page,
        per_page=per_page,
        sort=sort,
        posted_before=posted_before,
        posted_after=posted_after,
        is_edu_approved=is_edu_approved,
        subjects=subjects,
        grades=grades,
        standards=standards,
        license_=license_,
        customizable=customizable,
        show_customized=show_customized,
        has_makes=has_makes,
        is_featured=is_featured,
        is_fis_challenge_winnereatured=is_fis_challenge_winnereatured,
        liked_by=liked_by,
        made_by=made_by,
        is_derivative=is_derivative,
        category_id=category_id,
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
    sort: GetSearchTermTypethingsSort | Unset = UNSET,
    posted_before: str | Unset = UNSET,
    posted_after: str | Unset = UNSET,
    is_edu_approved: str | Unset = UNSET,
    subjects: str | Unset = UNSET,
    grades: str | Unset = UNSET,
    standards: str | Unset = UNSET,
    license_: str | Unset = UNSET,
    customizable: str | Unset = UNSET,
    show_customized: str | Unset = UNSET,
    has_makes: GetSearchTermTypethingsHasMakes | Unset = UNSET,
    is_featured: GetSearchTermTypethingsIsFeatured | Unset = UNSET,
    is_fis_challenge_winnereatured: GetSearchTermTypethingsIsFisChallengeWinnereatured
    | Unset = UNSET,
    liked_by: str | Unset = UNSET,
    made_by: str | Unset = UNSET,
    is_derivative: GetSearchTermTypethingsIsDerivative | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> (
    GetSearchTermTypethingsResponse200
    | GetSearchTermTypethingsResponse401
    | GetSearchTermTypethingsResponse403
    | GetSearchTermTypethingsResponse404
    | None
):
    """Search for Things

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypethingsSort | Unset):
        posted_before (str | Unset):
        posted_after (str | Unset):
        is_edu_approved (str | Unset):
        subjects (str | Unset):
        grades (str | Unset):
        standards (str | Unset):
        license_ (str | Unset):
        customizable (str | Unset):
        show_customized (str | Unset):
        has_makes (GetSearchTermTypethingsHasMakes | Unset):
        is_featured (GetSearchTermTypethingsIsFeatured | Unset):
        is_fis_challenge_winnereatured (GetSearchTermTypethingsIsFisChallengeWinnereatured |
            Unset):
        liked_by (str | Unset):
        made_by (str | Unset):
        is_derivative (GetSearchTermTypethingsIsDerivative | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSearchTermTypethingsResponse200 | GetSearchTermTypethingsResponse401 | GetSearchTermTypethingsResponse403 | GetSearchTermTypethingsResponse404
    """

    return sync_detailed(
        term=term,
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        posted_before=posted_before,
        posted_after=posted_after,
        is_edu_approved=is_edu_approved,
        subjects=subjects,
        grades=grades,
        standards=standards,
        license_=license_,
        customizable=customizable,
        show_customized=show_customized,
        has_makes=has_makes,
        is_featured=is_featured,
        is_fis_challenge_winnereatured=is_fis_challenge_winnereatured,
        liked_by=liked_by,
        made_by=made_by,
        is_derivative=is_derivative,
        category_id=category_id,
    ).parsed


async def asyncio_detailed(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypethingsSort | Unset = UNSET,
    posted_before: str | Unset = UNSET,
    posted_after: str | Unset = UNSET,
    is_edu_approved: str | Unset = UNSET,
    subjects: str | Unset = UNSET,
    grades: str | Unset = UNSET,
    standards: str | Unset = UNSET,
    license_: str | Unset = UNSET,
    customizable: str | Unset = UNSET,
    show_customized: str | Unset = UNSET,
    has_makes: GetSearchTermTypethingsHasMakes | Unset = UNSET,
    is_featured: GetSearchTermTypethingsIsFeatured | Unset = UNSET,
    is_fis_challenge_winnereatured: GetSearchTermTypethingsIsFisChallengeWinnereatured
    | Unset = UNSET,
    liked_by: str | Unset = UNSET,
    made_by: str | Unset = UNSET,
    is_derivative: GetSearchTermTypethingsIsDerivative | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> Response[
    GetSearchTermTypethingsResponse200
    | GetSearchTermTypethingsResponse401
    | GetSearchTermTypethingsResponse403
    | GetSearchTermTypethingsResponse404
]:
    """Search for Things

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypethingsSort | Unset):
        posted_before (str | Unset):
        posted_after (str | Unset):
        is_edu_approved (str | Unset):
        subjects (str | Unset):
        grades (str | Unset):
        standards (str | Unset):
        license_ (str | Unset):
        customizable (str | Unset):
        show_customized (str | Unset):
        has_makes (GetSearchTermTypethingsHasMakes | Unset):
        is_featured (GetSearchTermTypethingsIsFeatured | Unset):
        is_fis_challenge_winnereatured (GetSearchTermTypethingsIsFisChallengeWinnereatured |
            Unset):
        liked_by (str | Unset):
        made_by (str | Unset):
        is_derivative (GetSearchTermTypethingsIsDerivative | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSearchTermTypethingsResponse200 | GetSearchTermTypethingsResponse401 | GetSearchTermTypethingsResponse403 | GetSearchTermTypethingsResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
        page=page,
        per_page=per_page,
        sort=sort,
        posted_before=posted_before,
        posted_after=posted_after,
        is_edu_approved=is_edu_approved,
        subjects=subjects,
        grades=grades,
        standards=standards,
        license_=license_,
        customizable=customizable,
        show_customized=show_customized,
        has_makes=has_makes,
        is_featured=is_featured,
        is_fis_challenge_winnereatured=is_fis_challenge_winnereatured,
        liked_by=liked_by,
        made_by=made_by,
        is_derivative=is_derivative,
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypethingsSort | Unset = UNSET,
    posted_before: str | Unset = UNSET,
    posted_after: str | Unset = UNSET,
    is_edu_approved: str | Unset = UNSET,
    subjects: str | Unset = UNSET,
    grades: str | Unset = UNSET,
    standards: str | Unset = UNSET,
    license_: str | Unset = UNSET,
    customizable: str | Unset = UNSET,
    show_customized: str | Unset = UNSET,
    has_makes: GetSearchTermTypethingsHasMakes | Unset = UNSET,
    is_featured: GetSearchTermTypethingsIsFeatured | Unset = UNSET,
    is_fis_challenge_winnereatured: GetSearchTermTypethingsIsFisChallengeWinnereatured
    | Unset = UNSET,
    liked_by: str | Unset = UNSET,
    made_by: str | Unset = UNSET,
    is_derivative: GetSearchTermTypethingsIsDerivative | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> (
    GetSearchTermTypethingsResponse200
    | GetSearchTermTypethingsResponse401
    | GetSearchTermTypethingsResponse403
    | GetSearchTermTypethingsResponse404
    | None
):
    """Search for Things

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypethingsSort | Unset):
        posted_before (str | Unset):
        posted_after (str | Unset):
        is_edu_approved (str | Unset):
        subjects (str | Unset):
        grades (str | Unset):
        standards (str | Unset):
        license_ (str | Unset):
        customizable (str | Unset):
        show_customized (str | Unset):
        has_makes (GetSearchTermTypethingsHasMakes | Unset):
        is_featured (GetSearchTermTypethingsIsFeatured | Unset):
        is_fis_challenge_winnereatured (GetSearchTermTypethingsIsFisChallengeWinnereatured |
            Unset):
        liked_by (str | Unset):
        made_by (str | Unset):
        is_derivative (GetSearchTermTypethingsIsDerivative | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSearchTermTypethingsResponse200 | GetSearchTermTypethingsResponse401 | GetSearchTermTypethingsResponse403 | GetSearchTermTypethingsResponse404
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            posted_before=posted_before,
            posted_after=posted_after,
            is_edu_approved=is_edu_approved,
            subjects=subjects,
            grades=grades,
            standards=standards,
            license_=license_,
            customizable=customizable,
            show_customized=show_customized,
            has_makes=has_makes,
            is_featured=is_featured,
            is_fis_challenge_winnereatured=is_fis_challenge_winnereatured,
            liked_by=liked_by,
            made_by=made_by,
            is_derivative=is_derivative,
            category_id=category_id,
        )
    ).parsed
