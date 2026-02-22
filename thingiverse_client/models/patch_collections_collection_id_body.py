from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchCollectionsCollectionIdBody")


@_attrs_define
class PatchCollectionsCollectionIdBody:
    """
    Attributes:
        description (Any | Unset): Description of the collection
        featured_thing_id (Any | Unset): Featured Thing id from the collection
        name (Any | Unset): Name of the collection
    """

    description: Any | Unset = UNSET
    featured_thing_id: Any | Unset = UNSET
    name: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        featured_thing_id = self.featured_thing_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if featured_thing_id is not UNSET:
            field_dict["featured_thing_id"] = featured_thing_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        featured_thing_id = d.pop("featured_thing_id", UNSET)

        name = d.pop("name", UNSET)

        patch_collections_collection_id_body = cls(
            description=description,
            featured_thing_id=featured_thing_id,
            name=name,
        )

        patch_collections_collection_id_body.additional_properties = d
        return patch_collections_collection_id_body

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
