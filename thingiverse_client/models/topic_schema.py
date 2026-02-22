from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_schema_comment_of_topic import TopicSchemaCommentOfTopic
    from ..models.topic_schema_comments import TopicSchemaComments


T = TypeVar("T", bound="TopicSchema")


@_attrs_define
class TopicSchema:
    """
    Attributes:
        added (datetime.datetime | Unset):
        comment_of_topic (TopicSchemaCommentOfTopic | Unset):
        comments (TopicSchemaComments | Unset):
        group_url (str | Unset):
        id (int | Unset):
        modified (datetime.datetime | str | Unset):
        name (str | Unset):
        pinned (int | Unset):
        public_url (str | Unset):
        tags (list[str] | Unset):
        url (str | Unset):
    """

    added: datetime.datetime | Unset = UNSET
    comment_of_topic: TopicSchemaCommentOfTopic | Unset = UNSET
    comments: TopicSchemaComments | Unset = UNSET
    group_url: str | Unset = UNSET
    id: int | Unset = UNSET
    modified: datetime.datetime | str | Unset = UNSET
    name: str | Unset = UNSET
    pinned: int | Unset = UNSET
    public_url: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added: str | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        comment_of_topic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment_of_topic, Unset):
            comment_of_topic = self.comment_of_topic.to_dict()

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        group_url = self.group_url

        id = self.id

        modified: str | Unset
        if isinstance(self.modified, Unset):
            modified = UNSET
        elif isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        name = self.name

        pinned = self.pinned

        public_url = self.public_url

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if comment_of_topic is not UNSET:
            field_dict["comment_of_topic"] = comment_of_topic
        if comments is not UNSET:
            field_dict["comments"] = comments
        if group_url is not UNSET:
            field_dict["group_url"] = group_url
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if tags is not UNSET:
            field_dict["tags"] = tags
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.topic_schema_comment_of_topic import TopicSchemaCommentOfTopic
        from ..models.topic_schema_comments import TopicSchemaComments

        d = dict(src_dict)
        _added = d.pop("added", UNSET)
        added: datetime.datetime | Unset
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        _comment_of_topic = d.pop("comment_of_topic", UNSET)
        comment_of_topic: TopicSchemaCommentOfTopic | Unset
        if isinstance(_comment_of_topic, Unset):
            comment_of_topic = UNSET
        else:
            comment_of_topic = TopicSchemaCommentOfTopic.from_dict(_comment_of_topic)

        _comments = d.pop("comments", UNSET)
        comments: TopicSchemaComments | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = TopicSchemaComments.from_dict(_comments)

        group_url = d.pop("group_url", UNSET)

        id = d.pop("id", UNSET)

        def _parse_modified(data: object) -> datetime.datetime | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_1 = isoparse(data)

                return modified_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str | Unset, data)

        modified = _parse_modified(d.pop("modified", UNSET))

        name = d.pop("name", UNSET)

        pinned = d.pop("pinned", UNSET)

        public_url = d.pop("public_url", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        url = d.pop("url", UNSET)

        topic_schema = cls(
            added=added,
            comment_of_topic=comment_of_topic,
            comments=comments,
            group_url=group_url,
            id=id,
            modified=modified,
            name=name,
            pinned=pinned,
            public_url=public_url,
            tags=tags,
            url=url,
        )

        topic_schema.additional_properties = d
        return topic_schema

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
