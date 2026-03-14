from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_summary_schema_type_0 import UserSummarySchemaType0


T = TypeVar("T", bound="CollectionSchema")


@_attrs_define
class CollectionSchema:
    r"""
    Attributes:
        absolute_url (str):  Example: https://staging.thingiverse.com/CreativeTools/collections/7287575/things.
        added (datetime.datetime):  Example: 2017-01-16T22:21:25+00:00.
        count (int):  Example: 1.
        creator (None | UserSummarySchemaType0):
        description (str):  Example: meep.
        featured_thing_id (int | None): ID of the thing that is marked by the creator as being the "primary" thing.
        id (int):  Example: 7287575.
        is_editable (bool):
        is_featured (bool):
        is_watched (bool):
        modified (datetime.datetime):  Example: 2020-05-26T14:23:36+00:00.
        name (str):  Example: Calibration objects (By CreativeTools).
        preview_image (str):  Example:
            https://cdn.thingiverse.com/renders/98/d7/7c/14/a1/8169058952_beddf5f755_o_preview_card.jpg.
        thumbnail (str):  Example:
            https://cdn.thingiverse.com/renders/98/d7/7c/14/a1/8169058952_beddf5f755_o_preview_medium.jpg.
        url (str):  Example: https://api.thingiverse.com/collections/7287575.
        description_html (str | Unset):  Example: <div><p><strong>meep</strong></p></div>\n.
        featured_on (None | str | Unset): When thing was featured. Is only set when is_featured is true
        is_liked (bool | Unset):
    """

    absolute_url: str
    added: datetime.datetime
    count: int
    creator: None | UserSummarySchemaType0
    description: str
    featured_thing_id: int | None
    id: int
    is_editable: bool
    is_featured: bool
    is_watched: bool
    modified: datetime.datetime
    name: str
    preview_image: str
    thumbnail: str
    url: str
    description_html: str | Unset = UNSET
    featured_on: None | str | Unset = UNSET
    is_liked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        absolute_url = self.absolute_url

        added = self.added.isoformat()

        count = self.count

        creator: dict[str, Any] | None
        if isinstance(self.creator, UserSummarySchemaType0):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        description = self.description

        featured_thing_id: int | None
        featured_thing_id = self.featured_thing_id

        id = self.id

        is_editable = self.is_editable

        is_featured = self.is_featured

        is_watched = self.is_watched

        modified = self.modified.isoformat()

        name = self.name

        preview_image = self.preview_image

        thumbnail = self.thumbnail

        url = self.url

        description_html = self.description_html

        featured_on: None | str | Unset
        if isinstance(self.featured_on, Unset):
            featured_on = UNSET
        else:
            featured_on = self.featured_on

        is_liked = self.is_liked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "absolute_url": absolute_url,
                "added": added,
                "count": count,
                "creator": creator,
                "description": description,
                "featured_thing_id": featured_thing_id,
                "id": id,
                "is_editable": is_editable,
                "is_featured": is_featured,
                "is_watched": is_watched,
                "modified": modified,
                "name": name,
                "preview_image": preview_image,
                "thumbnail": thumbnail,
                "url": url,
            }
        )
        if description_html is not UNSET:
            field_dict["description_html"] = description_html
        if featured_on is not UNSET:
            field_dict["featured_on"] = featured_on
        if is_liked is not UNSET:
            field_dict["is_liked"] = is_liked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        d = dict(src_dict)
        absolute_url = d.pop("absolute_url")

        added = isoparse(d.pop("added"))

        count = d.pop("count")

        def _parse_creator(data: object) -> None | UserSummarySchemaType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasuser_summary_schema_type_0 = UserSummarySchemaType0.from_dict(data)

                return componentsschemasuser_summary_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserSummarySchemaType0, data)

        creator = _parse_creator(d.pop("creator"))

        description = d.pop("description")

        def _parse_featured_thing_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        featured_thing_id = _parse_featured_thing_id(d.pop("featured_thing_id"))

        id = d.pop("id")

        is_editable = d.pop("is_editable")

        is_featured = d.pop("is_featured")

        is_watched = d.pop("is_watched")

        modified = isoparse(d.pop("modified"))

        name = d.pop("name")

        preview_image = d.pop("preview_image")

        thumbnail = d.pop("thumbnail")

        url = d.pop("url")

        description_html = d.pop("description_html", UNSET)

        def _parse_featured_on(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        featured_on = _parse_featured_on(d.pop("featured_on", UNSET))

        is_liked = d.pop("is_liked", UNSET)

        collection_schema = cls(
            absolute_url=absolute_url,
            added=added,
            count=count,
            creator=creator,
            description=description,
            featured_thing_id=featured_thing_id,
            id=id,
            is_editable=is_editable,
            is_featured=is_featured,
            is_watched=is_watched,
            modified=modified,
            name=name,
            preview_image=preview_image,
            thumbnail=thumbnail,
            url=url,
            description_html=description_html,
            featured_on=featured_on,
            is_liked=is_liked,
        )

        collection_schema.additional_properties = d
        return collection_schema

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
