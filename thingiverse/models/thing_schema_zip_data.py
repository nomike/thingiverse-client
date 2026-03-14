from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thing_schema_zip_data_files_item import ThingSchemaZipDataFilesItem


T = TypeVar("T", bound="ThingSchemaZipData")


@_attrs_define
class ThingSchemaZipData:
    """
    Attributes:
        files (list[ThingSchemaZipDataFilesItem] | Unset):
    """

    files: list[ThingSchemaZipDataFilesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thing_schema_zip_data_files_item import ThingSchemaZipDataFilesItem

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: list[ThingSchemaZipDataFilesItem] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = ThingSchemaZipDataFilesItem.from_dict(files_item_data)

                files.append(files_item)

        thing_schema_zip_data = cls(
            files=files,
        )

        thing_schema_zip_data.additional_properties = d
        return thing_schema_zip_data

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
