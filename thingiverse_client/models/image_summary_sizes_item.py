from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageSummarySizesItem")


@_attrs_define
class ImageSummarySizesItem:
    """
    Attributes:
        size (str | Unset):  Example: large.
        type_ (str | Unset):  Example: thumb.
        url (str | Unset):  Example:
            https://cdn.thingiverse.com/renders/62/ab/d7/e3/ea/1_3D-printed_3DBenchy_by_Creative-Tools.com_thumb_large.JPG.
    """

    size: str | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        image_summary_sizes_item = cls(
            size=size,
            type_=type_,
            url=url,
        )

        image_summary_sizes_item.additional_properties = d
        return image_summary_sizes_item

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
