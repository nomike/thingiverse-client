from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_summary_schema_type_0 import UserSummarySchemaType0


T = TypeVar("T", bound="App")


@_attrs_define
class App:
    """
    Attributes:
        creator (None | Unset | UserSummarySchemaType0):
        id (int | Unset):
        is_approved (bool | Unset):
        is_published (bool | Unset):
        name (str | Unset):
        public_url (str | Unset):
        thumbnail (str | Unset):
        url (str | Unset):
    """

    creator: None | Unset | UserSummarySchemaType0 = UNSET
    id: int | Unset = UNSET
    is_approved: bool | Unset = UNSET
    is_published: bool | Unset = UNSET
    name: str | Unset = UNSET
    public_url: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, UserSummarySchemaType0):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        id = self.id

        is_approved = self.is_approved

        is_published = self.is_published

        name = self.name

        public_url = self.public_url

        thumbnail = self.thumbnail

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if id is not UNSET:
            field_dict["id"] = id
        if is_approved is not UNSET:
            field_dict["is_approved"] = is_approved
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
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
        from ..models.user_summary_schema_type_0 import UserSummarySchemaType0

        d = dict(src_dict)

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

        is_approved = d.pop("is_approved", UNSET)

        is_published = d.pop("is_published", UNSET)

        name = d.pop("name", UNSET)

        public_url = d.pop("public_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        url = d.pop("url", UNSET)

        app = cls(
            creator=creator,
            id=id,
            is_approved=is_approved,
            is_published=is_published,
            name=name,
            public_url=public_url,
            thumbnail=thumbnail,
            url=url,
        )

        app.additional_properties = d
        return app

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
