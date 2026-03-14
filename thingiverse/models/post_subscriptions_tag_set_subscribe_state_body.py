from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSubscriptionsTagSetSubscribeStateBody")


@_attrs_define
class PostSubscriptionsTagSetSubscribeStateBody:
    """
    Attributes:
        action (str): Set the type of action Example: subscribe.
        target_type (str): Set the type of target to which the user will be subscribed Example: thing.
    """

    action: str
    target_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        target_type = self.target_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "target_type": target_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        target_type = d.pop("target_type")

        post_subscriptions_tag_set_subscribe_state_body = cls(
            action=action,
            target_type=target_type,
        )

        post_subscriptions_tag_set_subscribe_state_body.additional_properties = d
        return post_subscriptions_tag_set_subscribe_state_body

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
