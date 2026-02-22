from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_schema import CommentSchema
    from ..models.group_topic_comments import GroupTopicComments
    from ..models.group_topic_tags import GroupTopicTags
    from ..models.member_schema import MemberSchema


T = TypeVar("T", bound="GroupTopic")


@_attrs_define
class GroupTopic:
    """
    Attributes:
        id (int):
        added (datetime.datetime | Unset):
        can_comment (bool | Unset):
        comment_of_topic (CommentSchema | Unset):
        comments (GroupTopicComments | Unset):
        group_url (str | Unset):
        modified (datetime.datetime | str | Unset):
        name (str | Unset):
        pinned (int | Unset):
        public_url (str | Unset):
        root_comment_count (int | Unset):
        tags (GroupTopicTags | Unset):
        type_name (str | Unset):
        url (str | Unset):
        user (MemberSchema | Unset):
        watched (bool | Unset):
    """

    id: int
    added: datetime.datetime | Unset = UNSET
    can_comment: bool | Unset = UNSET
    comment_of_topic: CommentSchema | Unset = UNSET
    comments: GroupTopicComments | Unset = UNSET
    group_url: str | Unset = UNSET
    modified: datetime.datetime | str | Unset = UNSET
    name: str | Unset = UNSET
    pinned: int | Unset = UNSET
    public_url: str | Unset = UNSET
    root_comment_count: int | Unset = UNSET
    tags: GroupTopicTags | Unset = UNSET
    type_name: str | Unset = UNSET
    url: str | Unset = UNSET
    user: MemberSchema | Unset = UNSET
    watched: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        added: str | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        can_comment = self.can_comment

        comment_of_topic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment_of_topic, Unset):
            comment_of_topic = self.comment_of_topic.to_dict()

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        group_url = self.group_url

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

        root_comment_count = self.root_comment_count

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        type_name = self.type_name

        url = self.url

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        watched = self.watched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if added is not UNSET:
            field_dict["added"] = added
        if can_comment is not UNSET:
            field_dict["can_comment"] = can_comment
        if comment_of_topic is not UNSET:
            field_dict["comment_of_topic"] = comment_of_topic
        if comments is not UNSET:
            field_dict["comments"] = comments
        if group_url is not UNSET:
            field_dict["group_url"] = group_url
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if root_comment_count is not UNSET:
            field_dict["root_comment_count"] = root_comment_count
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_name is not UNSET:
            field_dict["type_name"] = type_name
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user
        if watched is not UNSET:
            field_dict["watched"] = watched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_schema import CommentSchema
        from ..models.group_topic_comments import GroupTopicComments
        from ..models.group_topic_tags import GroupTopicTags
        from ..models.member_schema import MemberSchema

        d = dict(src_dict)
        id = d.pop("id")

        _added = d.pop("added", UNSET)
        added: datetime.datetime | Unset
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        can_comment = d.pop("can_comment", UNSET)

        _comment_of_topic = d.pop("comment_of_topic", UNSET)
        comment_of_topic: CommentSchema | Unset
        if isinstance(_comment_of_topic, Unset):
            comment_of_topic = UNSET
        else:
            comment_of_topic = CommentSchema.from_dict(_comment_of_topic)

        _comments = d.pop("comments", UNSET)
        comments: GroupTopicComments | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = GroupTopicComments.from_dict(_comments)

        group_url = d.pop("group_url", UNSET)

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

        root_comment_count = d.pop("root_comment_count", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: GroupTopicTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = GroupTopicTags.from_dict(_tags)

        type_name = d.pop("type_name", UNSET)

        url = d.pop("url", UNSET)

        _user = d.pop("user", UNSET)
        user: MemberSchema | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = MemberSchema.from_dict(_user)

        watched = d.pop("watched", UNSET)

        group_topic = cls(
            id=id,
            added=added,
            can_comment=can_comment,
            comment_of_topic=comment_of_topic,
            comments=comments,
            group_url=group_url,
            modified=modified,
            name=name,
            pinned=pinned,
            public_url=public_url,
            root_comment_count=root_comment_count,
            tags=tags,
            type_name=type_name,
            url=url,
            user=user,
            watched=watched,
        )

        group_topic.additional_properties = d
        return group_topic

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
