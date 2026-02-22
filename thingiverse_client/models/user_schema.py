from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_schema_groups_item import UserSchemaGroupsItem
    from ..models.user_schema_printers_item import UserSchemaPrintersItem
    from ..models.user_schema_programs_item import UserSchemaProgramsItem
    from ..models.user_schema_twitter_type_0 import UserSchemaTwitterType0
    from ..models.user_schema_types_item import UserSchemaTypesItem


T = TypeVar("T", bound="UserSchema")


@_attrs_define
class UserSchema:
    r"""
    Attributes:
        name (str):  Example: CreativeTools.
        accepts_tips (bool | Unset):
        bio (str | Unset):  Example: Creative Tools offers a wide range of software and hardware for both beginners and
            professional 2D and 3D creators. We always release [our 3D
            models](http:\/\/www.thingiverse.com\/CreativeTools\/designs) free of charge for anyone to download and use.
            Please [let us know](mailto:thingiverse@creativetools.se) if you have comments on our files or want to suggest
            future project ideas. Your feedback is highly appreciated!\r\n\r\n### Do you like our designs?\r\nPlease support
            us by placing your next 3D related order at [www.creativetools.se](https:\/\/www.creativetools.se\/). We offer a
            wide range of 3D software and 3D hardware, and are authorized resellers of well-known brands such as
            [Autodesk](https:\/\/www.creativetools.se\/autodesk), [Adobe](https:\/\/www.creativetools.se\/adobe), [Chaos
            Group](https:\/\/www.creativetools.se\/chaos-group), [Ultimaker](https:\/\/www.creativetools.se\/ultimaker),
            [Flashforge](https:\/\/www.creativetools.se\/flashforge), [MakerBot](https:\/\/www.creativetools.se\/makerbot)
            and [Formlabs](https:\/\/www.creativetools.se\/formlabs).\r\n\r\n\r\nWe would be honoured to serve you as a
            customer at [www.creativetools.se](https:\/\/www.creativetools.se).\r\n\r\n* * *  \r\n######[Online
            store](https:\/\/www.creativetools.se\/) - [Blog](https:\/\/blog.creativetools.se\/) -
            [#3DBenchy](http:\/\/www.3DBenchy.com) - [Twitter](http:\/\/twitter.com\/CreativeTools) -
            [Facebook](http:\/\/facebook.com\/creativetools) - [YouTube](http:\/\/youtube.com\/creativetools) -
            [Instagram](http:\/\/instagram.com\/creative_tools) - [LinkedIn](https:\/\/www.linkedin.com\/company\/creative-
            tools).
        bio_html (str | Unset):  Example: <div><p>Creative Tools offers a wide range of software and hardware for both
            beginners and professional 2D and 3D creators. We always release <a rel=\"ugc nofollow\"
            href=\"\/CreativeTools\/designs\">our 3D models<\/a> free of charge for anyone to download and use. Please <a
            href=\"mailto:thingiverse%20at%20creativetools.se\">let us know<\/a> if you have comments on our files or want
            to suggest future project ideas. Your feedback is highly appreciated!<\/p><h3>Do you like our
            designs?<\/h3><p>Please support us by placing your next 3D related order at <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/\">www.creativetools.se<\/a>. We offer a wide range of 3D software and 3D
            hardware, and are authorized resellers of well-known brands such as <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/autodesk\">Autodesk<\/a>, <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/adobe\">Adobe<\/a>, <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/chaos-group\">Chaos Group<\/a>, <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/ultimaker\">Ultimaker<\/a>, <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/flashforge\">Flashforge<\/a>, <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/makerbot\">MakerBot<\/a> and <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/formlabs\">Formlabs<\/a>.<\/p><p>We would be honoured to serve you as a
            customer at <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\">www.creativetools.se<\/a>.<\/p><hr><h6><a rel=\"ugc nofollow\"
            href=\"https:\/\/www.creativetools.se\/\">Online store<\/a> - <a rel=\"ugc nofollow\"
            href=\"https:\/\/blog.creativetools.se\/\">Blog<\/a> -  <a rel=\"ugc nofollow\"
            href=\"http:\/\/www.3DBenchy.com\">#3DBenchy<\/a> - <a rel=\"ugc nofollow\"
            href=\"http:\/\/twitter.com\/CreativeTools\">Twitter<\/a> - <a rel=\"ugc nofollow\"
            href=\"http:\/\/facebook.com\/creativetools\">Facebook<\/a> - <a rel=\"ugc nofollow\"
            href=\"http:\/\/youtube.com\/creativetools\">YouTube<\/a> - <a rel=\"ugc nofollow\"
            href=\"http:\/\/instagram.com\/creative_tools\">Instagram<\/a> - <a rel=\"ugc nofollow\"
            href=\"https:\/\/www.linkedin.com\/company\/creative-tools\">LinkedIn<\/a><\/h6><\/div>\n.
        collection_count (int | Unset):  Example: 16.
        copies_url (str | Unset):  Example: https://api.thingiverse.com/users/CreativeTools/copies.
        count_of_designs (int | Unset):  Example: 147.
        count_of_followers (int | Unset):  Example: 9828.
        count_of_following (int | Unset):  Example: 975.
        country (None | str | Unset):
        cover_image (str | Unset):  Example:
            https://cdn.thingiverse.com/renders/6d/54/65/5c/9b/Thingiverse_background_3_preview_birdwing.jpg.
        email (str | Unset):  Example: thingiverse@creativetools.se.
        favorite_count (int | Unset):  Example: 6.
        first_name (str | Unset):  Example: Creative.
        groups (list[UserSchemaGroupsItem] | Unset):
        has_favorite (bool | Unset):  Example: True.
        id (int | Unset):  Example: 1336.
        is_admin (bool | Unset):
        is_featured (bool | Unset):
        is_following (bool | Unset):  Example: True.
        is_moderator (bool | Unset):
        is_verified (bool | Unset):
        last_active (datetime.datetime | Unset):  Example: 2023-08-01T13:53:53+00:00.
        last_name (str | Unset):  Example: Tools.
        level (int | Unset): Is the user an admin or moderator? This will return 10 if user is a normal user Example:
            10.
        like_count (int | Unset):
        likes_url (str | Unset):  Example: https://api.thingiverse.com/users/CreativeTools/likes.
        location (str | Unset):  Example: Halmstad, Sweden.
        make_count (int | Unset):
        printers (list[UserSchemaPrintersItem] | Unset):
        programs (list[UserSchemaProgramsItem] | Unset):
        public_url (str | Unset):  Example: https://www.thingiverse.com/CreativeTools.
        registered (datetime.datetime | Unset):  Example: 2009-11-10T10:49:44+00:00.
        skill_level (str | Unset):  Example: Advanced.
        things_url (str | Unset):  Example: https://api.thingiverse.com/users/CreativeTools/things.
        thumbnail (str | Unset):  Example: https://cdn.thingiverse.com/renders/b3/a5/0c/45/3f/CT_thumb_medium.jpg.
        twitter (None | Unset | UserSchemaTwitterType0):
        types (list[UserSchemaTypesItem] | Unset):
        url (str | Unset):  Example: https://api.thingiverse.com/users/CreativeTools.
        website (str | Unset):  Example: http://CreativeTools.se.
    """

    name: str
    accepts_tips: bool | Unset = UNSET
    bio: str | Unset = UNSET
    bio_html: str | Unset = UNSET
    collection_count: int | Unset = UNSET
    copies_url: str | Unset = UNSET
    count_of_designs: int | Unset = UNSET
    count_of_followers: int | Unset = UNSET
    count_of_following: int | Unset = UNSET
    country: None | str | Unset = UNSET
    cover_image: str | Unset = UNSET
    email: str | Unset = UNSET
    favorite_count: int | Unset = UNSET
    first_name: str | Unset = UNSET
    groups: list[UserSchemaGroupsItem] | Unset = UNSET
    has_favorite: bool | Unset = UNSET
    id: int | Unset = UNSET
    is_admin: bool | Unset = UNSET
    is_featured: bool | Unset = UNSET
    is_following: bool | Unset = UNSET
    is_moderator: bool | Unset = UNSET
    is_verified: bool | Unset = UNSET
    last_active: datetime.datetime | Unset = UNSET
    last_name: str | Unset = UNSET
    level: int | Unset = UNSET
    like_count: int | Unset = UNSET
    likes_url: str | Unset = UNSET
    location: str | Unset = UNSET
    make_count: int | Unset = UNSET
    printers: list[UserSchemaPrintersItem] | Unset = UNSET
    programs: list[UserSchemaProgramsItem] | Unset = UNSET
    public_url: str | Unset = UNSET
    registered: datetime.datetime | Unset = UNSET
    skill_level: str | Unset = UNSET
    things_url: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    twitter: None | Unset | UserSchemaTwitterType0 = UNSET
    types: list[UserSchemaTypesItem] | Unset = UNSET
    url: str | Unset = UNSET
    website: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_schema_twitter_type_0 import UserSchemaTwitterType0

        name = self.name

        accepts_tips = self.accepts_tips

        bio = self.bio

        bio_html = self.bio_html

        collection_count = self.collection_count

        copies_url = self.copies_url

        count_of_designs = self.count_of_designs

        count_of_followers = self.count_of_followers

        count_of_following = self.count_of_following

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        cover_image = self.cover_image

        email = self.email

        favorite_count = self.favorite_count

        first_name = self.first_name

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        has_favorite = self.has_favorite

        id = self.id

        is_admin = self.is_admin

        is_featured = self.is_featured

        is_following = self.is_following

        is_moderator = self.is_moderator

        is_verified = self.is_verified

        last_active: str | Unset = UNSET
        if not isinstance(self.last_active, Unset):
            last_active = self.last_active.isoformat()

        last_name = self.last_name

        level = self.level

        like_count = self.like_count

        likes_url = self.likes_url

        location = self.location

        make_count = self.make_count

        printers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.printers, Unset):
            printers = []
            for printers_item_data in self.printers:
                printers_item = printers_item_data.to_dict()
                printers.append(printers_item)

        programs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.programs, Unset):
            programs = []
            for programs_item_data in self.programs:
                programs_item = programs_item_data.to_dict()
                programs.append(programs_item)

        public_url = self.public_url

        registered: str | Unset = UNSET
        if not isinstance(self.registered, Unset):
            registered = self.registered.isoformat()

        skill_level = self.skill_level

        things_url = self.things_url

        thumbnail = self.thumbnail

        twitter: dict[str, Any] | None | Unset
        if isinstance(self.twitter, Unset):
            twitter = UNSET
        elif isinstance(self.twitter, UserSchemaTwitterType0):
            twitter = self.twitter.to_dict()
        else:
            twitter = self.twitter

        types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.to_dict()
                types.append(types_item)

        url = self.url

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if accepts_tips is not UNSET:
            field_dict["accepts_tips"] = accepts_tips
        if bio is not UNSET:
            field_dict["bio"] = bio
        if bio_html is not UNSET:
            field_dict["bio_html"] = bio_html
        if collection_count is not UNSET:
            field_dict["collection_count"] = collection_count
        if copies_url is not UNSET:
            field_dict["copies_url"] = copies_url
        if count_of_designs is not UNSET:
            field_dict["count_of_designs"] = count_of_designs
        if count_of_followers is not UNSET:
            field_dict["count_of_followers"] = count_of_followers
        if count_of_following is not UNSET:
            field_dict["count_of_following"] = count_of_following
        if country is not UNSET:
            field_dict["country"] = country
        if cover_image is not UNSET:
            field_dict["cover_image"] = cover_image
        if email is not UNSET:
            field_dict["email"] = email
        if favorite_count is not UNSET:
            field_dict["favorite_count"] = favorite_count
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if has_favorite is not UNSET:
            field_dict["has_favorite"] = has_favorite
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
        if last_active is not UNSET:
            field_dict["last_active"] = last_active
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if level is not UNSET:
            field_dict["level"] = level
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if likes_url is not UNSET:
            field_dict["likes_url"] = likes_url
        if location is not UNSET:
            field_dict["location"] = location
        if make_count is not UNSET:
            field_dict["make_count"] = make_count
        if printers is not UNSET:
            field_dict["printers"] = printers
        if programs is not UNSET:
            field_dict["programs"] = programs
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if registered is not UNSET:
            field_dict["registered"] = registered
        if skill_level is not UNSET:
            field_dict["skill_level"] = skill_level
        if things_url is not UNSET:
            field_dict["things_url"] = things_url
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if types is not UNSET:
            field_dict["types"] = types
        if url is not UNSET:
            field_dict["url"] = url
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_schema_groups_item import UserSchemaGroupsItem
        from ..models.user_schema_printers_item import UserSchemaPrintersItem
        from ..models.user_schema_programs_item import UserSchemaProgramsItem
        from ..models.user_schema_twitter_type_0 import UserSchemaTwitterType0
        from ..models.user_schema_types_item import UserSchemaTypesItem

        d = dict(src_dict)
        name = d.pop("name")

        accepts_tips = d.pop("accepts_tips", UNSET)

        bio = d.pop("bio", UNSET)

        bio_html = d.pop("bio_html", UNSET)

        collection_count = d.pop("collection_count", UNSET)

        copies_url = d.pop("copies_url", UNSET)

        count_of_designs = d.pop("count_of_designs", UNSET)

        count_of_followers = d.pop("count_of_followers", UNSET)

        count_of_following = d.pop("count_of_following", UNSET)

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        cover_image = d.pop("cover_image", UNSET)

        email = d.pop("email", UNSET)

        favorite_count = d.pop("favorite_count", UNSET)

        first_name = d.pop("first_name", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[UserSchemaGroupsItem] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = UserSchemaGroupsItem.from_dict(groups_item_data)

                groups.append(groups_item)

        has_favorite = d.pop("has_favorite", UNSET)

        id = d.pop("id", UNSET)

        is_admin = d.pop("is_admin", UNSET)

        is_featured = d.pop("is_featured", UNSET)

        is_following = d.pop("is_following", UNSET)

        is_moderator = d.pop("is_moderator", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        _last_active = d.pop("last_active", UNSET)
        last_active: datetime.datetime | Unset
        if isinstance(_last_active, Unset):
            last_active = UNSET
        else:
            last_active = isoparse(_last_active)

        last_name = d.pop("last_name", UNSET)

        level = d.pop("level", UNSET)

        like_count = d.pop("like_count", UNSET)

        likes_url = d.pop("likes_url", UNSET)

        location = d.pop("location", UNSET)

        make_count = d.pop("make_count", UNSET)

        _printers = d.pop("printers", UNSET)
        printers: list[UserSchemaPrintersItem] | Unset = UNSET
        if _printers is not UNSET:
            printers = []
            for printers_item_data in _printers:
                printers_item = UserSchemaPrintersItem.from_dict(printers_item_data)

                printers.append(printers_item)

        _programs = d.pop("programs", UNSET)
        programs: list[UserSchemaProgramsItem] | Unset = UNSET
        if _programs is not UNSET:
            programs = []
            for programs_item_data in _programs:
                programs_item = UserSchemaProgramsItem.from_dict(programs_item_data)

                programs.append(programs_item)

        public_url = d.pop("public_url", UNSET)

        _registered = d.pop("registered", UNSET)
        registered: datetime.datetime | Unset
        if isinstance(_registered, Unset):
            registered = UNSET
        else:
            registered = isoparse(_registered)

        skill_level = d.pop("skill_level", UNSET)

        things_url = d.pop("things_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        def _parse_twitter(data: object) -> None | Unset | UserSchemaTwitterType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                twitter_type_0 = UserSchemaTwitterType0.from_dict(data)

                return twitter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserSchemaTwitterType0, data)

        twitter = _parse_twitter(d.pop("twitter", UNSET))

        _types = d.pop("types", UNSET)
        types: list[UserSchemaTypesItem] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = UserSchemaTypesItem.from_dict(types_item_data)

                types.append(types_item)

        url = d.pop("url", UNSET)

        website = d.pop("website", UNSET)

        user_schema = cls(
            name=name,
            accepts_tips=accepts_tips,
            bio=bio,
            bio_html=bio_html,
            collection_count=collection_count,
            copies_url=copies_url,
            count_of_designs=count_of_designs,
            count_of_followers=count_of_followers,
            count_of_following=count_of_following,
            country=country,
            cover_image=cover_image,
            email=email,
            favorite_count=favorite_count,
            first_name=first_name,
            groups=groups,
            has_favorite=has_favorite,
            id=id,
            is_admin=is_admin,
            is_featured=is_featured,
            is_following=is_following,
            is_moderator=is_moderator,
            is_verified=is_verified,
            last_active=last_active,
            last_name=last_name,
            level=level,
            like_count=like_count,
            likes_url=likes_url,
            location=location,
            make_count=make_count,
            printers=printers,
            programs=programs,
            public_url=public_url,
            registered=registered,
            skill_level=skill_level,
            things_url=things_url,
            thumbnail=thumbnail,
            twitter=twitter,
            types=types,
            url=url,
            website=website,
        )

        user_schema.additional_properties = d
        return user_schema

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
