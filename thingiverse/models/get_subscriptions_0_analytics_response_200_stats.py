from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSubscriptions0AnalyticsResponse200Stats")


@_attrs_define
class GetSubscriptions0AnalyticsResponse200Stats:
    """
    Attributes:
        collects (str | Unset):
        downloads (str | Unset):
        likes (str | Unset):
        makes (str | Unset):
        views (str | Unset):
    """

    collects: str | Unset = UNSET
    downloads: str | Unset = UNSET
    likes: str | Unset = UNSET
    makes: str | Unset = UNSET
    views: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collects = self.collects

        downloads = self.downloads

        likes = self.likes

        makes = self.makes

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collects is not UNSET:
            field_dict["collects"] = collects
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if likes is not UNSET:
            field_dict["likes"] = likes
        if makes is not UNSET:
            field_dict["makes"] = makes
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collects = d.pop("collects", UNSET)

        downloads = d.pop("downloads", UNSET)

        likes = d.pop("likes", UNSET)

        makes = d.pop("makes", UNSET)

        views = d.pop("views", UNSET)

        get_subscriptions_0_analytics_response_200_stats = cls(
            collects=collects,
            downloads=downloads,
            likes=likes,
            makes=makes,
            views=views,
        )

        get_subscriptions_0_analytics_response_200_stats.additional_properties = d
        return get_subscriptions_0_analytics_response_200_stats

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
