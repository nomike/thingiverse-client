from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_banner_0_page_ad_response_200_custom_ads import (
        GetBanner0PageAdResponse200CustomAds,
    )


T = TypeVar("T", bound="GetBanner0PageAdResponse200")


@_attrs_define
class GetBanner0PageAdResponse200:
    """
    Attributes:
        blocked_ad_variation (str | Unset):
        custom_ads (GetBanner0PageAdResponse200CustomAds | Unset):
    """

    blocked_ad_variation: str | Unset = UNSET
    custom_ads: GetBanner0PageAdResponse200CustomAds | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocked_ad_variation = self.blocked_ad_variation

        custom_ads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_ads, Unset):
            custom_ads = self.custom_ads.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blocked_ad_variation is not UNSET:
            field_dict["blockedAdVariation"] = blocked_ad_variation
        if custom_ads is not UNSET:
            field_dict["customAds"] = custom_ads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_banner_0_page_ad_response_200_custom_ads import (
            GetBanner0PageAdResponse200CustomAds,
        )

        d = dict(src_dict)
        blocked_ad_variation = d.pop("blockedAdVariation", UNSET)

        _custom_ads = d.pop("customAds", UNSET)
        custom_ads: GetBanner0PageAdResponse200CustomAds | Unset
        if isinstance(_custom_ads, Unset):
            custom_ads = UNSET
        else:
            custom_ads = GetBanner0PageAdResponse200CustomAds.from_dict(_custom_ads)

        get_banner_0_page_ad_response_200 = cls(
            blocked_ad_variation=blocked_ad_variation,
            custom_ads=custom_ads,
        )

        get_banner_0_page_ad_response_200.additional_properties = d
        return get_banner_0_page_ad_response_200

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
