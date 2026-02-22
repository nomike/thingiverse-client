from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeaturedSchemaSpotlightImages")


@_attrs_define
class FeaturedSchemaSpotlightImages:
    """
    Attributes:
        large (str | Unset):
        small (str | Unset):
    """

    large: str | Unset = UNSET
    small: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        large = self.large

        small = self.small

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if large is not UNSET:
            field_dict["large"] = large
        if small is not UNSET:
            field_dict["small"] = small

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        large = d.pop("large", UNSET)

        small = d.pop("small", UNSET)

        featured_schema_spotlight_images = cls(
            large=large,
            small=small,
        )

        featured_schema_spotlight_images.additional_properties = d
        return featured_schema_spotlight_images

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
