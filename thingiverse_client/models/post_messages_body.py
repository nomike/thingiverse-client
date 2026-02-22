from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostMessagesBody")


@_attrs_define
class PostMessagesBody:
    """
    Attributes:
        body (str): The contents of the message Example: The actual message.
        subject (str): Set the subject of message Example: Message Subject.
        to_user (str): Set the username to whom the message will be sent. Example: Thingiverse.
    """

    body: str
    subject: str
    to_user: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        subject = self.subject

        to_user = self.to_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "subject": subject,
                "to_user": to_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        subject = d.pop("subject")

        to_user = d.pop("to_user")

        post_messages_body = cls(
            body=body,
            subject=subject,
            to_user=to_user,
        )

        post_messages_body.additional_properties = d
        return post_messages_body

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
