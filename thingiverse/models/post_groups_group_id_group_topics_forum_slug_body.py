from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_groups_group_id_group_topics_forum_slug_body_files_item import (
        PostGroupsGroupIdGroupTopicsForumSlugBodyFilesItem,
    )


T = TypeVar("T", bound="PostGroupsGroupIdGroupTopicsForumSlugBody")


@_attrs_define
class PostGroupsGroupIdGroupTopicsForumSlugBody:
    """
    Attributes:
        body (str): Body text of Topic
        name (str): Name of Topic
        filenames (list[Any] | Unset): Array of filenames to be uploaded
        files (list[PostGroupsGroupIdGroupTopicsForumSlugBodyFilesItem] | Unset): Array of files to be uploaded
        tags (list[Any] | Unset): Array of tags
    """

    body: str
    name: str
    filenames: list[Any] | Unset = UNSET
    files: list[PostGroupsGroupIdGroupTopicsForumSlugBodyFilesItem] | Unset = UNSET
    tags: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        name = self.name

        filenames: list[Any] | Unset = UNSET
        if not isinstance(self.filenames, Unset):
            filenames = self.filenames

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        tags: list[Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "name": name,
            }
        )
        if filenames is not UNSET:
            field_dict["filenames"] = filenames
        if files is not UNSET:
            field_dict["files"] = files
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("body", (None, str(self.body).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.filenames, Unset):
            for filenames_item_element in self.filenames:
                files.append(
                    ("filenames", (None, str(filenames_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.files, Unset):
            for files_item_element in self.files:
                files.append(
                    (
                        "files",
                        (
                            None,
                            json.dumps(files_item_element.to_dict()).encode(),
                            "application/json",
                        ),
                    )
                )

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_groups_group_id_group_topics_forum_slug_body_files_item import (
            PostGroupsGroupIdGroupTopicsForumSlugBodyFilesItem,
        )

        d = dict(src_dict)
        body = d.pop("body")

        name = d.pop("name")

        filenames = cast(list[Any], d.pop("filenames", UNSET))

        _files = d.pop("files", UNSET)
        files: list[PostGroupsGroupIdGroupTopicsForumSlugBodyFilesItem] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = PostGroupsGroupIdGroupTopicsForumSlugBodyFilesItem.from_dict(
                    files_item_data
                )

                files.append(files_item)

        tags = cast(list[Any], d.pop("tags", UNSET))

        post_groups_group_id_group_topics_forum_slug_body = cls(
            body=body,
            name=name,
            filenames=filenames,
            files=files,
            tags=tags,
        )

        post_groups_group_id_group_topics_forum_slug_body.additional_properties = d
        return post_groups_group_id_group_topics_forum_slug_body

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
