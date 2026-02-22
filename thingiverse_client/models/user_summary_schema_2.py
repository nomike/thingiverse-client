from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSummarySchema2")


@_attrs_define
class UserSummarySchema2:
    """
    Attributes:
        accepts_tips (bool | Unset):
        collection_count (int | Unset):
        count_of_designs (int | Unset):
        count_of_followers (int | Unset):
        count_of_following (int | Unset):
        cover (str | Unset):
        first_name (str | Unset):
        id (int | Unset):
        is_admin (bool | Unset):
        is_following (bool | Unset):
        last_name (str | Unset):
        location (str | Unset):
        make_count (int | Unset):
        name (str | Unset):
        public_url (str | Unset):
        thumbnail (str | Unset):
        url (str | Unset):
    """

    accepts_tips: bool | Unset = UNSET
    collection_count: int | Unset = UNSET
    count_of_designs: int | Unset = UNSET
    count_of_followers: int | Unset = UNSET
    count_of_following: int | Unset = UNSET
    cover: str | Unset = UNSET
    first_name: str | Unset = UNSET
    id: int | Unset = UNSET
    is_admin: bool | Unset = UNSET
    is_following: bool | Unset = UNSET
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

        collection_count = self.collection_count

        count_of_designs = self.count_of_designs

        count_of_followers = self.count_of_followers

        count_of_following = self.count_of_following

        cover = self.cover

        first_name = self.first_name

        id = self.id

        is_admin = self.is_admin

        is_following = self.is_following

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
        if collection_count is not UNSET:
            field_dict["collection_count"] = collection_count
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
        if is_following is not UNSET:
            field_dict["is_following"] = is_following
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

        collection_count = d.pop("collection_count", UNSET)

        count_of_designs = d.pop("count_of_designs", UNSET)

        count_of_followers = d.pop("count_of_followers", UNSET)

        count_of_following = d.pop("count_of_following", UNSET)

        cover = d.pop("cover", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        is_admin = d.pop("is_admin", UNSET)

        is_following = d.pop("is_following", UNSET)

        last_name = d.pop("last_name", UNSET)

        location = d.pop("location", UNSET)

        make_count = d.pop("make_count", UNSET)

        name = d.pop("name", UNSET)

        public_url = d.pop("public_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        url = d.pop("url", UNSET)

        user_summary_schema_2 = cls(
            accepts_tips=accepts_tips,
            collection_count=collection_count,
            count_of_designs=count_of_designs,
            count_of_followers=count_of_followers,
            count_of_following=count_of_following,
            cover=cover,
            first_name=first_name,
            id=id,
            is_admin=is_admin,
            is_following=is_following,
            last_name=last_name,
            location=location,
            make_count=make_count,
            name=name,
            public_url=public_url,
            thumbnail=thumbnail,
            url=url,
        )

        user_summary_schema_2.additional_properties = d
        return user_summary_schema_2

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
