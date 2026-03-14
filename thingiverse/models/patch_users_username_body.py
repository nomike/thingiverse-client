from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchUsersUsernameBody")


@_attrs_define
class PatchUsersUsernameBody:
    """
    Attributes:
        bio (str | Unset): Replace the biography for this user.
        default_license (str | Unset): One of cc, cc-sa, cc-nd, cc-nc, cc-nc-sa, cc-nc-nd, pd0, gpl, lgpl, bsd. Update
            default license.
        first_name (str | Unset): Replace the first name of this user.
        last_name (str | Unset): Replace the last name of this user.
        location (str | Unset): Replace the location for this user.
    """

    bio: str | Unset = UNSET
    default_license: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bio = self.bio

        default_license = self.default_license

        first_name = self.first_name

        last_name = self.last_name

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bio is not UNSET:
            field_dict["bio"] = bio
        if default_license is not UNSET:
            field_dict["default_license"] = default_license
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bio = d.pop("bio", UNSET)

        default_license = d.pop("default_license", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        location = d.pop("location", UNSET)

        patch_users_username_body = cls(
            bio=bio,
            default_license=default_license,
            first_name=first_name,
            last_name=last_name,
            location=location,
        )

        patch_users_username_body.additional_properties = d
        return patch_users_username_body

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
