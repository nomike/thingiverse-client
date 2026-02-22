from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.url_schema import UrlSchema


T = TypeVar("T", bound="GroupTopicTags")


@_attrs_define
class GroupTopicTags:
    """
    Attributes:
        absolute_url (str | Unset):
        count (int | Unset):
        name (str | Unset):
        url (UrlSchema | Unset):
    """

    absolute_url: str | Unset = UNSET
    count: int | Unset = UNSET
    name: str | Unset = UNSET
    url: UrlSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        absolute_url = self.absolute_url

        count = self.count

        name = self.name

        url: dict[str, Any] | Unset = UNSET
        if not isinstance(self.url, Unset):
            url = self.url.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if absolute_url is not UNSET:
            field_dict["absolute_url"] = absolute_url
        if count is not UNSET:
            field_dict["count"] = count
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.url_schema import UrlSchema

        d = dict(src_dict)
        absolute_url = d.pop("absolute_url", UNSET)

        count = d.pop("count", UNSET)

        name = d.pop("name", UNSET)

        _url = d.pop("url", UNSET)
        url: UrlSchema | Unset
        if isinstance(_url, Unset):
            url = UNSET
        else:
            url = UrlSchema.from_dict(_url)

        group_topic_tags = cls(
            absolute_url=absolute_url,
            count=count,
            name=name,
            url=url,
        )

        group_topic_tags.additional_properties = d
        return group_topic_tags

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
