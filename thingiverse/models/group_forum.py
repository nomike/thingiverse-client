from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupForum")


@_attrs_define
class GroupForum:
    """
    Attributes:
        description (str | Unset):
        id (int | Unset):
        name (str | Unset):
        slug (str | Unset):
        tags (list[str] | Unset):
        thumbnail (str | Unset):
        topic_count (int | Unset):
    """

    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    thumbnail: str | Unset = UNSET
    topic_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        slug = self.slug

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        thumbnail = self.thumbnail

        topic_count = self.topic_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tags is not UNSET:
            field_dict["tags"] = tags
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if topic_count is not UNSET:
            field_dict["topic_count"] = topic_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        thumbnail = d.pop("thumbnail", UNSET)

        topic_count = d.pop("topic_count", UNSET)

        group_forum = cls(
            description=description,
            id=id,
            name=name,
            slug=slug,
            tags=tags,
            thumbnail=thumbnail,
            topic_count=topic_count,
        )

        group_forum.additional_properties = d
        return group_forum

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
