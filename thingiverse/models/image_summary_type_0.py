from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_summary_sizes_item import ImageSummarySizesItem


T = TypeVar("T", bound="ImageSummaryType0")


@_attrs_define
class ImageSummaryType0:
    """
    Attributes:
        added (datetime.datetime | Unset):  Example: 2015-04-09T12:55:23+00:00.
        id (int | Unset):  Example: 2012326.
        name (str | Unset):  Example: 1_3D-printed_3DBenchy_by_Creative-Tools.com.JPG.
        sizes (list[ImageSummarySizesItem] | Unset):
        url (str | Unset):  Example:
            https://cdn.thingiverse.com/assets/ee/dc/9a/fb/74/1_3D-printed_3DBenchy_by_Creative-Tools.com.JPG.
    """

    added: datetime.datetime | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    sizes: list[ImageSummarySizesItem] | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added: str | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        id = self.id

        name = self.name

        sizes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sizes, Unset):
            sizes = []
            for sizes_item_data in self.sizes:
                sizes_item = sizes_item_data.to_dict()
                sizes.append(sizes_item)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sizes is not UNSET:
            field_dict["sizes"] = sizes
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_summary_sizes_item import ImageSummarySizesItem

        d = dict(src_dict)
        _added = d.pop("added", UNSET)
        added: datetime.datetime | Unset
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _sizes = d.pop("sizes", UNSET)
        sizes: list[ImageSummarySizesItem] | Unset = UNSET
        if _sizes is not UNSET:
            sizes = []
            for sizes_item_data in _sizes:
                sizes_item = ImageSummarySizesItem.from_dict(sizes_item_data)

                sizes.append(sizes_item)

        url = d.pop("url", UNSET)

        image_summary_type_0 = cls(
            added=added,
            id=id,
            name=name,
            sizes=sizes,
            url=url,
        )

        image_summary_type_0.additional_properties = d
        return image_summary_type_0

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
