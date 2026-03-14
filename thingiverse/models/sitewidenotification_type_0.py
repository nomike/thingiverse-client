from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SitewidenotificationType0")


@_attrs_define
class SitewidenotificationType0:
    """
    Attributes:
        id (int | Unset):
        notification (str | Unset):
        notification_html (str | Unset):
        type_ (str | Unset):
    """

    id: int | Unset = UNSET
    notification: str | Unset = UNSET
    notification_html: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        notification = self.notification

        notification_html = self.notification_html

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if notification is not UNSET:
            field_dict["notification"] = notification
        if notification_html is not UNSET:
            field_dict["notification_html"] = notification_html
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        notification = d.pop("notification", UNSET)

        notification_html = d.pop("notification_html", UNSET)

        type_ = d.pop("type", UNSET)

        sitewidenotification_type_0 = cls(
            id=id,
            notification=notification,
            notification_html=notification_html,
            type_=type_,
        )

        sitewidenotification_type_0.additional_properties = d
        return sitewidenotification_type_0

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
