from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_things_body_license import PostThingsBodyLicense
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostThingsBody")


@_attrs_define
class PostThingsBody:
    """
    Attributes:
        category (str): Set the category of the thing. Uses full category name (eg. "3D Printer Parts") Example: Other.
        license_ (PostThingsBodyLicense): One of cc, cc-sa, cc-nd, cc-nc-sa, cc-nc-nd, pd0, gpl, lgpl, bsd. Set license.
            Example: cc.
        name (str): Set the name of the thing Example: Test thing.
        ancestors (list[int] | Unset): An array of thing ids that this thing is derived from. Example: [2000].
        description (str | Unset): Set the description. Example: Some kind of description about the thing that you are
            posting.
        instructions (str | Unset): Set the instructions. Example: This is an instruction!.
        is_customizer (bool | Unset): Toggle whether this thing is a customizer. Default is false.
        is_remix (bool | Unset): Is this thing remixed from another thing
        is_wip (bool | Unset): Toggle whether this thing is a work in progress. Default is false.
        tags (list[str] | Unset): An array of strings containing tag names. Sets all current tags. Example: ['test',
            'tag'].
    """

    category: str
    license_: PostThingsBodyLicense
    name: str
    ancestors: list[int] | Unset = UNSET
    description: str | Unset = UNSET
    instructions: str | Unset = UNSET
    is_customizer: bool | Unset = UNSET
    is_remix: bool | Unset = UNSET
    is_wip: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        license_ = self.license_.value

        name = self.name

        ancestors: list[int] | Unset = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = self.ancestors

        description = self.description

        instructions = self.instructions

        is_customizer = self.is_customizer

        is_remix = self.is_remix

        is_wip = self.is_wip

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "license": license_,
                "name": name,
            }
        )
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if description is not UNSET:
            field_dict["description"] = description
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if is_customizer is not UNSET:
            field_dict["is_customizer"] = is_customizer
        if is_remix is not UNSET:
            field_dict["is_remix"] = is_remix
        if is_wip is not UNSET:
            field_dict["is_wip"] = is_wip
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        license_ = PostThingsBodyLicense(d.pop("license"))

        name = d.pop("name")

        ancestors = cast(list[int], d.pop("ancestors", UNSET))

        description = d.pop("description", UNSET)

        instructions = d.pop("instructions", UNSET)

        is_customizer = d.pop("is_customizer", UNSET)

        is_remix = d.pop("is_remix", UNSET)

        is_wip = d.pop("is_wip", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        post_things_body = cls(
            category=category,
            license_=license_,
            name=name,
            ancestors=ancestors,
            description=description,
            instructions=instructions,
            is_customizer=is_customizer,
            is_remix=is_remix,
            is_wip=is_wip,
            tags=tags,
        )

        post_things_body.additional_properties = d
        return post_things_body

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
