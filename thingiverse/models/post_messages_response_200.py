from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_messages_response_200_user import PostMessagesResponse200User


T = TypeVar("T", bound="PostMessagesResponse200")


@_attrs_define
class PostMessagesResponse200:
    """
    Attributes:
        id (int | Unset):
        is_read (int | Unset):
        subject (str | Unset):  Example: Message Subject.
        user (PostMessagesResponse200User | Unset):
    """

    id: int | Unset = UNSET
    is_read: int | Unset = UNSET
    subject: str | Unset = UNSET
    user: PostMessagesResponse200User | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_read = self.is_read

        subject = self.subject

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_read is not UNSET:
            field_dict["is_read"] = is_read
        if subject is not UNSET:
            field_dict["subject"] = subject
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_messages_response_200_user import PostMessagesResponse200User

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_read = d.pop("is_read", UNSET)

        subject = d.pop("subject", UNSET)

        _user = d.pop("user", UNSET)
        user: PostMessagesResponse200User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PostMessagesResponse200User.from_dict(_user)

        post_messages_response_200 = cls(
            id=id,
            is_read=is_read,
            subject=subject,
            user=user,
        )

        post_messages_response_200.additional_properties = d
        return post_messages_response_200

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
