from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_schema_sources_item_type_0 import EventSchemaSourcesItemType0
    from ..models.event_schema_subscription_type_0 import EventSchemaSubscriptionType0
    from ..models.event_schema_targets_item import EventSchemaTargetsItem


T = TypeVar("T", bound="EventSchema")


@_attrs_define
class EventSchema:
    """
    Attributes:
        id (int | Unset):
        message (str | Unset):
        sources (list[EventSchemaSourcesItemType0] | Unset):
        subscription (EventSchemaSubscriptionType0 | None | Unset):
        targets (list[EventSchemaTargetsItem] | Unset):
        time (datetime.datetime | Unset):
        type_ (int | Unset):
    """

    id: int | Unset = UNSET
    message: str | Unset = UNSET
    sources: list[EventSchemaSourcesItemType0] | Unset = UNSET
    subscription: EventSchemaSubscriptionType0 | None | Unset = UNSET
    targets: list[EventSchemaTargetsItem] | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    type_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_schema_sources_item_type_0 import EventSchemaSourcesItemType0
        from ..models.event_schema_subscription_type_0 import EventSchemaSubscriptionType0

        id = self.id

        message = self.message

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item: dict[str, Any]
                if isinstance(sources_item_data, EventSchemaSourcesItemType0):
                    sources_item = sources_item_data.to_dict()

                sources.append(sources_item)

        subscription: dict[str, Any] | None | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        elif isinstance(self.subscription, EventSchemaSubscriptionType0):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if sources is not UNSET:
            field_dict["sources"] = sources
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if targets is not UNSET:
            field_dict["targets"] = targets
        if time is not UNSET:
            field_dict["time"] = time
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_schema_sources_item_type_0 import EventSchemaSourcesItemType0
        from ..models.event_schema_subscription_type_0 import EventSchemaSubscriptionType0
        from ..models.event_schema_targets_item import EventSchemaTargetsItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[EventSchemaSourcesItemType0] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:

                def _parse_sources_item(data: object) -> EventSchemaSourcesItemType0:
                    if not isinstance(data, dict):
                        raise TypeError()
                    sources_item_type_0 = EventSchemaSourcesItemType0.from_dict(data)

                    return sources_item_type_0

                sources_item = _parse_sources_item(sources_item_data)

                sources.append(sources_item)

        def _parse_subscription(data: object) -> EventSchemaSubscriptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_type_0 = EventSchemaSubscriptionType0.from_dict(data)

                return subscription_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventSchemaSubscriptionType0 | None | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        _targets = d.pop("targets", UNSET)
        targets: list[EventSchemaTargetsItem] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = EventSchemaTargetsItem.from_dict(targets_item_data)

                targets.append(targets_item)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        type_ = d.pop("type", UNSET)

        event_schema = cls(
            id=id,
            message=message,
            sources=sources,
            subscription=subscription,
            targets=targets,
            time=time,
            type_=type_,
        )

        event_schema.additional_properties = d
        return event_schema

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
