from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCommentsBody")


@_attrs_define
class PostCommentsBody:
    """
    Attributes:
        body (str): Set the body of the reply Example: Hello world!.
        recaptcha_token (str): Set the recaptcha token to confirm that the user is not a bot
        target_id (int):  Example: 10.
        target_type (str): What is the type this comment should be posted on (thing, make, etc) Example: thing.
        parent_id (int | Unset): If it's a nested comment, set the id of the parent comment here. (optional!)
    """

    body: str
    recaptcha_token: str
    target_id: int
    target_type: str
    parent_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        recaptcha_token = self.recaptcha_token

        target_id = self.target_id

        target_type = self.target_type

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "recaptcha_token": recaptcha_token,
                "target_id": target_id,
                "target_type": target_type,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        recaptcha_token = d.pop("recaptcha_token")

        target_id = d.pop("target_id")

        target_type = d.pop("target_type")

        parent_id = d.pop("parent_id", UNSET)

        post_comments_body = cls(
            body=body,
            recaptcha_token=recaptcha_token,
            target_id=target_id,
            target_type=target_type,
            parent_id=parent_id,
        )

        post_comments_body.additional_properties = d
        return post_comments_body

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
