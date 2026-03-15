from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_copies_copy_id_threaded_comments_response_200_comments_additional_property_needs_moderation import (
    GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyNeedsModeration,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_copies_copy_id_threaded_comments_response_200_comments_additional_property_assets_item import (
        GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyAssetsItem,
    )


T = TypeVar("T", bound="GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalProperty")


@_attrs_define
class GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalProperty:
    """
    Attributes:
        add_date (datetime.datetime | Unset):
        assets (list[GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyAssetsItem] | Unset):
        body (str | Unset):
        id (int | Unset):
        is_deleted (bool | Unset):
        modified_date (datetime.datetime | str | Unset):
        needs_moderation (GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyNeedsModeration | Unset):
        parent_id (int | Unset):
        parent_url (str | Unset):
        parent_user_name (str | Unset):
        url (str | Unset):
        user_id (int | Unset):
    """

    add_date: datetime.datetime | Unset = UNSET
    assets: (
        list[GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyAssetsItem] | Unset
    ) = UNSET
    body: str | Unset = UNSET
    id: int | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    modified_date: datetime.datetime | str | Unset = UNSET
    needs_moderation: (
        GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyNeedsModeration | Unset
    ) = UNSET
    parent_id: int | Unset = UNSET
    parent_url: str | Unset = UNSET
    parent_user_name: str | Unset = UNSET
    url: str | Unset = UNSET
    user_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_date: str | Unset = UNSET
        if not isinstance(self.add_date, Unset):
            add_date = self.add_date.isoformat()

        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        body = self.body

        id = self.id

        is_deleted = self.is_deleted

        modified_date: str | Unset
        if isinstance(self.modified_date, Unset):
            modified_date = UNSET
        elif isinstance(self.modified_date, datetime.datetime):
            modified_date = self.modified_date.isoformat()
        else:
            modified_date = self.modified_date

        needs_moderation: int | Unset = UNSET
        if not isinstance(self.needs_moderation, Unset):
            needs_moderation = self.needs_moderation.value

        parent_id = self.parent_id

        parent_url = self.parent_url

        parent_user_name = self.parent_user_name

        url = self.url

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_date is not UNSET:
            field_dict["add_date"] = add_date
        if assets is not UNSET:
            field_dict["assets"] = assets
        if body is not UNSET:
            field_dict["body"] = body
        if id is not UNSET:
            field_dict["id"] = id
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if modified_date is not UNSET:
            field_dict["modified_date"] = modified_date
        if needs_moderation is not UNSET:
            field_dict["needs_moderation"] = needs_moderation
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if parent_url is not UNSET:
            field_dict["parent_url"] = parent_url
        if parent_user_name is not UNSET:
            field_dict["parent_user_name"] = parent_user_name
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_copies_copy_id_threaded_comments_response_200_comments_additional_property_assets_item import (
            GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyAssetsItem,
        )

        d = dict(src_dict)
        _add_date = d.pop("add_date", UNSET)
        add_date: datetime.datetime | Unset
        if isinstance(_add_date, Unset):
            add_date = UNSET
        else:
            add_date = isoparse(_add_date)

        _assets = d.pop("assets", UNSET)
        assets: (
            list[GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyAssetsItem]
            | Unset
        ) = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyAssetsItem.from_dict(
                    assets_item_data
                )

                assets.append(assets_item)

        body = d.pop("body", UNSET)

        id = d.pop("id", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        def _parse_modified_date(data: object) -> datetime.datetime | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_date_type_0 = isoparse(data)

                return modified_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str | Unset, data)

        modified_date = _parse_modified_date(d.pop("modified_date", UNSET))

        _needs_moderation = d.pop("needs_moderation", UNSET)
        needs_moderation: (
            GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyNeedsModeration
            | Unset
        )
        if isinstance(_needs_moderation, Unset):
            needs_moderation = UNSET
        else:
            needs_moderation = (
                GetCopiesCopyIdThreadedCommentsResponse200CommentsAdditionalPropertyNeedsModeration(
                    _needs_moderation
                )
            )

        parent_id = d.pop("parent_id", UNSET)

        parent_url = d.pop("parent_url", UNSET)

        parent_user_name = d.pop("parent_user_name", UNSET)

        url = d.pop("url", UNSET)

        user_id = d.pop("user_id", UNSET)

        get_copies_copy_id_threaded_comments_response_200_comments_additional_property = cls(
            add_date=add_date,
            assets=assets,
            body=body,
            id=id,
            is_deleted=is_deleted,
            modified_date=modified_date,
            needs_moderation=needs_moderation,
            parent_id=parent_id,
            parent_url=parent_url,
            parent_user_name=parent_user_name,
            url=url,
            user_id=user_id,
        )

        get_copies_copy_id_threaded_comments_response_200_comments_additional_property.additional_properties = d
        return get_copies_copy_id_threaded_comments_response_200_comments_additional_property

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
