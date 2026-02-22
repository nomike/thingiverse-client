from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagSchema")


@_attrs_define
class TagSchema:
    """
    Attributes:
        absolute_url (str | Unset):  Example: /tag:Benchy.
        count (int | Unset):  Example: 76.
        name (str | Unset):  Example: Benchy.
        things_url (str | Unset):  Example: https://api.thingiverse.com/tags/benchy/things.
        url (str | Unset):  Example: https://staging.thingiverse.com/tags/benchy.
    """

    absolute_url: str | Unset = UNSET
    count: int | Unset = UNSET
    name: str | Unset = UNSET
    things_url: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        absolute_url = self.absolute_url

        count = self.count

        name = self.name

        things_url = self.things_url

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if absolute_url is not UNSET:
            field_dict["absolute_url"] = absolute_url
        if count is not UNSET:
            field_dict["count"] = count
        if name is not UNSET:
            field_dict["name"] = name
        if things_url is not UNSET:
            field_dict["things_url"] = things_url
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        absolute_url = d.pop("absolute_url", UNSET)

        count = d.pop("count", UNSET)

        name = d.pop("name", UNSET)

        things_url = d.pop("things_url", UNSET)

        url = d.pop("url", UNSET)

        tag_schema = cls(
            absolute_url=absolute_url,
            count=count,
            name=name,
            things_url=things_url,
            url=url,
        )

        tag_schema.additional_properties = d
        return tag_schema

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
