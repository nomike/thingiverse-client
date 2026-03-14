from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_schema import CategorySchema


T = TypeVar("T", bound="GetCategoriesSlugResponse200")


@_attrs_define
class GetCategoriesSlugResponse200:
    """
    Attributes:
        children (list[CategorySchema] | Unset):
        count (int | Unset):
        name (str | Unset):
        preview_image (str | Unset):
        things_url (str | Unset):
        thumbnail (str | Unset):
        url (str | Unset):
    """

    children: list[CategorySchema] | Unset = UNSET
    count: int | Unset = UNSET
    name: str | Unset = UNSET
    preview_image: str | Unset = UNSET
    things_url: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        count = self.count

        name = self.name

        preview_image = self.preview_image

        things_url = self.things_url

        thumbnail = self.thumbnail

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if count is not UNSET:
            field_dict["count"] = count
        if name is not UNSET:
            field_dict["name"] = name
        if preview_image is not UNSET:
            field_dict["preview_image"] = preview_image
        if things_url is not UNSET:
            field_dict["things_url"] = things_url
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_schema import CategorySchema

        d = dict(src_dict)
        _children = d.pop("children", UNSET)
        children: list[CategorySchema] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = CategorySchema.from_dict(children_item_data)

                children.append(children_item)

        count = d.pop("count", UNSET)

        name = d.pop("name", UNSET)

        preview_image = d.pop("preview_image", UNSET)

        things_url = d.pop("things_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        url = d.pop("url", UNSET)

        get_categories_slug_response_200 = cls(
            children=children,
            count=count,
            name=name,
            preview_image=preview_image,
            things_url=things_url,
            thumbnail=thumbnail,
            url=url,
        )

        get_categories_slug_response_200.additional_properties = d
        return get_categories_slug_response_200

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
