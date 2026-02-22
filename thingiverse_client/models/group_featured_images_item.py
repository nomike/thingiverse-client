from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupFeaturedImagesItem")


@_attrs_define
class GroupFeaturedImagesItem:
    """
    Attributes:
        url_image (str | Unset):
        url_thing (str | Unset):
    """

    url_image: str | Unset = UNSET
    url_thing: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_image = self.url_image

        url_thing = self.url_thing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url_image is not UNSET:
            field_dict["url_image"] = url_image
        if url_thing is not UNSET:
            field_dict["url_thing"] = url_thing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url_image = d.pop("url_image", UNSET)

        url_thing = d.pop("url_thing", UNSET)

        group_featured_images_item = cls(
            url_image=url_image,
            url_thing=url_thing,
        )

        group_featured_images_item.additional_properties = d
        return group_featured_images_item

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
