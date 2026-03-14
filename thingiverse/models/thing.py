from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0
    from ..models.tag_schema import TagSchema
    from ..models.thing_ancestors_item import ThingAncestorsItem
    from ..models.thing_details_parts_item import ThingDetailsPartsItem
    from ..models.thing_edu_details_parts_type_0_item import ThingEduDetailsPartsType0Item
    from ..models.thing_education import ThingEducation
    from ..models.thing_zip_data import ThingZipData
    from ..models.user_summary_schema_type_0 import UserSummarySchemaType0


T = TypeVar("T", bound="Thing")


@_attrs_define
class Thing:
    r"""
    Attributes:
        id (int):  Example: 763622.
        name (str):  Example: #3DBenchy - The jolly 3D printing torture-test by CreativeTools.se.
        added (datetime.datetime | Unset):  Example: 2015-04-09T12:57:28+00:00.
        allows_derivatives (bool | Unset):
        ancestors (list[ThingAncestorsItem] | Unset):
        ancestors_url (str | Unset):  Example: https://api.thingiverse.com/things/763622/ancestors.
        app_count (int | Unset):  Example: 3.
        app_id (int | None | Unset):
        can_comment (bool | Unset):  Example: True.
        categories_url (str | Unset):  Example: https://api.thingiverse.com/things/763622/categories.
        collect_count (int | Unset):  Example: 135811.
        comment_count (int | Unset):  Example: 808.
        creator (None | Unset | UserSummarySchemaType0):
        default_image (ImageSummarySchemaType0 | None | Unset):
        derivatives_url (str | Unset):  Example: https://api.thingiverse.com/things/763622/derivatives.
        description (str | Unset):  Example: Creative Tools](https:\/\/www.creativetools.se\/) Creative Tools supplies
            3D printer and 3D scanner products incl filaments, accessories and support and also 3D software for leading CAD,
            modeling, animation, and rendering..
        description_html (str | Unset):  Example: <div><p><a rel=\"ugc nofollow\"
            href=\"https://www.creativetools.se/\">Creative Tools</a> Creative Tools supplies 3D printer and 3D scanner
            products incl filaments, accessories and support and also 3D software for leading CAD, modeling, animation, and
            rendering.</p></div>.
        details (str | Unset):
        details_parts (list[ThingDetailsPartsItem] | Unset):
        download_count (int | Unset):  Example: 3169879.
        edu_details (str | Unset):
        edu_details_parts (list[ThingEduDetailsPartsType0Item] | None | Unset):
        education (ThingEducation | Unset):
        file_count (int | Unset):  Example: 24.
        files_url (str | Unset):  Example: https://api.thingiverse.com/things/763622/files.
        images_url (str | Unset):  Example: https://api.thingiverse.com/things/763622/images.
        instructions (str | Unset):
        instructions_html (str | Unset):  Example: <div><\/div>\n.
        is_ai (bool | None | Unset):
        is_banned (bool | Unset):
        is_collected (bool | Unset):
        is_comments_disabled (bool | Unset):
        is_decoy (int | Unset):
        is_derivative (bool | Unset):
        is_featured (bool | Unset):  Example: True.
        is_liked (bool | Unset):  Example: True.
        is_nsfw (bool | None | Unset):
        is_published (int | Unset):  Example: 1.
        is_purchased (int | Unset):  Example: 1.
        is_watched (bool | Unset):
        is_wip (int | Unset):  Example: 1.
        license_ (str | Unset):  Example: Creative Commons - Attribution - No Derivatives.
        like_count (int | Unset):  Example: 80855.
        likes_url (str | Unset):  Example: https://api.thingiverse.com/things/763622/likes.
        make_count (int | Unset):  Example: 4518.
        moderation (None | str | Unset):
        modified (datetime.datetime | Unset):  Example: 2015-04-09T12:57:28+00:00.
        needs_moderation (int | Unset):
        public_url (str | Unset):  Example: https://wwww.thingiverse.com/thing:763622.
        remix_count (int | Unset):
        root_comment_count (int | Unset):  Example: 535.
        tags (list[TagSchema] | Unset):
        tags_url (str | Unset):
        thumbnail (str | Unset):  Example:
            https://cdn.thingiverse.com/renders/62/ab/d7/e3/ea/1_3D-printed_3DBenchy_by_Creative-
            Tools.com_display_large.JPG.
        type_name (str | Unset):  Example: Thing.
        url (str | Unset):  Example: https://api.thingiverse.com/things/763622.
        view_count (int | Unset):  Example: 4065156.
        zip_data (ThingZipData | Unset):
    """

    id: int
    name: str
    added: datetime.datetime | Unset = UNSET
    allows_derivatives: bool | Unset = UNSET
    ancestors: list[ThingAncestorsItem] | Unset = UNSET
    ancestors_url: str | Unset = UNSET
    app_count: int | Unset = UNSET
    app_id: int | None | Unset = UNSET
    can_comment: bool | Unset = UNSET
    categories_url: str | Unset = UNSET
    collect_count: int | Unset = UNSET
    comment_count: int | Unset = UNSET
    creator: None | Unset | UserSummarySchemaType0 = UNSET
    default_image: ImageSummarySchemaType0 | None | Unset = UNSET
    derivatives_url: str | Unset = UNSET
    description: str | Unset = UNSET
    description_html: str | Unset = UNSET
    details: str | Unset = UNSET
    details_parts: list[ThingDetailsPartsItem] | Unset = UNSET
    download_count: int | Unset = UNSET
    edu_details: str | Unset = UNSET
    edu_details_parts: list[ThingEduDetailsPartsType0Item] | None | Unset = UNSET
    education: ThingEducation | Unset = UNSET
    file_count: int | Unset = UNSET
    files_url: str | Unset = UNSET
    images_url: str | Unset = UNSET
    instructions: str | Unset = UNSET
    instructions_html: str | Unset = UNSET
    is_ai: bool | None | Unset = UNSET
    is_banned: bool | Unset = UNSET
    is_collected: bool | Unset = UNSET
    is_comments_disabled: bool | Unset = UNSET
    is_decoy: int | Unset = UNSET
    is_derivative: bool | Unset = UNSET
    is_featured: bool | Unset = UNSET
    is_liked: bool | Unset = UNSET
    is_nsfw: bool | None | Unset = UNSET
    is_published: int | Unset = UNSET
    is_purchased: int | Unset = UNSET
    is_watched: bool | Unset = UNSET
    is_wip: int | Unset = UNSET
    license_: str | Unset = UNSET
    like_count: int | Unset = UNSET
    likes_url: str | Unset = UNSET
    make_count: int | Unset = UNSET
    moderation: None | str | Unset = UNSET
    modified: datetime.datetime | Unset = UNSET
    needs_moderation: int | Unset = UNSET
    public_url: str | Unset = UNSET
    remix_count: int | Unset = UNSET
    root_comment_count: int | Unset = UNSET
    tags: list[TagSchema] | Unset = UNSET
    tags_url: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    type_name: str | Unset = UNSET
    url: str | Unset = UNSET
    view_count: int | Unset = UNSET
    zip_data: ThingZipData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        id = self.id

        name = self.name

        added: str | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        allows_derivatives = self.allows_derivatives

        ancestors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = []
            for ancestors_item_data in self.ancestors:
                ancestors_item = ancestors_item_data.to_dict()
                ancestors.append(ancestors_item)

        ancestors_url = self.ancestors_url

        app_count = self.app_count

        app_id: int | None | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        can_comment = self.can_comment

        categories_url = self.categories_url

        collect_count = self.collect_count

        comment_count = self.comment_count

        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, UserSummarySchemaType0):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        default_image: dict[str, Any] | None | Unset
        if isinstance(self.default_image, Unset):
            default_image = UNSET
        elif isinstance(self.default_image, ImageSummarySchemaType0):
            default_image = self.default_image.to_dict()
        else:
            default_image = self.default_image

        derivatives_url = self.derivatives_url

        description = self.description

        description_html = self.description_html

        details = self.details

        details_parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details_parts, Unset):
            details_parts = []
            for details_parts_item_data in self.details_parts:
                details_parts_item = details_parts_item_data.to_dict()
                details_parts.append(details_parts_item)

        download_count = self.download_count

        edu_details = self.edu_details

        edu_details_parts: list[dict[str, Any]] | None | Unset
        if isinstance(self.edu_details_parts, Unset):
            edu_details_parts = UNSET
        elif isinstance(self.edu_details_parts, list):
            edu_details_parts = []
            for edu_details_parts_type_0_item_data in self.edu_details_parts:
                edu_details_parts_type_0_item = edu_details_parts_type_0_item_data.to_dict()
                edu_details_parts.append(edu_details_parts_type_0_item)

        else:
            edu_details_parts = self.edu_details_parts

        education: dict[str, Any] | Unset = UNSET
        if not isinstance(self.education, Unset):
            education = self.education.to_dict()

        file_count = self.file_count

        files_url = self.files_url

        images_url = self.images_url

        instructions = self.instructions

        instructions_html = self.instructions_html

        is_ai: bool | None | Unset
        if isinstance(self.is_ai, Unset):
            is_ai = UNSET
        else:
            is_ai = self.is_ai

        is_banned = self.is_banned

        is_collected = self.is_collected

        is_comments_disabled = self.is_comments_disabled

        is_decoy = self.is_decoy

        is_derivative = self.is_derivative

        is_featured = self.is_featured

        is_liked = self.is_liked

        is_nsfw: bool | None | Unset
        if isinstance(self.is_nsfw, Unset):
            is_nsfw = UNSET
        else:
            is_nsfw = self.is_nsfw

        is_published = self.is_published

        is_purchased = self.is_purchased

        is_watched = self.is_watched

        is_wip = self.is_wip

        license_ = self.license_

        like_count = self.like_count

        likes_url = self.likes_url

        make_count = self.make_count

        moderation: None | str | Unset
        if isinstance(self.moderation, Unset):
            moderation = UNSET
        else:
            moderation = self.moderation

        modified: str | Unset = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        needs_moderation = self.needs_moderation

        public_url = self.public_url

        remix_count = self.remix_count

        root_comment_count = self.root_comment_count

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        tags_url = self.tags_url

        thumbnail = self.thumbnail

        type_name = self.type_name

        url = self.url

        view_count = self.view_count

        zip_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.zip_data, Unset):
            zip_data = self.zip_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if added is not UNSET:
            field_dict["added"] = added
        if allows_derivatives is not UNSET:
            field_dict["allows_derivatives"] = allows_derivatives
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if ancestors_url is not UNSET:
            field_dict["ancestors_url"] = ancestors_url
        if app_count is not UNSET:
            field_dict["app_count"] = app_count
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if can_comment is not UNSET:
            field_dict["can_comment"] = can_comment
        if categories_url is not UNSET:
            field_dict["categories_url"] = categories_url
        if collect_count is not UNSET:
            field_dict["collect_count"] = collect_count
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if creator is not UNSET:
            field_dict["creator"] = creator
        if default_image is not UNSET:
            field_dict["default_image"] = default_image
        if derivatives_url is not UNSET:
            field_dict["derivatives_url"] = derivatives_url
        if description is not UNSET:
            field_dict["description"] = description
        if description_html is not UNSET:
            field_dict["description_html"] = description_html
        if details is not UNSET:
            field_dict["details"] = details
        if details_parts is not UNSET:
            field_dict["details_parts"] = details_parts
        if download_count is not UNSET:
            field_dict["download_count"] = download_count
        if edu_details is not UNSET:
            field_dict["edu_details"] = edu_details
        if edu_details_parts is not UNSET:
            field_dict["edu_details_parts"] = edu_details_parts
        if education is not UNSET:
            field_dict["education"] = education
        if file_count is not UNSET:
            field_dict["file_count"] = file_count
        if files_url is not UNSET:
            field_dict["files_url"] = files_url
        if images_url is not UNSET:
            field_dict["images_url"] = images_url
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if instructions_html is not UNSET:
            field_dict["instructions_html"] = instructions_html
        if is_ai is not UNSET:
            field_dict["is_ai"] = is_ai
        if is_banned is not UNSET:
            field_dict["is_banned"] = is_banned
        if is_collected is not UNSET:
            field_dict["is_collected"] = is_collected
        if is_comments_disabled is not UNSET:
            field_dict["is_comments_disabled"] = is_comments_disabled
        if is_decoy is not UNSET:
            field_dict["is_decoy"] = is_decoy
        if is_derivative is not UNSET:
            field_dict["is_derivative"] = is_derivative
        if is_featured is not UNSET:
            field_dict["is_featured"] = is_featured
        if is_liked is not UNSET:
            field_dict["is_liked"] = is_liked
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if is_purchased is not UNSET:
            field_dict["is_purchased"] = is_purchased
        if is_watched is not UNSET:
            field_dict["is_watched"] = is_watched
        if is_wip is not UNSET:
            field_dict["is_wip"] = is_wip
        if license_ is not UNSET:
            field_dict["license"] = license_
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if likes_url is not UNSET:
            field_dict["likes_url"] = likes_url
        if make_count is not UNSET:
            field_dict["make_count"] = make_count
        if moderation is not UNSET:
            field_dict["moderation"] = moderation
        if modified is not UNSET:
            field_dict["modified"] = modified
        if needs_moderation is not UNSET:
            field_dict["needs_moderation"] = needs_moderation
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if remix_count is not UNSET:
            field_dict["remix_count"] = remix_count
        if root_comment_count is not UNSET:
            field_dict["root_comment_count"] = root_comment_count
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tags_url is not UNSET:
            field_dict["tags_url"] = tags_url
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if type_name is not UNSET:
            field_dict["type_name"] = type_name
        if url is not UNSET:
            field_dict["url"] = url
        if view_count is not UNSET:
            field_dict["view_count"] = view_count
        if zip_data is not UNSET:
            field_dict["zip_data"] = zip_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0
        from ..models.tag_schema import TagSchema
        from ..models.thing_ancestors_item import ThingAncestorsItem
        from ..models.thing_details_parts_item import ThingDetailsPartsItem
        from ..models.thing_edu_details_parts_type_0_item import ThingEduDetailsPartsType0Item
        from ..models.thing_education import ThingEducation
        from ..models.thing_zip_data import ThingZipData
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        _added = d.pop("added", UNSET)
        added: datetime.datetime | Unset
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        allows_derivatives = d.pop("allows_derivatives", UNSET)

        _ancestors = d.pop("ancestors", UNSET)
        ancestors: list[ThingAncestorsItem] | Unset = UNSET
        if _ancestors is not UNSET:
            ancestors = []
            for ancestors_item_data in _ancestors:
                ancestors_item = ThingAncestorsItem.from_dict(ancestors_item_data)

                ancestors.append(ancestors_item)

        ancestors_url = d.pop("ancestors_url", UNSET)

        app_count = d.pop("app_count", UNSET)

        def _parse_app_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        can_comment = d.pop("can_comment", UNSET)

        categories_url = d.pop("categories_url", UNSET)

        collect_count = d.pop("collect_count", UNSET)

        comment_count = d.pop("comment_count", UNSET)

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

        def _parse_default_image(data: object) -> ImageSummarySchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasimage_summary_schema_type_0 = ImageSummarySchemaType0.from_dict(
                    data
                )

                return componentsschemasimage_summary_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageSummarySchemaType0 | None | Unset, data)

        default_image = _parse_default_image(d.pop("default_image", UNSET))

        derivatives_url = d.pop("derivatives_url", UNSET)

        description = d.pop("description", UNSET)

        description_html = d.pop("description_html", UNSET)

        details = d.pop("details", UNSET)

        _details_parts = d.pop("details_parts", UNSET)
        details_parts: list[ThingDetailsPartsItem] | Unset = UNSET
        if _details_parts is not UNSET:
            details_parts = []
            for details_parts_item_data in _details_parts:
                details_parts_item = ThingDetailsPartsItem.from_dict(details_parts_item_data)

                details_parts.append(details_parts_item)

        download_count = d.pop("download_count", UNSET)

        edu_details = d.pop("edu_details", UNSET)

        def _parse_edu_details_parts(
            data: object,
        ) -> list[ThingEduDetailsPartsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edu_details_parts_type_0 = []
                _edu_details_parts_type_0 = data
                for edu_details_parts_type_0_item_data in _edu_details_parts_type_0:
                    edu_details_parts_type_0_item = ThingEduDetailsPartsType0Item.from_dict(
                        edu_details_parts_type_0_item_data
                    )

                    edu_details_parts_type_0.append(edu_details_parts_type_0_item)

                return edu_details_parts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ThingEduDetailsPartsType0Item] | None | Unset, data)

        edu_details_parts = _parse_edu_details_parts(d.pop("edu_details_parts", UNSET))

        _education = d.pop("education", UNSET)
        education: ThingEducation | Unset
        if isinstance(_education, Unset):
            education = UNSET
        else:
            education = ThingEducation.from_dict(_education)

        file_count = d.pop("file_count", UNSET)

        files_url = d.pop("files_url", UNSET)

        images_url = d.pop("images_url", UNSET)

        instructions = d.pop("instructions", UNSET)

        instructions_html = d.pop("instructions_html", UNSET)

        def _parse_is_ai(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_ai = _parse_is_ai(d.pop("is_ai", UNSET))

        is_banned = d.pop("is_banned", UNSET)

        is_collected = d.pop("is_collected", UNSET)

        is_comments_disabled = d.pop("is_comments_disabled", UNSET)

        is_decoy = d.pop("is_decoy", UNSET)

        is_derivative = d.pop("is_derivative", UNSET)

        is_featured = d.pop("is_featured", UNSET)

        is_liked = d.pop("is_liked", UNSET)

        def _parse_is_nsfw(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_nsfw = _parse_is_nsfw(d.pop("is_nsfw", UNSET))

        is_published = d.pop("is_published", UNSET)

        is_purchased = d.pop("is_purchased", UNSET)

        is_watched = d.pop("is_watched", UNSET)

        is_wip = d.pop("is_wip", UNSET)

        license_ = d.pop("license", UNSET)

        like_count = d.pop("like_count", UNSET)

        likes_url = d.pop("likes_url", UNSET)

        make_count = d.pop("make_count", UNSET)

        def _parse_moderation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        moderation = _parse_moderation(d.pop("moderation", UNSET))

        _modified = d.pop("modified", UNSET)
        modified: datetime.datetime | Unset
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        needs_moderation = d.pop("needs_moderation", UNSET)

        public_url = d.pop("public_url", UNSET)

        remix_count = d.pop("remix_count", UNSET)

        root_comment_count = d.pop("root_comment_count", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[TagSchema] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = TagSchema.from_dict(tags_item_data)

                tags.append(tags_item)

        tags_url = d.pop("tags_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        type_name = d.pop("type_name", UNSET)

        url = d.pop("url", UNSET)

        view_count = d.pop("view_count", UNSET)

        _zip_data = d.pop("zip_data", UNSET)
        zip_data: ThingZipData | Unset
        if isinstance(_zip_data, Unset):
            zip_data = UNSET
        else:
            zip_data = ThingZipData.from_dict(_zip_data)

        thing = cls(
            id=id,
            name=name,
            added=added,
            allows_derivatives=allows_derivatives,
            ancestors=ancestors,
            ancestors_url=ancestors_url,
            app_count=app_count,
            app_id=app_id,
            can_comment=can_comment,
            categories_url=categories_url,
            collect_count=collect_count,
            comment_count=comment_count,
            creator=creator,
            default_image=default_image,
            derivatives_url=derivatives_url,
            description=description,
            description_html=description_html,
            details=details,
            details_parts=details_parts,
            download_count=download_count,
            edu_details=edu_details,
            edu_details_parts=edu_details_parts,
            education=education,
            file_count=file_count,
            files_url=files_url,
            images_url=images_url,
            instructions=instructions,
            instructions_html=instructions_html,
            is_ai=is_ai,
            is_banned=is_banned,
            is_collected=is_collected,
            is_comments_disabled=is_comments_disabled,
            is_decoy=is_decoy,
            is_derivative=is_derivative,
            is_featured=is_featured,
            is_liked=is_liked,
            is_nsfw=is_nsfw,
            is_published=is_published,
            is_purchased=is_purchased,
            is_watched=is_watched,
            is_wip=is_wip,
            license_=license_,
            like_count=like_count,
            likes_url=likes_url,
            make_count=make_count,
            moderation=moderation,
            modified=modified,
            needs_moderation=needs_moderation,
            public_url=public_url,
            remix_count=remix_count,
            root_comment_count=root_comment_count,
            tags=tags,
            tags_url=tags_url,
            thumbnail=thumbnail,
            type_name=type_name,
            url=url,
            view_count=view_count,
            zip_data=zip_data,
        )

        thing.additional_properties = d
        return thing

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
