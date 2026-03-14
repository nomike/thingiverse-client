from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSubscriptions0DashboardSourcesResponse200AdditionalPropertyItem")


@_attrs_define
class GetSubscriptions0DashboardSourcesResponse200AdditionalPropertyItem:
    """
    Attributes:
        image_url (str | Unset):
        name (str | Unset):
        target_id (int | Unset):  Example: 1.
        target_type (str | Unset):
        target_url (str | Unset):
    """

    image_url: str | Unset = UNSET
    name: str | Unset = UNSET
    target_id: int | Unset = UNSET
    target_type: str | Unset = UNSET
    target_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        name = self.name

        target_id = self.target_id

        target_type = self.target_type

        target_url = self.target_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if name is not UNSET:
            field_dict["name"] = name
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if target_url is not UNSET:
            field_dict["target_url"] = target_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_url = d.pop("image_url", UNSET)

        name = d.pop("name", UNSET)

        target_id = d.pop("target_id", UNSET)

        target_type = d.pop("target_type", UNSET)

        target_url = d.pop("target_url", UNSET)

        get_subscriptions_0_dashboard_sources_response_200_additional_property_item = cls(
            image_url=image_url,
            name=name,
            target_id=target_id,
            target_type=target_type,
            target_url=target_url,
        )

        get_subscriptions_0_dashboard_sources_response_200_additional_property_item.additional_properties = d
        return get_subscriptions_0_dashboard_sources_response_200_additional_property_item

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
