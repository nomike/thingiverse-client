from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.copy_details_parts_item import CopyDetailsPartsItem
    from ..models.thing_schema import ThingSchema
    from ..models.user_summary_schema_type_0 import UserSummarySchemaType0


T = TypeVar("T", bound="Copy")


@_attrs_define
class Copy:
    r"""
    Attributes:
        added (datetime.datetime | Unset):  Example: 2018-05-15T17:30:32+00:00.
        category_name (str | Unset):  Example: 3D Printing Tests.
        category_url (str | Unset):  Example: /categories/3d-printing/3d-printing-tests.
        comment_count (int | Unset):
        creator (None | Unset | UserSummarySchemaType0):
        description (str | Unset):  Example: First print on the SnapMaker straight out of the box. Came out beautifully.
        description_html (str | Unset):  Example: <div><p>First print on the SnapMaker straight out of the box. Came out
            beautifully<\/p><\/div>\n.
        details (str | Unset):  Example: <h1 class=\"thing-component-header summary
            description\">Description</h1>\n<div><p>First print on the SnapMaker straight out of the box. Came out
            beautifully</p></div>\n<h1 class=\"thing-component-header settings print-settings\">Print Settings</h1>\n<p
            class=\"detail-setting printer\"><strong>Printer: </strong>\n                         <div><p>SnapMaker
            3-in-1</p></div>\n</p>                                    \n                                                <p
            class=\"detail-setting rafts\"><strong>Rafts: </strong>\n                         <div><p>No</p></div>\n</p>
            \n                                                <p class=\"detail-setting supports\"><strong>Supports:
            </strong>\n                         <div><p>No</p></div>\n</p>                                    \n
            <p class=\"detail-setting resolution\"><strong>Resolution: </strong>\n                         <div><p>0.2
            mm</p></div>\n</p>                                    \n                                                <p
            class=\"detail-setting infill\"><strong>Infill: </strong>\n                         <div><p>8%</p></div>\n</p>
            \n                        <br>                        <p class=\"detail-setting notes\"><strong>Notes:
            </strong>\n                        </p><div><p>PLA</p></div>\n.
        details_parts (list[CopyDetailsPartsItem] | Unset):
        id (int | Unset):  Example: 491683.
        images_url (str | Unset):  Example: https://api.thingiverse.com/copies/491683/images.
        is_comments_disabled (bool | Unset):
        is_liked (bool | Unset):
        is_watched (bool | Unset):
        like_count (int | Unset):  Example: 2.
        name (str | Unset):  Example: #3DBenchy - The jolly 3D printing torture-test by CreativeTools.se.
        needs_moderation (bool | Unset):
        preview_image (str | Unset):  Example:
            https://cdn.thingiverse.com/renders/e1/29/55/07/54/f85e5d82c3c10a936c72cc593ba47308_preview_card.JPG.
        public_url (str | Unset):  Example: https://www.thingiverse.com/make:491683.
        root_comment_count (int | Unset):
        thing (ThingSchema | Unset):
        thumbnail (str | Unset):  Example:
            https://cdn.thingiverse.com/renders/e1/29/55/07/54/f85e5d82c3c10a936c72cc593ba47308_thumb_medium.JPG.
        type_name (str | Unset):  Example: Make.
        url (str | Unset):  Example: https://api.thingiverse.com/copies/491683.
        view_count (int | Unset):  Example: 1.
    """

    added: datetime.datetime | Unset = UNSET
    category_name: str | Unset = UNSET
    category_url: str | Unset = UNSET
    comment_count: int | Unset = UNSET
    creator: None | Unset | UserSummarySchemaType0 = UNSET
    description: str | Unset = UNSET
    description_html: str | Unset = UNSET
    details: str | Unset = UNSET
    details_parts: list[CopyDetailsPartsItem] | Unset = UNSET
    id: int | Unset = UNSET
    images_url: str | Unset = UNSET
    is_comments_disabled: bool | Unset = UNSET
    is_liked: bool | Unset = UNSET
    is_watched: bool | Unset = UNSET
    like_count: int | Unset = UNSET
    name: str | Unset = UNSET
    needs_moderation: bool | Unset = UNSET
    preview_image: str | Unset = UNSET
    public_url: str | Unset = UNSET
    root_comment_count: int | Unset = UNSET
    thing: ThingSchema | Unset = UNSET
    thumbnail: str | Unset = UNSET
    type_name: str | Unset = UNSET
    url: str | Unset = UNSET
    view_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        added: str | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        category_name = self.category_name

        category_url = self.category_url

        comment_count = self.comment_count

        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, UserSummarySchemaType0):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        description = self.description

        description_html = self.description_html

        details = self.details

        details_parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details_parts, Unset):
            details_parts = []
            for details_parts_item_data in self.details_parts:
                details_parts_item = details_parts_item_data.to_dict()
                details_parts.append(details_parts_item)

        id = self.id

        images_url = self.images_url

        is_comments_disabled = self.is_comments_disabled

        is_liked = self.is_liked

        is_watched = self.is_watched

        like_count = self.like_count

        name = self.name

        needs_moderation = self.needs_moderation

        preview_image = self.preview_image

        public_url = self.public_url

        root_comment_count = self.root_comment_count

        thing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thing, Unset):
            thing = self.thing.to_dict()

        thumbnail = self.thumbnail

        type_name = self.type_name

        url = self.url

        view_count = self.view_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if category_url is not UNSET:
            field_dict["category_url"] = category_url
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if description_html is not UNSET:
            field_dict["description_html"] = description_html
        if details is not UNSET:
            field_dict["details"] = details
        if details_parts is not UNSET:
            field_dict["details_parts"] = details_parts
        if id is not UNSET:
            field_dict["id"] = id
        if images_url is not UNSET:
            field_dict["images_url"] = images_url
        if is_comments_disabled is not UNSET:
            field_dict["is_comments_disabled"] = is_comments_disabled
        if is_liked is not UNSET:
            field_dict["is_liked"] = is_liked
        if is_watched is not UNSET:
            field_dict["is_watched"] = is_watched
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if name is not UNSET:
            field_dict["name"] = name
        if needs_moderation is not UNSET:
            field_dict["needs_moderation"] = needs_moderation
        if preview_image is not UNSET:
            field_dict["preview_image"] = preview_image
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if root_comment_count is not UNSET:
            field_dict["root_comment_count"] = root_comment_count
        if thing is not UNSET:
            field_dict["thing"] = thing
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if type_name is not UNSET:
            field_dict["type_name"] = type_name
        if url is not UNSET:
            field_dict["url"] = url
        if view_count is not UNSET:
            field_dict["view_count"] = view_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.copy_details_parts_item import CopyDetailsPartsItem
        from ..models.thing_schema import ThingSchema
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        d = dict(src_dict)
        _added = d.pop("added", UNSET)
        added: datetime.datetime | Unset
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        category_name = d.pop("category_name", UNSET)

        category_url = d.pop("category_url", UNSET)

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

        description = d.pop("description", UNSET)

        description_html = d.pop("description_html", UNSET)

        details = d.pop("details", UNSET)

        _details_parts = d.pop("details_parts", UNSET)
        details_parts: list[CopyDetailsPartsItem] | Unset = UNSET
        if _details_parts is not UNSET:
            details_parts = []
            for details_parts_item_data in _details_parts:
                details_parts_item = CopyDetailsPartsItem.from_dict(details_parts_item_data)

                details_parts.append(details_parts_item)

        id = d.pop("id", UNSET)

        images_url = d.pop("images_url", UNSET)

        is_comments_disabled = d.pop("is_comments_disabled", UNSET)

        is_liked = d.pop("is_liked", UNSET)

        is_watched = d.pop("is_watched", UNSET)

        like_count = d.pop("like_count", UNSET)

        name = d.pop("name", UNSET)

        needs_moderation = d.pop("needs_moderation", UNSET)

        preview_image = d.pop("preview_image", UNSET)

        public_url = d.pop("public_url", UNSET)

        root_comment_count = d.pop("root_comment_count", UNSET)

        _thing = d.pop("thing", UNSET)
        thing: ThingSchema | Unset
        if isinstance(_thing, Unset):
            thing = UNSET
        else:
            thing = ThingSchema.from_dict(_thing)

        thumbnail = d.pop("thumbnail", UNSET)

        type_name = d.pop("type_name", UNSET)

        url = d.pop("url", UNSET)

        view_count = d.pop("view_count", UNSET)

        copy = cls(
            added=added,
            category_name=category_name,
            category_url=category_url,
            comment_count=comment_count,
            creator=creator,
            description=description,
            description_html=description_html,
            details=details,
            details_parts=details_parts,
            id=id,
            images_url=images_url,
            is_comments_disabled=is_comments_disabled,
            is_liked=is_liked,
            is_watched=is_watched,
            like_count=like_count,
            name=name,
            needs_moderation=needs_moderation,
            preview_image=preview_image,
            public_url=public_url,
            root_comment_count=root_comment_count,
            thing=thing,
            thumbnail=thumbnail,
            type_name=type_name,
            url=url,
            view_count=view_count,
        )

        copy.additional_properties = d
        return copy

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
