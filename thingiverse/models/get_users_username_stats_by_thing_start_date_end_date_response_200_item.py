from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUsersUsernameStatsByThingStartDateEndDateResponse200Item")


@_attrs_define
class GetUsersUsernameStatsByThingStartDateEndDateResponse200Item:
    """
    Attributes:
        collects (int | Unset):
        comments (int | Unset):
        day (str | Unset):  Example: 2023-03-28.
        derivatives (int | Unset):
        downloads (int | Unset):
        likes (int | Unset):
        makes (int | Unset):
        user_id (int | Unset):
        views (int | Unset):
        watches (int | Unset):
    """

    collects: int | Unset = UNSET
    comments: int | Unset = UNSET
    day: str | Unset = UNSET
    derivatives: int | Unset = UNSET
    downloads: int | Unset = UNSET
    likes: int | Unset = UNSET
    makes: int | Unset = UNSET
    user_id: int | Unset = UNSET
    views: int | Unset = UNSET
    watches: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collects = self.collects

        comments = self.comments

        day = self.day

        derivatives = self.derivatives

        downloads = self.downloads

        likes = self.likes

        makes = self.makes

        user_id = self.user_id

        views = self.views

        watches = self.watches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collects is not UNSET:
            field_dict["collects"] = collects
        if comments is not UNSET:
            field_dict["comments"] = comments
        if day is not UNSET:
            field_dict["day"] = day
        if derivatives is not UNSET:
            field_dict["derivatives"] = derivatives
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if likes is not UNSET:
            field_dict["likes"] = likes
        if makes is not UNSET:
            field_dict["makes"] = makes
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if views is not UNSET:
            field_dict["views"] = views
        if watches is not UNSET:
            field_dict["watches"] = watches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collects = d.pop("collects", UNSET)

        comments = d.pop("comments", UNSET)

        day = d.pop("day", UNSET)

        derivatives = d.pop("derivatives", UNSET)

        downloads = d.pop("downloads", UNSET)

        likes = d.pop("likes", UNSET)

        makes = d.pop("makes", UNSET)

        user_id = d.pop("user_id", UNSET)

        views = d.pop("views", UNSET)

        watches = d.pop("watches", UNSET)

        get_users_username_stats_by_thing_start_date_end_date_response_200_item = cls(
            collects=collects,
            comments=comments,
            day=day,
            derivatives=derivatives,
            downloads=downloads,
            likes=likes,
            makes=makes,
            user_id=user_id,
            views=views,
            watches=watches,
        )

        get_users_username_stats_by_thing_start_date_end_date_response_200_item.additional_properties = d
        return get_users_username_stats_by_thing_start_date_end_date_response_200_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
