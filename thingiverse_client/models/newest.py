from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_schema import TagSchema
    from ..models.user_summary_schema_type_0 import UserSummarySchemaType0


T = TypeVar("T", bound="Newest")


@_attrs_define
class Newest:
    """
    Attributes:
        collect_count (int | Unset):
        comment_count (int | Unset):
        created_at (datetime.datetime | Unset):
        creator (None | Unset | UserSummarySchemaType0):
        id (int | Unset):
        is_nsfw (bool | None | Unset):
        is_private (int | Unset):
        is_published (int | Unset):
        is_purchased (int | Unset):
        like_count (int | Unset):
        make_count (int | Unset):
        name (str | Unset):
        preview_image (str | Unset):
        public_url (str | Unset):
        rank (int | None | Unset):
        tags (list[TagSchema] | Unset):
        thumbnail (str | Unset):
        url (str | Unset):
    """

    collect_count: int | Unset = UNSET
    comment_count: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    creator: None | Unset | UserSummarySchemaType0 = UNSET
    id: int | Unset = UNSET
    is_nsfw: bool | None | Unset = UNSET
    is_private: int | Unset = UNSET
    is_published: int | Unset = UNSET
    is_purchased: int | Unset = UNSET
    like_count: int | Unset = UNSET
    make_count: int | Unset = UNSET
    name: str | Unset = UNSET
    preview_image: str | Unset = UNSET
    public_url: str | Unset = UNSET
    rank: int | None | Unset = UNSET
    tags: list[TagSchema] | Unset = UNSET
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

        is_nsfw: bool | None | Unset
        if isinstance(self.is_nsfw, Unset):
            is_nsfw = UNSET
        else:
            is_nsfw = self.is_nsfw

        is_private = self.is_private

        is_published = self.is_published

        is_purchased = self.is_purchased

        like_count = self.like_count

        make_count = self.make_count

        name = self.name

        preview_image = self.preview_image

        public_url = self.public_url

        rank: int | None | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

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
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if make_count is not UNSET:
            field_dict["make_count"] = make_count
        if name is not UNSET:
            field_dict["name"] = name
        if preview_image is not UNSET:
            field_dict["preview_image"] = preview_image
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if rank is not UNSET:
            field_dict["rank"] = rank
        if tags is not UNSET:
            field_dict["tags"] = tags
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_schema import TagSchema
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

        def _parse_is_nsfw(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw", UNSET))

        is_private = d.pop("is_private", UNSET)

        is_published = d.pop("is_published", UNSET)

        is_purchased = d.pop("is_purchased", UNSET)

        like_count = d.pop("like_count", UNSET)

        make_count = d.pop("make_count", UNSET)

        name = d.pop("name", UNSET)

        preview_image = d.pop("preview_image", UNSET)

        public_url = d.pop("public_url", UNSET)

        def _parse_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[TagSchema] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = TagSchema.from_dict(tags_item_data)

                tags.append(tags_item)

        thumbnail = d.pop("thumbnail", UNSET)

        url = d.pop("url", UNSET)

        newest = cls(
            collect_count=collect_count,
            comment_count=comment_count,
            created_at=created_at,
            creator=creator,
            id=id,
            is_nsfw=is_nsfw,
            is_private=is_private,
            is_published=is_published,
            is_purchased=is_purchased,
            like_count=like_count,
            make_count=make_count,
            name=name,
            preview_image=preview_image,
            public_url=public_url,
            rank=rank,
            tags=tags,
            thumbnail=thumbnail,
            url=url,
        )

        newest.additional_properties = d
        return newest

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
