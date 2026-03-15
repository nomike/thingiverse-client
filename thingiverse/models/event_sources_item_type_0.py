from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0


T = TypeVar("T", bound="EventSourcesItemType0")


@_attrs_define
class EventSourcesItemType0:
    """
    Attributes:
        default_image (ImageSummarySchemaType0 | None | Unset):
        thumbnail (str | Unset):
    """

    default_image: ImageSummarySchemaType0 | None | Unset = UNSET
    thumbnail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0

        default_image: dict[str, Any] | None | Unset
        if isinstance(self.default_image, Unset):
            default_image = UNSET
        elif isinstance(self.default_image, ImageSummarySchemaType0):
            default_image = self.default_image.to_dict()
        else:
            default_image = self.default_image

        thumbnail = self.thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_image is not UNSET:
            field_dict["default_image"] = default_image
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0

        d = dict(src_dict)

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

        thumbnail = d.pop("thumbnail", UNSET)

        event_sources_item_type_0 = cls(
            default_image=default_image,
            thumbnail=thumbnail,
        )

        event_sources_item_type_0.additional_properties = d
        return event_sources_item_type_0

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
