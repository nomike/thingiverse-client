from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.program_schema import ProgramSchema


T = TypeVar("T", bound="GetPrograms0AllResponse200")


@_attrs_define
class GetPrograms0AllResponse200:
    """
    Attributes:
        count (int | Unset):
        programs (list[ProgramSchema] | Unset):
    """

    count: int | Unset = UNSET
    programs: list[ProgramSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        programs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.programs, Unset):
            programs = []
            for programs_item_data in self.programs:
                programs_item = programs_item_data.to_dict()
                programs.append(programs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if programs is not UNSET:
            field_dict["programs"] = programs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.program_schema import ProgramSchema

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _programs = d.pop("programs", UNSET)
        programs: list[ProgramSchema] | Unset = UNSET
        if _programs is not UNSET:
            programs = []
            for programs_item_data in _programs:
                programs_item = ProgramSchema.from_dict(programs_item_data)

                programs.append(programs_item)

        get_programs_0_all_response_200 = cls(
            count=count,
            programs=programs,
        )

        get_programs_0_all_response_200.additional_properties = d
        return get_programs_0_all_response_200

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
