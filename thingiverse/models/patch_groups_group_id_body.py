from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchGroupsGroupIdBody")


@_attrs_define
class PatchGroupsGroupIdBody:
    """
    Attributes:
        description (str | Unset): Replace the description of the group
        featured_things (list[Any] | Unset): Replace the featured things of the group
        name (str | Unset): Replace the name of the group
    """

    description: str | Unset = UNSET
    featured_things: list[Any] | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        featured_things: list[Any] | Unset = UNSET
        if not isinstance(self.featured_things, Unset):
            featured_things = self.featured_things

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if featured_things is not UNSET:
            field_dict["featuredThings"] = featured_things
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        featured_things = cast(list[Any], d.pop("featuredThings", UNSET))

        name = d.pop("name", UNSET)

        patch_groups_group_id_body = cls(
            description=description,
            featured_things=featured_things,
            name=name,
        )

        patch_groups_group_id_body.additional_properties = d
        return patch_groups_group_id_body

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
