from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_summary_schema_type_0 import UserSummarySchemaType0


T = TypeVar("T", bound="TopicSchemaCommentOfTopicThingsItem")


@_attrs_define
class TopicSchemaCommentOfTopicThingsItem:
    """
    Attributes:
        collect_count (int | Unset):
        comment_count (int | Unset):
        created_at (datetime.datetime | Unset):
        creator (None | Unset | UserSummarySchemaType0):
        id (int | Unset):
        is_nsfw (bool | Unset):
        is_private (bool | Unset):
        is_published (bool | Unset):
        is_purchased (bool | Unset):
        name (str | Unset):
        public_url (str | Unset):
        thumbnail (str | Unset):
        url (str | Unset):
    """

    collect_count: int | Unset = UNSET
    comment_count: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    creator: None | Unset | UserSummarySchemaType0 = UNSET
    id: int | Unset = UNSET
    is_nsfw: bool | Unset = UNSET
    is_private: bool | Unset = UNSET
    is_published: bool | Unset = UNSET
    is_purchased: bool | Unset = UNSET
    name: str | Unset = UNSET
    public_url: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        collect_count = self.collect_count

        comment_count = self.comment_count

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, UserSummarySchemaType0):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        id = self.id

        is_nsfw = self.is_nsfw

        is_private = self.is_private

        is_published = self.is_published

        is_purchased = self.is_purchased

        name = self.name

        public_url = self.public_url

        thumbnail = self.thumbnail

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collect_count is not UNSET:
            field_dict["collect_count"] = collect_count
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if creator is not UNSET:
            field_dict["creator"] = creator
        if id is not UNSET:
            field_dict["id"] = id
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if is_purchased is not UNSET:
            field_dict["is_purchased"] = is_purchased
        if name is not UNSET:
            field_dict["name"] = name
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        d = dict(src_dict)
        collect_count = d.pop("collect_count", UNSET)

        comment_count = d.pop("comment_count", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_creator(data: object) -> None | Unset | UserSummarySchemaType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasuser_summary_schema_type_0 = UserSummarySchemaType0.from_dict(data)

                return componentsschemasuser_summary_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserSummarySchemaType0, data)

        creator = _parse_creator(d.pop("creator", UNSET))

        id = d.pop("id", UNSET)

        is_nsfw = d.pop("is_nsfw", UNSET)

        is_private = d.pop("is_private", UNSET)

        is_published = d.pop("is_published", UNSET)

        is_purchased = d.pop("is_purchased", UNSET)

        name = d.pop("name", UNSET)

        public_url = d.pop("public_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        url = d.pop("url", UNSET)

        topic_schema_comment_of_topic_things_item = cls(
            collect_count=collect_count,
            comment_count=comment_count,
            created_at=created_at,
            creator=creator,
            id=id,
            is_nsfw=is_nsfw,
            is_private=is_private,
            is_published=is_published,
            is_purchased=is_purchased,
            name=name,
            public_url=public_url,
            thumbnail=thumbnail,
            url=url,
        )

        topic_schema_comment_of_topic_things_item.additional_properties = d
        return topic_schema_comment_of_topic_things_item

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
