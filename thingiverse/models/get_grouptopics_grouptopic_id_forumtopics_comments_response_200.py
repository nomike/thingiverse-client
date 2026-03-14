from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_schema import CommentSchema
    from ..models.grouptopic_schema import GrouptopicSchema


T = TypeVar("T", bound="GetGrouptopicsGrouptopicIdForumtopicsCommentsResponse200")


@_attrs_define
class GetGrouptopicsGrouptopicIdForumtopicsCommentsResponse200:
    """
    Attributes:
        topics_comments (list[CommentSchema | GrouptopicSchema] | Unset):
        total (int | Unset):
    """

    topics_comments: list[CommentSchema | GrouptopicSchema] | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.grouptopic_schema import GrouptopicSchema

        topics_comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topics_comments, Unset):
            topics_comments = []
            for topics_comments_item_data in self.topics_comments:
                topics_comments_item: dict[str, Any]
                if isinstance(topics_comments_item_data, GrouptopicSchema):
                    topics_comments_item = topics_comments_item_data.to_dict()
                else:
                    topics_comments_item = topics_comments_item_data.to_dict()

                topics_comments.append(topics_comments_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topics_comments is not UNSET:
            field_dict["topics_comments"] = topics_comments
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_schema import CommentSchema
        from ..models.grouptopic_schema import GrouptopicSchema

        d = dict(src_dict)
        _topics_comments = d.pop("topics_comments", UNSET)
        topics_comments: list[CommentSchema | GrouptopicSchema] | Unset = UNSET
        if _topics_comments is not UNSET:
            topics_comments = []
            for topics_comments_item_data in _topics_comments:

                def _parse_topics_comments_item(data: object) -> CommentSchema | GrouptopicSchema:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        topics_comments_item_type_0 = GrouptopicSchema.from_dict(data)

                        return topics_comments_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    topics_comments_item_type_1 = CommentSchema.from_dict(data)

                    return topics_comments_item_type_1

                topics_comments_item = _parse_topics_comments_item(topics_comments_item_data)

                topics_comments.append(topics_comments_item)

        total = d.pop("total", UNSET)

        get_grouptopics_grouptopic_id_forumtopics_comments_response_200 = cls(
            topics_comments=topics_comments,
            total=total,
        )

        get_grouptopics_grouptopic_id_forumtopics_comments_response_200.additional_properties = d
        return get_grouptopics_grouptopic_id_forumtopics_comments_response_200

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
