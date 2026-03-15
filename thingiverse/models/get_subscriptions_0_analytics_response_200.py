from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_subscriptions_0_analytics_response_200_stats import (
        GetSubscriptions0AnalyticsResponse200Stats,
    )


T = TypeVar("T", bound="GetSubscriptions0AnalyticsResponse200")


@_attrs_define
class GetSubscriptions0AnalyticsResponse200:
    """
    Attributes:
        stats (GetSubscriptions0AnalyticsResponse200Stats | Unset):
        thing_count (int | Unset):
    """

    stats: GetSubscriptions0AnalyticsResponse200Stats | Unset = UNSET
    thing_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        thing_count = self.thing_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stats is not UNSET:
            field_dict["stats"] = stats
        if thing_count is not UNSET:
            field_dict["thing_count"] = thing_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscriptions_0_analytics_response_200_stats import (
            GetSubscriptions0AnalyticsResponse200Stats,
        )

        d = dict(src_dict)
        _stats = d.pop("stats", UNSET)
        stats: GetSubscriptions0AnalyticsResponse200Stats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = GetSubscriptions0AnalyticsResponse200Stats.from_dict(_stats)

        thing_count = d.pop("thing_count", UNSET)

        get_subscriptions_0_analytics_response_200 = cls(
            stats=stats,
            thing_count=thing_count,
        )

        get_subscriptions_0_analytics_response_200.additional_properties = d
        return get_subscriptions_0_analytics_response_200

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
