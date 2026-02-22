from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostThingopsIdsMoveBody")


@_attrs_define
class PostThingopsIdsMoveBody:
    """
    Attributes:
        source_collection_id (int): Set the id of the collection where the specified thing is located
        target_collection_id (int): Set the id of the collection where the specified thing will be moved
    """

    source_collection_id: int
    target_collection_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_collection_id = self.source_collection_id

        target_collection_id = self.target_collection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_collection_id": source_collection_id,
                "target_collection_id": target_collection_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_collection_id = d.pop("source_collection_id")

        target_collection_id = d.pop("target_collection_id")

        post_thingops_ids_move_body = cls(
            source_collection_id=source_collection_id,
            target_collection_id=target_collection_id,
        )

        post_thingops_ids_move_body.additional_properties = d
        return post_thingops_ids_move_body

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
