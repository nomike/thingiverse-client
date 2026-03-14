from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BannerSchema")


@_attrs_define
class BannerSchema:
    """
    Attributes:
        banner_image (str | Unset):
        banner_mobile_image (str | Unset):
        banner_mobile_video (str | Unset):
        banner_tablet_image (str | Unset):
        banner_tablet_video (str | Unset):
        banner_url (str | Unset):
        banner_video (str | Unset):
        big_banner_image (str | Unset):
        big_banner_video (str | Unset):
        location (str | Unset):
    """

    banner_image: str | Unset = UNSET
    banner_mobile_image: str | Unset = UNSET
    banner_mobile_video: str | Unset = UNSET
    banner_tablet_image: str | Unset = UNSET
    banner_tablet_video: str | Unset = UNSET
    banner_url: str | Unset = UNSET
    banner_video: str | Unset = UNSET
    big_banner_image: str | Unset = UNSET
    big_banner_video: str | Unset = UNSET
    location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        banner_image = self.banner_image

        banner_mobile_image = self.banner_mobile_image

        banner_mobile_video = self.banner_mobile_video

        banner_tablet_image = self.banner_tablet_image

        banner_tablet_video = self.banner_tablet_video

        banner_url = self.banner_url

        banner_video = self.banner_video

        big_banner_image = self.big_banner_image

        big_banner_video = self.big_banner_video

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if banner_image is not UNSET:
            field_dict["banner_image"] = banner_image
        if banner_mobile_image is not UNSET:
            field_dict["banner_mobile_image"] = banner_mobile_image
        if banner_mobile_video is not UNSET:
            field_dict["banner_mobile_video"] = banner_mobile_video
        if banner_tablet_image is not UNSET:
            field_dict["banner_tablet_image"] = banner_tablet_image
        if banner_tablet_video is not UNSET:
            field_dict["banner_tablet_video"] = banner_tablet_video
        if banner_url is not UNSET:
            field_dict["banner_url"] = banner_url
        if banner_video is not UNSET:
            field_dict["banner_video"] = banner_video
        if big_banner_image is not UNSET:
            field_dict["big_banner_image"] = big_banner_image
        if big_banner_video is not UNSET:
            field_dict["big_banner_video"] = big_banner_video
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        banner_image = d.pop("banner_image", UNSET)

        banner_mobile_image = d.pop("banner_mobile_image", UNSET)

        banner_mobile_video = d.pop("banner_mobile_video", UNSET)

        banner_tablet_image = d.pop("banner_tablet_image", UNSET)

        banner_tablet_video = d.pop("banner_tablet_video", UNSET)

        banner_url = d.pop("banner_url", UNSET)

        banner_video = d.pop("banner_video", UNSET)

        big_banner_image = d.pop("big_banner_image", UNSET)

        big_banner_video = d.pop("big_banner_video", UNSET)

        location = d.pop("location", UNSET)

        banner_schema = cls(
            banner_image=banner_image,
            banner_mobile_image=banner_mobile_image,
            banner_mobile_video=banner_mobile_video,
            banner_tablet_image=banner_tablet_image,
            banner_tablet_video=banner_tablet_video,
            banner_url=banner_url,
            banner_video=banner_video,
            big_banner_image=big_banner_image,
            big_banner_video=big_banner_video,
            location=location,
        )

        banner_schema.additional_properties = d
        return banner_schema

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
