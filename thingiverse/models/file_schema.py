from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_schema_meta_data_item import FileSchemaMetaDataItem
    from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0


T = TypeVar("T", bound="FileSchema")


@_attrs_define
class FileSchema:
    """
    Attributes:
        date (str | Unset):  Example: 2015-04-09 12:55:22.
        default_image (ImageSummarySchemaType0 | None | Unset):
        direct_url (None | str | Unset): This will return null if it's not in the 'printable' file list (eg a pdf)
            Example: https://cdn.thingiverse.com/assets/7d/fc/6e/33/fe/3DBenchy.stl.
        download_count (int | Unset):  Example: 451301.
        download_url (str | Unset):  Example: https://api.thingiverse.com/files/1223854/download.
        formatted_size (str | Unset): a formatted string of a filesize Example: 10 mb.
        id (int | Unset):  Example: 1223854.
        meta_data (list[FileSchemaMetaDataItem] | Unset):
        name (str | Unset):  Example: 3DBenchy.stl.
        public_url (str | Unset):  Example: https://www.thingiverse.com/download:1223854.
        size (int | Unset):  Example: 11285384.
        threejs_url (str | Unset):  Example: https://cdn.thingiverse.com/threejs_json/07/ad/ba/fc/87/3DBenchy.js.
        thumbnail (str | Unset):  Example: https://cdn.thingiverse.com/renders/40/37/dc/8d/31/3DBenchy_thumb_medium.jpg.
        url (str | Unset):  Example: https://api.thingiverse.com/files/1223854.
    """

    date: str | Unset = UNSET
    default_image: ImageSummarySchemaType0 | None | Unset = UNSET
    direct_url: None | str | Unset = UNSET
    download_count: int | Unset = UNSET
    download_url: str | Unset = UNSET
    formatted_size: str | Unset = UNSET
    id: int | Unset = UNSET
    meta_data: list[FileSchemaMetaDataItem] | Unset = UNSET
    name: str | Unset = UNSET
    public_url: str | Unset = UNSET
    size: int | Unset = UNSET
    threejs_url: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0

        date = self.date

        default_image: dict[str, Any] | None | Unset
        if isinstance(self.default_image, Unset):
            default_image = UNSET
        elif isinstance(self.default_image, ImageSummarySchemaType0):
            default_image = self.default_image.to_dict()
        else:
            default_image = self.default_image

        direct_url: None | str | Unset
        if isinstance(self.direct_url, Unset):
            direct_url = UNSET
        else:
            direct_url = self.direct_url

        download_count = self.download_count

        download_url = self.download_url

        formatted_size = self.formatted_size

        id = self.id

        meta_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = []
            for meta_data_item_data in self.meta_data:
                meta_data_item = meta_data_item_data.to_dict()
                meta_data.append(meta_data_item)

        name = self.name

        public_url = self.public_url

        size = self.size

        threejs_url = self.threejs_url

        thumbnail = self.thumbnail

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if default_image is not UNSET:
            field_dict["default_image"] = default_image
        if direct_url is not UNSET:
            field_dict["direct_url"] = direct_url
        if download_count is not UNSET:
            field_dict["download_count"] = download_count
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if formatted_size is not UNSET:
            field_dict["formatted_size"] = formatted_size
        if id is not UNSET:
            field_dict["id"] = id
        if meta_data is not UNSET:
            field_dict["meta_data"] = meta_data
        if name is not UNSET:
            field_dict["name"] = name
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if size is not UNSET:
            field_dict["size"] = size
        if threejs_url is not UNSET:
            field_dict["threejs_url"] = threejs_url
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_schema_meta_data_item import FileSchemaMetaDataItem
        from ..models.image_summary_schema_type_0 import ImageSummarySchemaType0

        d = dict(src_dict)
        date = d.pop("date", UNSET)

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

        def _parse_direct_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direct_url = _parse_direct_url(d.pop("direct_url", UNSET))

        download_count = d.pop("download_count", UNSET)

        download_url = d.pop("download_url", UNSET)

        formatted_size = d.pop("formatted_size", UNSET)

        id = d.pop("id", UNSET)

        _meta_data = d.pop("meta_data", UNSET)
        meta_data: list[FileSchemaMetaDataItem] | Unset = UNSET
        if _meta_data is not UNSET:
            meta_data = []
            for meta_data_item_data in _meta_data:
                meta_data_item = FileSchemaMetaDataItem.from_dict(meta_data_item_data)

                meta_data.append(meta_data_item)

        name = d.pop("name", UNSET)

        public_url = d.pop("public_url", UNSET)

        size = d.pop("size", UNSET)

        threejs_url = d.pop("threejs_url", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        url = d.pop("url", UNSET)

        file_schema = cls(
            date=date,
            default_image=default_image,
            direct_url=direct_url,
            download_count=download_count,
            download_url=download_url,
            formatted_size=formatted_size,
            id=id,
            meta_data=meta_data,
            name=name,
            public_url=public_url,
            size=size,
            threejs_url=threejs_url,
            thumbnail=thumbnail,
            url=url,
        )

        file_schema.additional_properties = d
        return file_schema

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
