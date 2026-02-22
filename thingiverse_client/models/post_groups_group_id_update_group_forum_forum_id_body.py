from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostGroupsGroupIdUpdateGroupForumForumIdBody")


@_attrs_define
class PostGroupsGroupIdUpdateGroupForumForumIdBody:
    """
    Attributes:
        description (str): Set the description of the forum
        name (str): Set the name of the forum
        file (File | Unset): Set the image. Available formats are jpeg, jpg, gif, png
        filename (str | Unset): Set the file name
    """

    description: str
    name: str
    file: File | Unset = UNSET
    filename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("description", (None, str(self.description).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.filename, Unset):
            files.append(("filename", (None, str(self.filename).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        filename = d.pop("filename", UNSET)

        post_groups_group_id_update_group_forum_forum_id_body = cls(
            description=description,
            name=name,
            file=file,
            filename=filename,
        )

        post_groups_group_id_update_group_forum_forum_id_body.additional_properties = d
        return post_groups_group_id_update_group_forum_forum_id_body

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
