from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchThingsThingIdBody")


@_attrs_define
class PatchThingsThingIdBody:
    """
    Attributes:
        ancestors (list[int] | Unset): array of id's of all things that this was remixed from. Note that is_remix should
            be set to true as well Example: [2000].
        category (int | str | Unset): Replace the category of the thing with an category id. This field also supports
            the old way of providing the full category name (eg. "3D Printer Parts") as string.
        description (str | Unset): Replace the description.
        instructions (str | Unset): Replace the instructions.
        is_remix (bool | Unset): Is this thing remixed from another thing
        is_wip (bool | Unset): Toggle whether this thing is a work in progress.
        license_ (str | Unset): One of cc, cc-sa, cc-nd, cc-nc-sa, cc-nc-nd, pd0, gpl, lgpl, bsd. Replace license
        name (str | Unset): Replace the name of the thing
        tags (list[str] | Unset): An array of strings containing tag names. Replaces all current tags.
    """

    ancestors: list[int] | Unset = UNSET
    category: int | str | Unset = UNSET
    description: str | Unset = UNSET
    instructions: str | Unset = UNSET
    is_remix: bool | Unset = UNSET
    is_wip: bool | Unset = UNSET
    license_: str | Unset = UNSET
    name: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ancestors: list[int] | Unset = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = self.ancestors

        category: int | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        description = self.description

        instructions = self.instructions

        is_remix = self.is_remix

        is_wip = self.is_wip

        license_ = self.license_

        name = self.name

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if is_remix is not UNSET:
            field_dict["is_remix"] = is_remix
        if is_wip is not UNSET:
            field_dict["is_wip"] = is_wip
        if license_ is not UNSET:
            field_dict["license"] = license_
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ancestors = cast(list[int], d.pop("ancestors", UNSET))

        def _parse_category(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        description = d.pop("description", UNSET)

        instructions = d.pop("instructions", UNSET)

        is_remix = d.pop("is_remix", UNSET)

        is_wip = d.pop("is_wip", UNSET)

        license_ = d.pop("license", UNSET)

        name = d.pop("name", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        patch_things_thing_id_body = cls(
            ancestors=ancestors,
            category=category,
            description=description,
            instructions=instructions,
            is_remix=is_remix,
            is_wip=is_wip,
            license_=license_,
            name=name,
            tags=tags,
        )

        patch_things_thing_id_body.additional_properties = d
        return patch_things_thing_id_body

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
