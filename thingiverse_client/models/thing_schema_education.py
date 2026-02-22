from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thing_schema_education_grades_item import ThingSchemaEducationGradesItem
    from ..models.thing_schema_education_subjects_item import ThingSchemaEducationSubjectsItem


T = TypeVar("T", bound="ThingSchemaEducation")


@_attrs_define
class ThingSchemaEducation:
    """
    Attributes:
        grades (list[ThingSchemaEducationGradesItem] | Unset):
        subjects (list[ThingSchemaEducationSubjectsItem] | Unset):
    """

    grades: list[ThingSchemaEducationGradesItem] | Unset = UNSET
    subjects: list[ThingSchemaEducationSubjectsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grades: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grades, Unset):
            grades = []
            for grades_item_data in self.grades:
                grades_item = grades_item_data.to_dict()
                grades.append(grades_item)

        subjects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subjects, Unset):
            subjects = []
            for subjects_item_data in self.subjects:
                subjects_item = subjects_item_data.to_dict()
                subjects.append(subjects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grades is not UNSET:
            field_dict["grades"] = grades
        if subjects is not UNSET:
            field_dict["subjects"] = subjects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thing_schema_education_grades_item import ThingSchemaEducationGradesItem
        from ..models.thing_schema_education_subjects_item import ThingSchemaEducationSubjectsItem

        d = dict(src_dict)
        _grades = d.pop("grades", UNSET)
        grades: list[ThingSchemaEducationGradesItem] | Unset = UNSET
        if _grades is not UNSET:
            grades = []
            for grades_item_data in _grades:
                grades_item = ThingSchemaEducationGradesItem.from_dict(grades_item_data)

                grades.append(grades_item)

        _subjects = d.pop("subjects", UNSET)
        subjects: list[ThingSchemaEducationSubjectsItem] | Unset = UNSET
        if _subjects is not UNSET:
            subjects = []
            for subjects_item_data in _subjects:
                subjects_item = ThingSchemaEducationSubjectsItem.from_dict(subjects_item_data)

                subjects.append(subjects_item)

        thing_schema_education = cls(
            grades=grades,
            subjects=subjects,
        )

        thing_schema_education.additional_properties = d
        return thing_schema_education

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
