from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_copies_copy_id_threaded_comments_response_200_users_additional_property_is_admin import (
    GetCopiesCopyIdThreadedCommentsResponse200UsersAdditionalPropertyIsAdmin,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCopiesCopyIdThreadedCommentsResponse200UsersAdditionalProperty")


@_attrs_define
class GetCopiesCopyIdThreadedCommentsResponse200UsersAdditionalProperty:
    """
    Attributes:
        is_admin (GetCopiesCopyIdThreadedCommentsResponse200UsersAdditionalPropertyIsAdmin | Unset):
        user_avatar (str | Unset):
        user_name (str | Unset):
    """

    is_admin: GetCopiesCopyIdThreadedCommentsResponse200UsersAdditionalPropertyIsAdmin | Unset = (
        UNSET
    )
    user_avatar: str | Unset = UNSET
    user_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_admin: int | Unset = UNSET
        if not isinstance(self.is_admin, Unset):
            is_admin = self.is_admin.value

        user_avatar = self.user_avatar

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if user_avatar is not UNSET:
            field_dict["user_avatar"] = user_avatar
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _is_admin = d.pop("is_admin", UNSET)
        is_admin: GetCopiesCopyIdThreadedCommentsResponse200UsersAdditionalPropertyIsAdmin | Unset
        if isinstance(_is_admin, Unset):
            is_admin = UNSET
        else:
            is_admin = GetCopiesCopyIdThreadedCommentsResponse200UsersAdditionalPropertyIsAdmin(
                _is_admin
            )

        user_avatar = d.pop("user_avatar", UNSET)

        user_name = d.pop("user_name", UNSET)

        get_copies_copy_id_threaded_comments_response_200_users_additional_property = cls(
            is_admin=is_admin,
            user_avatar=user_avatar,
            user_name=user_name,
        )

        get_copies_copy_id_threaded_comments_response_200_users_additional_property.additional_properties = d
        return get_copies_copy_id_threaded_comments_response_200_users_additional_property

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
