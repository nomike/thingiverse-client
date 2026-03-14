from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCategoriesResponse200Item")


@_attrs_define
class GetCategoriesResponse200Item:
    """
    Attributes:
        count (int | Unset):
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        things_url (str | Unset):
        url (str | Unset):
    """

    count: int | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    things_url: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        id = self.id

        name = self.name

        slug = self.slug

        things_url = self.things_url

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if things_url is not UNSET:
            field_dict["things_url"] = things_url
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        things_url = d.pop("things_url", UNSET)

        url = d.pop("url", UNSET)

        get_categories_response_200_item = cls(
            count=count,
            id=id,
            name=name,
            slug=slug,
            things_url=things_url,
            url=url,
        )

        get_categories_response_200_item.additional_properties = d
        return get_categories_response_200_item

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
