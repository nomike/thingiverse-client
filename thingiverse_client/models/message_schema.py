from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageSchema")


@_attrs_define
class MessageSchema:
    """
    Attributes:
        add_date (datetime.datetime | Unset):
        comment_id (int | Unset):
        from_user_id (int | Unset):
        id (int | Unset):
        modified_date (datetime.datetime | Unset):
        subject (str | Unset):
        to_user_id (int | Unset):
    """

    add_date: datetime.datetime | Unset = UNSET
    comment_id: int | Unset = UNSET
    from_user_id: int | Unset = UNSET
    id: int | Unset = UNSET
    modified_date: datetime.datetime | Unset = UNSET
    subject: str | Unset = UNSET
    to_user_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_date: str | Unset = UNSET
        if not isinstance(self.add_date, Unset):
            add_date = self.add_date.isoformat()

        comment_id = self.comment_id

        from_user_id = self.from_user_id

        id = self.id

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        subject = self.subject

        to_user_id = self.to_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_date is not UNSET:
            field_dict["add_date"] = add_date
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id
        if from_user_id is not UNSET:
            field_dict["from_user_id"] = from_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if modified_date is not UNSET:
            field_dict["modified_date"] = modified_date
        if subject is not UNSET:
            field_dict["subject"] = subject
        if to_user_id is not UNSET:
            field_dict["to_user_id"] = to_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _add_date = d.pop("add_date", UNSET)
        add_date: datetime.datetime | Unset
        if isinstance(_add_date, Unset):
            add_date = UNSET
        else:
            add_date = isoparse(_add_date)

        comment_id = d.pop("comment_id", UNSET)

        from_user_id = d.pop("from_user_id", UNSET)

        id = d.pop("id", UNSET)

        _modified_date = d.pop("modified_date", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        subject = d.pop("subject", UNSET)

        to_user_id = d.pop("to_user_id", UNSET)

        message_schema = cls(
            add_date=add_date,
            comment_id=comment_id,
            from_user_id=from_user_id,
            id=id,
            modified_date=modified_date,
            subject=subject,
            to_user_id=to_user_id,
        )

        message_schema.additional_properties = d
        return message_schema

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
