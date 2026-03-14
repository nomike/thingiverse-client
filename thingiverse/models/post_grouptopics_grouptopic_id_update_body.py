from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_grouptopics_grouptopic_id_update_body_attachments_item import (
        PostGrouptopicsGrouptopicIdUpdateBodyAttachmentsItem,
    )
    from ..models.post_grouptopics_grouptopic_id_update_body_filenames_item import (
        PostGrouptopicsGrouptopicIdUpdateBodyFilenamesItem,
    )
    from ..models.post_grouptopics_grouptopic_id_update_body_files_item import (
        PostGrouptopicsGrouptopicIdUpdateBodyFilesItem,
    )
    from ..models.post_grouptopics_grouptopic_id_update_body_tags_item import (
        PostGrouptopicsGrouptopicIdUpdateBodyTagsItem,
    )


T = TypeVar("T", bound="PostGrouptopicsGrouptopicIdUpdateBody")


@_attrs_define
class PostGrouptopicsGrouptopicIdUpdateBody:
    """
    Attributes:
        attachments (list[PostGrouptopicsGrouptopicIdUpdateBodyAttachmentsItem] | Unset): Array of atachments ids to
            update Example: ['80111'].
        body (str | Unset): Set the body of the topic
        filenames (list[PostGrouptopicsGrouptopicIdUpdateBodyFilenamesItem] | Unset): Array of names of the files
            Example: ['File1.jpg', 'File2.jpg'].
        files (list[PostGrouptopicsGrouptopicIdUpdateBodyFilesItem] | Unset): Array of files Example: ['File1.jpg',
            'File2.jpg'].
        name (str | Unset): Set the name of the topic
        tags (list[PostGrouptopicsGrouptopicIdUpdateBodyTagsItem] | Unset): Set the category of the thing. Uses full
            category name (eg. "3D Printer Parts") Example: ['tag1', 'tag2', 'tag3'].
    """

    attachments: list[PostGrouptopicsGrouptopicIdUpdateBodyAttachmentsItem] | Unset = UNSET
    body: str | Unset = UNSET
    filenames: list[PostGrouptopicsGrouptopicIdUpdateBodyFilenamesItem] | Unset = UNSET
    files: list[PostGrouptopicsGrouptopicIdUpdateBodyFilesItem] | Unset = UNSET
    name: str | Unset = UNSET
    tags: list[PostGrouptopicsGrouptopicIdUpdateBodyTagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        body = self.body

        filenames: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filenames, Unset):
            filenames = []
            for filenames_item_data in self.filenames:
                filenames_item = filenames_item_data.to_dict()
                filenames.append(filenames_item)

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        name = self.name

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

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
        from ..models.post_grouptopics_grouptopic_id_update_body_attachments_item import (
            PostGrouptopicsGrouptopicIdUpdateBodyAttachmentsItem,
        )
        from ..models.post_grouptopics_grouptopic_id_update_body_filenames_item import (
            PostGrouptopicsGrouptopicIdUpdateBodyFilenamesItem,
        )
        from ..models.post_grouptopics_grouptopic_id_update_body_files_item import (
            PostGrouptopicsGrouptopicIdUpdateBodyFilesItem,
        )
        from ..models.post_grouptopics_grouptopic_id_update_body_tags_item import (
            PostGrouptopicsGrouptopicIdUpdateBodyTagsItem,
        )

        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: list[PostGrouptopicsGrouptopicIdUpdateBodyAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = PostGrouptopicsGrouptopicIdUpdateBodyAttachmentsItem.from_dict(
                    attachments_item_data
                )

                attachments.append(attachments_item)

        body = d.pop("body", UNSET)

        _filenames = d.pop("filenames", UNSET)
        filenames: list[PostGrouptopicsGrouptopicIdUpdateBodyFilenamesItem] | Unset = UNSET
        if _filenames is not UNSET:
            filenames = []
            for filenames_item_data in _filenames:
                filenames_item = PostGrouptopicsGrouptopicIdUpdateBodyFilenamesItem.from_dict(
                    filenames_item_data
                )

                filenames.append(filenames_item)

        _files = d.pop("files", UNSET)
        files: list[PostGrouptopicsGrouptopicIdUpdateBodyFilesItem] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = PostGrouptopicsGrouptopicIdUpdateBodyFilesItem.from_dict(
                    files_item_data
                )

                files.append(files_item)

        name = d.pop("name", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[PostGrouptopicsGrouptopicIdUpdateBodyTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = PostGrouptopicsGrouptopicIdUpdateBodyTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

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
