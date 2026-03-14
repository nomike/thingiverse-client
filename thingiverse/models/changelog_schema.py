from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.changelog_schema_highlights_item import ChangelogSchemaHighlightsItem


T = TypeVar("T", bound="ChangelogSchema")


@_attrs_define
class ChangelogSchema:
    """
    Attributes:
        bugfixes (list[str] | Unset):
        data (str | Unset):  Example: 29-11-2022.
        features (list[str] | Unset):
        highlights (list[ChangelogSchemaHighlightsItem] | Unset):
        version (str | Unset):  Example: 2.49.0.
    """

    bugfixes: list[str] | Unset = UNSET
    data: str | Unset = UNSET
    features: list[str] | Unset = UNSET
    highlights: list[ChangelogSchemaHighlightsItem] | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bugfixes: list[str] | Unset = UNSET
        if not isinstance(self.bugfixes, Unset):
            bugfixes = self.bugfixes

        data = self.data

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        highlights: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.highlights, Unset):
            highlights = []
            for highlights_item_data in self.highlights:
                highlights_item = highlights_item_data.to_dict()
                highlights.append(highlights_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bugfixes is not UNSET:
            field_dict["bugfixes"] = bugfixes
        if data is not UNSET:
            field_dict["data"] = data
        if features is not UNSET:
            field_dict["features"] = features
        if highlights is not UNSET:
            field_dict["highlights"] = highlights
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.changelog_schema_highlights_item import ChangelogSchemaHighlightsItem

        d = dict(src_dict)
        bugfixes = cast(list[str], d.pop("bugfixes", UNSET))

        data = d.pop("data", UNSET)

        features = cast(list[str], d.pop("features", UNSET))

        _highlights = d.pop("highlights", UNSET)
        highlights: list[ChangelogSchemaHighlightsItem] | Unset = UNSET
        if _highlights is not UNSET:
            highlights = []
            for highlights_item_data in _highlights:
                highlights_item = ChangelogSchemaHighlightsItem.from_dict(highlights_item_data)

                highlights.append(highlights_item)

        version = d.pop("version", UNSET)

        changelog_schema = cls(
            bugfixes=bugfixes,
            data=data,
            features=features,
            highlights=highlights,
            version=version,
        )

        changelog_schema.additional_properties = d
        return changelog_schema

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
