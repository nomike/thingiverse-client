from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_schema_comment_of_topic_attachments_item import (
        TopicSchemaCommentOfTopicAttachmentsItem,
    )
    from ..models.topic_schema_comment_of_topic_things_item import (
        TopicSchemaCommentOfTopicThingsItem,
    )
    from ..models.user_summary_schema_type_0 import UserSummarySchemaType0


T = TypeVar("T", bound="TopicSchemaCommentOfTopic")


@_attrs_define
class TopicSchemaCommentOfTopic:
    """
    Attributes:
        added (datetime.datetime | Unset):
        attachments (list[TopicSchemaCommentOfTopicAttachmentsItem] | Unset):
        body (str | Unset):
        body_html (str | Unset):
        has_children (bool | Unset):
        id (int | Unset):
        is_deleted (bool | Unset):
        is_root_comment (bool | Unset):
        modified (datetime.datetime | str | Unset):
        needs_moderation (bool | Unset):
        parent_id (int | Unset):
        parent_url (str | Unset):
        public_url (str | Unset):
        target_id (int | Unset):
        target_type (str | Unset):
        target_url (str | Unset):
        things (list[TopicSchemaCommentOfTopicThingsItem] | Unset):
        topic_name (str | Unset):
        url (str | Unset):
        user (None | Unset | UserSummarySchemaType0):
    """

    added: datetime.datetime | Unset = UNSET
    attachments: list[TopicSchemaCommentOfTopicAttachmentsItem] | Unset = UNSET
    body: str | Unset = UNSET
    body_html: str | Unset = UNSET
    has_children: bool | Unset = UNSET
    id: int | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    is_root_comment: bool | Unset = UNSET
    modified: datetime.datetime | str | Unset = UNSET
    needs_moderation: bool | Unset = UNSET
    parent_id: int | Unset = UNSET
    parent_url: str | Unset = UNSET
    public_url: str | Unset = UNSET
    target_id: int | Unset = UNSET
    target_type: str | Unset = UNSET
    target_url: str | Unset = UNSET
    things: list[TopicSchemaCommentOfTopicThingsItem] | Unset = UNSET
    topic_name: str | Unset = UNSET
    url: str | Unset = UNSET
    user: None | Unset | UserSummarySchemaType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        added: str | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        body = self.body

        body_html = self.body_html

        has_children = self.has_children

        id = self.id

        is_deleted = self.is_deleted

        is_root_comment = self.is_root_comment

        modified: str | Unset
        if isinstance(self.modified, Unset):
            modified = UNSET
        elif isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        needs_moderation = self.needs_moderation

        parent_id = self.parent_id

        parent_url = self.parent_url

        public_url = self.public_url

        target_id = self.target_id

        target_type = self.target_type

        target_url = self.target_url

        things: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.things, Unset):
            things = []
            for things_item_data in self.things:
                things_item = things_item_data.to_dict()
                things.append(things_item)

        topic_name = self.topic_name

        url = self.url

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UserSummarySchemaType0):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if body is not UNSET:
            field_dict["body"] = body
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if has_children is not UNSET:
            field_dict["has_children"] = has_children
        if id is not UNSET:
            field_dict["id"] = id
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if is_root_comment is not UNSET:
            field_dict["is_root_comment"] = is_root_comment
        if modified is not UNSET:
            field_dict["modified"] = modified
        if needs_moderation is not UNSET:
            field_dict["needs_moderation"] = needs_moderation
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if parent_url is not UNSET:
            field_dict["parent_url"] = parent_url
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if things is not UNSET:
            field_dict["things"] = things
        if topic_name is not UNSET:
            field_dict["topic_name"] = topic_name
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.topic_schema_comment_of_topic_attachments_item import (
            TopicSchemaCommentOfTopicAttachmentsItem,
        )
        from ..models.topic_schema_comment_of_topic_things_item import (
            TopicSchemaCommentOfTopicThingsItem,
        )
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        d = dict(src_dict)
        _added = d.pop("added", UNSET)
        added: datetime.datetime | Unset
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[TopicSchemaCommentOfTopicAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = TopicSchemaCommentOfTopicAttachmentsItem.from_dict(
                    attachments_item_data
                )

                attachments.append(attachments_item)

        body = d.pop("body", UNSET)

        body_html = d.pop("body_html", UNSET)

        has_children = d.pop("has_children", UNSET)

        id = d.pop("id", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        is_root_comment = d.pop("is_root_comment", UNSET)

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

        needs_moderation = d.pop("needs_moderation", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        parent_url = d.pop("parent_url", UNSET)

        public_url = d.pop("public_url", UNSET)

        target_id = d.pop("target_id", UNSET)

        target_type = d.pop("target_type", UNSET)

        target_url = d.pop("target_url", UNSET)

        _things = d.pop("things", UNSET)
        things: list[TopicSchemaCommentOfTopicThingsItem] | Unset = UNSET
        if _things is not UNSET:
            things = []
            for things_item_data in _things:
                things_item = TopicSchemaCommentOfTopicThingsItem.from_dict(things_item_data)

                things.append(things_item)

        topic_name = d.pop("topic_name", UNSET)

        url = d.pop("url", UNSET)

        def _parse_user(data: object) -> None | Unset | UserSummarySchemaType0:
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

        user = _parse_user(d.pop("user", UNSET))

        topic_schema_comment_of_topic = cls(
            added=added,
            attachments=attachments,
            body=body,
            body_html=body_html,
            has_children=has_children,
            id=id,
            is_deleted=is_deleted,
            is_root_comment=is_root_comment,
            modified=modified,
            needs_moderation=needs_moderation,
            parent_id=parent_id,
            parent_url=parent_url,
            public_url=public_url,
            target_id=target_id,
            target_type=target_type,
            target_url=target_url,
            things=things,
            topic_name=topic_name,
            url=url,
            user=user,
        )

        topic_schema_comment_of_topic.additional_properties = d
        return topic_schema_comment_of_topic

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
