from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSummaryType0")


@_attrs_define
class UserSummaryType0:
    """
    Attributes:
        accepts_tips (bool | Unset):
        count_of_designs (int | Unset):  Example: 147.
        count_of_followers (int | Unset):  Example: 9828.
        count_of_following (int | Unset):  Example: 975.
        cover (str | Unset):  Example:
            https://cdn.thingiverse.com/renders/6d/54/65/5c/9b/Thingiverse_background_3_preview_large.jpg.
        first_name (str | Unset):  Example: Creative.
        id (int | Unset):  Example: 1336.
        is_admin (bool | Unset):
        is_featured (bool | Unset):
        is_following (bool | Unset):  Example: True.
        is_moderator (bool | Unset):
        is_verified (bool | Unset):
        last_name (str | Unset):  Example: Tools.
        location (str | Unset):  Example: Halmstad, Sweden.
        make_count (int | Unset):
        name (str | Unset):  Example: CreativeTools.
        public_url (str | Unset):  Example: https://www.thingiverse.com/CreativeTools.
        thumbnail (str | Unset):  Example: https://cdn.thingiverse.com/renders/b3/a5/0c/45/3f/CT_thumb_medium.jpg.
        url (str | Unset):  Example: https://api.thingiverse.com/users/CreativeTools.
    """

    accepts_tips: bool | Unset = UNSET
    count_of_designs: int | Unset = UNSET
    count_of_followers: int | Unset = UNSET
    count_of_following: int | Unset = UNSET
    cover: str | Unset = UNSET
    first_name: str | Unset = UNSET
    id: int | Unset = UNSET
    is_admin: bool | Unset = UNSET
    is_featured: bool | Unset = UNSET
    is_following: bool | Unset = UNSET
    is_moderator: bool | Unset = UNSET
    is_verified: bool | Unset = UNSET
    last_name: str | Unset = UNSET
    location: str | Unset = UNSET
    make_count: int | Unset = UNSET
    name: str | Unset = UNSET
    public_url: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepts_tips = self.accepts_tips

        count_of_designs = self.count_of_designs

        count_of_followers = self.count_of_followers

        count_of_following = self.count_of_following

        cover = self.cover

        first_name = self.first_name

        id = self.id

        is_admin = self.is_admin

        is_featured = self.is_featured

        is_following = self.is_following

        is_moderator = self.is_moderator

        is_verified = self.is_verified

        last_name = self.last_name

        location = self.location

        make_count = self.make_count

        name = self.name

        public_url = self.public_url

        thumbnail = self.thumbnail

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepts_tips is not UNSET:
            field_dict["accepts_tips"] = accepts_tips
        if count_of_designs is not UNSET:
            field_dict["count_of_designs"] = count_of_designs
        if count_of_followers is not UNSET:
            field_dict["count_of_followers"] = count_of_followers
        if count_of_following is not UNSET:
            field_dict["count_of_following"] = count_of_following
        if cover is not UNSET:
            field_dict["cover"] = cover
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if is_featured is not UNSET:
            field_dict["is_featured"] = is_featured
        if is_following is not UNSET:
            field_dict["is_following"] = is_following
        if is_moderator is not UNSET:
            field_dict["is_moderator"] = is_moderator
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if location is not UNSET:
            field_dict["location"] = location
        if make_count is not UNSET:
            field_dict["make_count"] = make_count
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
        d = dict(src_dict)
        accepts_tips = d.pop("accepts_tips", UNSET)

        count_of_designs = d.pop("count_of_designs", UNSET)

        count_of_followers = d.pop("count_of_followers", UNSET)

        count_of_following = d.pop("count_of_following", UNSET)

        cover = d.pop("cover", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        is_admin = d.pop("is_admin", UNSET)

        is_featured = d.pop("is_featured", UNSET)

        is_following = d.pop("is_following", UNSET)

        is_moderator = d.pop("is_moderator", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        last_name = d.pop("last_name", UNSET)

        location = d.pop("location", UNSET)

        make_count = d.pop("make_count", UNSET)

        name = d.pop("name", UNSET)

        public_url = d.pop("public_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        url = d.pop("url", UNSET)

        user_summary_type_0 = cls(
            accepts_tips=accepts_tips,
            count_of_designs=count_of_designs,
            count_of_followers=count_of_followers,
            count_of_following=count_of_following,
            cover=cover,
            first_name=first_name,
            id=id,
            is_admin=is_admin,
            is_featured=is_featured,
            is_following=is_following,
            is_moderator=is_moderator,
            is_verified=is_verified,
            last_name=last_name,
            location=location,
            make_count=make_count,
            name=name,
            public_url=public_url,
            thumbnail=thumbnail,
            url=url,
        )

        user_summary_type_0.additional_properties = d
        return user_summary_type_0

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
