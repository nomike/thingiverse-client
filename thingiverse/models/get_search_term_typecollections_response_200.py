from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_schema import CollectionSchema


T = TypeVar("T", bound="GetSearchTermTypecollectionsResponse200")


@_attrs_define
class GetSearchTermTypecollectionsResponse200:
    """
    Attributes:
        hits (list[CollectionSchema] | Unset):
        total (int | Unset):
    """

    hits: list[CollectionSchema] | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hits, Unset):
            hits = []
            for hits_item_data in self.hits:
                hits_item = hits_item_data.to_dict()
                hits.append(hits_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hits is not UNSET:
            field_dict["hits"] = hits
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_schema import CollectionSchema

        d = dict(src_dict)
        _hits = d.pop("hits", UNSET)
        hits: list[CollectionSchema] | Unset = UNSET
        if _hits is not UNSET:
            hits = []
            for hits_item_data in _hits:
                hits_item = CollectionSchema.from_dict(hits_item_data)

                hits.append(hits_item)

        total = d.pop("total", UNSET)

        get_search_term_typecollections_response_200 = cls(
            hits=hits,
            total=total,
        )

        get_search_term_typecollections_response_200.additional_properties = d
        return get_search_term_typecollections_response_200

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
