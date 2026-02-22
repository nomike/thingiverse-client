from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSubscriptions0DashboardResponse200ItemsItemImage")


@_attrs_define
class GetSubscriptions0DashboardResponse200ItemsItemImage:
    """
    Attributes:
        img_src (str | Unset):
        link (str | Unset):
        title (str | Unset):
    """

    img_src: str | Unset = UNSET
    link: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        img_src = self.img_src

        link = self.link

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if img_src is not UNSET:
            field_dict["img_src"] = img_src
        if link is not UNSET:
            field_dict["link"] = link
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        img_src = d.pop("img_src", UNSET)

        link = d.pop("link", UNSET)

        title = d.pop("title", UNSET)

        get_subscriptions_0_dashboard_response_200_items_item_image = cls(
            img_src=img_src,
            link=link,
            title=title,
        )

        get_subscriptions_0_dashboard_response_200_items_item_image.additional_properties = d
        return get_subscriptions_0_dashboard_response_200_items_item_image

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
