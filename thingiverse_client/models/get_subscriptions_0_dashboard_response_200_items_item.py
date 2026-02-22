from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_schema import CategorySchema
    from ..models.comment_schema import CommentSchema
    from ..models.copy_schema import CopySchema
    from ..models.get_subscriptions_0_dashboard_response_200_items_item_image import (
        GetSubscriptions0DashboardResponse200ItemsItemImage,
    )
    from ..models.thing_schema import ThingSchema
    from ..models.user_schema import UserSchema


T = TypeVar("T", bound="GetSubscriptions0DashboardResponse200ItemsItem")


@_attrs_define
class GetSubscriptions0DashboardResponse200ItemsItem:
    """
    Attributes:
        content (CategorySchema | CommentSchema | CopySchema | ThingSchema | Unset):
        id (int | Unset):
        image (GetSubscriptions0DashboardResponse200ItemsItemImage | Unset):
        is_personal (bool | Unset):
        is_subscribed (bool | Unset):
        message (str | Unset):
        time (str | Unset):
        type_ (str | Unset):
        user (UserSchema | Unset):
    """

    content: CategorySchema | CommentSchema | CopySchema | ThingSchema | Unset = UNSET
    id: int | Unset = UNSET
    image: GetSubscriptions0DashboardResponse200ItemsItemImage | Unset = UNSET
    is_personal: bool | Unset = UNSET
    is_subscribed: bool | Unset = UNSET
    message: str | Unset = UNSET
    time: str | Unset = UNSET
    type_: str | Unset = UNSET
    user: UserSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.comment_schema import CommentSchema
        from ..models.copy_schema import CopySchema
        from ..models.thing_schema import ThingSchema

        content: dict[str, Any] | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif (
            isinstance(self.content, ThingSchema)
            or isinstance(self.content, CopySchema)
            or isinstance(self.content, CommentSchema)
        ):
            content = self.content.to_dict()
        else:
            content = self.content.to_dict()

        id = self.id

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        is_personal = self.is_personal

        is_subscribed = self.is_subscribed

        message = self.message

        time = self.time

        type_ = self.type_

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if is_personal is not UNSET:
            field_dict["is_personal"] = is_personal
        if is_subscribed is not UNSET:
            field_dict["is_subscribed"] = is_subscribed
        if message is not UNSET:
            field_dict["message"] = message
        if time is not UNSET:
            field_dict["time"] = time
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_schema import CategorySchema
        from ..models.comment_schema import CommentSchema
        from ..models.copy_schema import CopySchema
        from ..models.get_subscriptions_0_dashboard_response_200_items_item_image import (
            GetSubscriptions0DashboardResponse200ItemsItemImage,
        )
        from ..models.thing_schema import ThingSchema
        from ..models.user_schema import UserSchema

        d = dict(src_dict)

        def _parse_content(
            data: object,
        ) -> CategorySchema | CommentSchema | CopySchema | ThingSchema | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = ThingSchema.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = CopySchema.from_dict(data)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_2 = CommentSchema.from_dict(data)

                return content_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            content_type_3 = CategorySchema.from_dict(data)

            return content_type_3

        content = _parse_content(d.pop("content", UNSET))

        id = d.pop("id", UNSET)

        _image = d.pop("image", UNSET)
        image: GetSubscriptions0DashboardResponse200ItemsItemImage | Unset
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = GetSubscriptions0DashboardResponse200ItemsItemImage.from_dict(_image)

        is_personal = d.pop("is_personal", UNSET)

        is_subscribed = d.pop("is_subscribed", UNSET)

        message = d.pop("message", UNSET)

        time = d.pop("time", UNSET)

        type_ = d.pop("type", UNSET)

        _user = d.pop("user", UNSET)
        user: UserSchema | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserSchema.from_dict(_user)

        get_subscriptions_0_dashboard_response_200_items_item = cls(
            content=content,
            id=id,
            image=image,
            is_personal=is_personal,
            is_subscribed=is_subscribed,
            message=message,
            time=time,
            type_=type_,
            user=user,
        )

        get_subscriptions_0_dashboard_response_200_items_item.additional_properties = d
        return get_subscriptions_0_dashboard_response_200_items_item

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
