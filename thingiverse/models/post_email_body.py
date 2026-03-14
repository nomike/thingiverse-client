from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_email_body_email_type import PostEmailBodyEmailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostEmailBody")


@_attrs_define
class PostEmailBody:
    """
    Attributes:
        email_type (PostEmailBodyEmailType): Set the type of email
        site (str): Set the parameter of site. Site parameter's value should be either 'tv' or 'mb' Example: tv.
        user_id (int): Set the ID of the user who will receive the email Example: 2.
        client_id (str | Unset): Set the client ID of app Example: 615fc4464de0c742cafb.
        forgot_email (str | Unset): Set the forgotten email. In this case, set the email type as a forgot Example:
            test@gmail.com.
    """

    email_type: PostEmailBodyEmailType
    site: str
    user_id: int
    client_id: str | Unset = UNSET
    forgot_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_type = self.email_type.value

        site = self.site

        user_id = self.user_id

        client_id = self.client_id

        forgot_email = self.forgot_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_type": email_type,
                "site": site,
                "user_id": user_id,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if forgot_email is not UNSET:
            field_dict["forgot_email"] = forgot_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_type = PostEmailBodyEmailType(d.pop("email_type"))

        site = d.pop("site")

        user_id = d.pop("user_id")

        client_id = d.pop("client_id", UNSET)

        forgot_email = d.pop("forgot_email", UNSET)

        post_email_body = cls(
            email_type=email_type,
            site=site,
            user_id=user_id,
            client_id=client_id,
            forgot_email=forgot_email,
        )

        post_email_body.additional_properties = d
        return post_email_body

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
