from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGrouptopicsGrouptopicIdUpdateBody")


@_attrs_define
class PostGrouptopicsGrouptopicIdUpdateBody:
    """
    Attributes:
        attachments (list[str] | Unset): Array of attachments ids to update Example: ['80111'].
        body (str | Unset): Set the body of the topic
        filenames (list[str] | Unset): Array of names of the files Example: ['File1.jpg', 'File2.jpg'].
        files (list[str] | Unset): Array of files Example: ['File1.jpg', 'File2.jpg'].
        name (str | Unset): Set the name of the topic
        tags (list[str] | Unset): Set the category of the thing. Uses full category name (eg. "3D Printer Parts")
            Example: ['tag1', 'tag2', 'tag3'].
    """

    attachments: list[str] | Unset = UNSET
    body: str | Unset = UNSET
    filenames: list[str] | Unset = UNSET
    files: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        body = self.body

        filenames: list[str] | Unset = UNSET
        if not isinstance(self.filenames, Unset):
            filenames = self.filenames

        files: list[str] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files

        name = self.name

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if body is not UNSET:
            field_dict["body"] = body
        if filenames is not UNSET:
            field_dict["filenames"] = filenames
        if files is not UNSET:
            field_dict["files"] = files
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachments = cast(list[str], d.pop("attachments", UNSET))

        body = d.pop("body", UNSET)

        filenames = cast(list[str], d.pop("filenames", UNSET))

        files = cast(list[str], d.pop("files", UNSET))

        name = d.pop("name", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        post_grouptopics_grouptopic_id_update_body = cls(
            attachments=attachments,
            body=body,
            filenames=filenames,
            files=files,
            name=name,
            tags=tags,
        )

        post_grouptopics_grouptopic_id_update_body.additional_properties = d
        return post_grouptopics_grouptopic_id_update_body

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
