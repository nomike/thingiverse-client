from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_copies_copy_id_threaded_comments_response_200_comments import (
        GetCopiesCopyIdThreadedCommentsResponse200Comments,
    )
    from ..models.get_copies_copy_id_threaded_comments_response_200_users import (
        GetCopiesCopyIdThreadedCommentsResponse200Users,
    )


T = TypeVar("T", bound="GetCopiesCopyIdThreadedCommentsResponse200")


@_attrs_define
class GetCopiesCopyIdThreadedCommentsResponse200:
    """
    Attributes:
        comments (GetCopiesCopyIdThreadedCommentsResponse200Comments | Unset):
        users (GetCopiesCopyIdThreadedCommentsResponse200Users | Unset):
    """

    comments: GetCopiesCopyIdThreadedCommentsResponse200Comments | Unset = UNSET
    users: GetCopiesCopyIdThreadedCommentsResponse200Users | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_copies_copy_id_threaded_comments_response_200_comments import (
            GetCopiesCopyIdThreadedCommentsResponse200Comments,
        )
        from ..models.get_copies_copy_id_threaded_comments_response_200_users import (
            GetCopiesCopyIdThreadedCommentsResponse200Users,
        )

        d = dict(src_dict)
        _comments = d.pop("comments", UNSET)
        comments: GetCopiesCopyIdThreadedCommentsResponse200Comments | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = GetCopiesCopyIdThreadedCommentsResponse200Comments.from_dict(_comments)

        _users = d.pop("users", UNSET)
        users: GetCopiesCopyIdThreadedCommentsResponse200Users | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = GetCopiesCopyIdThreadedCommentsResponse200Users.from_dict(_users)

        get_copies_copy_id_threaded_comments_response_200 = cls(
            comments=comments,
            users=users,
        )

        get_copies_copy_id_threaded_comments_response_200.additional_properties = d
        return get_copies_copy_id_threaded_comments_response_200

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
