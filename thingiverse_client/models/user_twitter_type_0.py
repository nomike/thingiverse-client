from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserTwitterType0")


@_attrs_define
class UserTwitterType0:
    """
    Attributes:
        account_name (str | Unset):  Example: CreativeTools.
        account_url (str | Unset):  Example: http://twitter.com/CreativeTools.
    """

    account_name: str | Unset = UNSET
    account_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        account_url = self.account_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_url is not UNSET:
            field_dict["account_url"] = account_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("account_name", UNSET)

        account_url = d.pop("account_url", UNSET)

        user_twitter_type_0 = cls(
            account_name=account_name,
            account_url=account_url,
        )

        user_twitter_type_0.additional_properties = d
        return user_twitter_type_0

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
