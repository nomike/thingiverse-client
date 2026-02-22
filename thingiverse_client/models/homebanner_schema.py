from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thing_schema import ThingSchema


T = TypeVar("T", bound="HomebannerSchema")


@_attrs_define
class HomebannerSchema:
    """
    Attributes:
        background_color (str | Unset):
        background_image_url (str | Unset):
        body (str | Unset):
        button_name (str | Unset):
        button_url (str | Unset):
        id (int | Unset):
        image_url (str | Unset):
        mobile_image_url (str | Unset):
        tablet_image_url (str | Unset):
        thing (ThingSchema | Unset):
        title (str | Unset):
        type_ (str | Unset):
    """

    background_color: str | Unset = UNSET
    background_image_url: str | Unset = UNSET
    body: str | Unset = UNSET
    button_name: str | Unset = UNSET
    button_url: str | Unset = UNSET
    id: int | Unset = UNSET
    image_url: str | Unset = UNSET
    mobile_image_url: str | Unset = UNSET
    tablet_image_url: str | Unset = UNSET
    thing: ThingSchema | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_color = self.background_color

        background_image_url = self.background_image_url

        body = self.body

        button_name = self.button_name

        button_url = self.button_url

        id = self.id

        image_url = self.image_url

        mobile_image_url = self.mobile_image_url

        tablet_image_url = self.tablet_image_url

        thing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thing, Unset):
            thing = self.thing.to_dict()

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_color is not UNSET:
            field_dict["background_color"] = background_color
        if background_image_url is not UNSET:
            field_dict["background_image_url"] = background_image_url
        if body is not UNSET:
            field_dict["body"] = body
        if button_name is not UNSET:
            field_dict["button_name"] = button_name
        if button_url is not UNSET:
            field_dict["button_url"] = button_url
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if mobile_image_url is not UNSET:
            field_dict["mobile_image_url"] = mobile_image_url
        if tablet_image_url is not UNSET:
            field_dict["tablet_image_url"] = tablet_image_url
        if thing is not UNSET:
            field_dict["thing"] = thing
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thing_schema import ThingSchema

        d = dict(src_dict)
        background_color = d.pop("background_color", UNSET)

        background_image_url = d.pop("background_image_url", UNSET)

        body = d.pop("body", UNSET)

        button_name = d.pop("button_name", UNSET)

        button_url = d.pop("button_url", UNSET)

        id = d.pop("id", UNSET)

        image_url = d.pop("image_url", UNSET)

        mobile_image_url = d.pop("mobile_image_url", UNSET)

        tablet_image_url = d.pop("tablet_image_url", UNSET)

        _thing = d.pop("thing", UNSET)
        thing: ThingSchema | Unset
        if isinstance(_thing, Unset):
            thing = UNSET
        else:
            thing = ThingSchema.from_dict(_thing)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        homebanner_schema = cls(
            background_color=background_color,
            background_image_url=background_image_url,
            body=body,
            button_name=button_name,
            button_url=button_url,
            id=id,
            image_url=image_url,
            mobile_image_url=mobile_image_url,
            tablet_image_url=tablet_image_url,
            thing=thing,
            title=title,
            type_=type_,
        )

        homebanner_schema.additional_properties = d
        return homebanner_schema

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
