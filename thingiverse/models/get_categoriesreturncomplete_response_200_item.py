from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_categoriesreturncomplete_response_200_item_children_item import (
        GetCategoriesreturncompleteResponse200ItemChildrenItem,
    )


T = TypeVar("T", bound="GetCategoriesreturncompleteResponse200Item")


@_attrs_define
class GetCategoriesreturncompleteResponse200Item:
    """
    Attributes:
        children (list[GetCategoriesreturncompleteResponse200ItemChildrenItem] | Unset):
        name (str | Unset):
        url (str | Unset):
    """

    children: list[GetCategoriesreturncompleteResponse200ItemChildrenItem] | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_categoriesreturncomplete_response_200_item_children_item import (
            GetCategoriesreturncompleteResponse200ItemChildrenItem,
        )

        d = dict(src_dict)
        _children = d.pop("children", UNSET)
        children: list[GetCategoriesreturncompleteResponse200ItemChildrenItem] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = GetCategoriesreturncompleteResponse200ItemChildrenItem.from_dict(
                    children_item_data
                )

                children.append(children_item)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        get_categoriesreturncomplete_response_200_item = cls(
            children=children,
            name=name,
            url=url,
        )

        get_categoriesreturncomplete_response_200_item.additional_properties = d
        return get_categoriesreturncomplete_response_200_item

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
