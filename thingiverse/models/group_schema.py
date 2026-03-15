from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_schema_featured_images_item import GroupSchemaFeaturedImagesItem
    from ..models.group_schema_featured_item import GroupSchemaFeaturedItem
    from ..models.group_schema_group_topics import GroupSchemaGroupTopics
    from ..models.group_schema_members import GroupSchemaMembers
    from ..models.group_schema_things import GroupSchemaThings


T = TypeVar("T", bound="GroupSchema")


@_attrs_define
class GroupSchema:
    """
    Attributes:
        id (int):
        creator (int | Unset):
        description (str | Unset):
        featured (list[GroupSchemaFeaturedItem] | Unset):
        featured_images (list[GroupSchemaFeaturedImagesItem] | Unset):
        group_topics (GroupSchemaGroupTopics | Unset):
        image (str | Unset):
        is_member (bool | Unset):
        members (GroupSchemaMembers | Unset):
        name (str | Unset):
        pinned_topics (int | Unset):
        public_url (str | Unset):
        slug (str | Unset):
        things (GroupSchemaThings | Unset):
        url (str | Unset):
    """

    id: int
    creator: int | Unset = UNSET
    description: str | Unset = UNSET
    featured: list[GroupSchemaFeaturedItem] | Unset = UNSET
    featured_images: list[GroupSchemaFeaturedImagesItem] | Unset = UNSET
    group_topics: GroupSchemaGroupTopics | Unset = UNSET
    image: str | Unset = UNSET
    is_member: bool | Unset = UNSET
    members: GroupSchemaMembers | Unset = UNSET
    name: str | Unset = UNSET
    pinned_topics: int | Unset = UNSET
    public_url: str | Unset = UNSET
    slug: str | Unset = UNSET
    things: GroupSchemaThings | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        creator = self.creator

        description = self.description

        featured: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.featured, Unset):
            featured = []
            for featured_item_data in self.featured:
                featured_item = featured_item_data.to_dict()
                featured.append(featured_item)

        featured_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.featured_images, Unset):
            featured_images = []
            for featured_images_item_data in self.featured_images:
                featured_images_item = featured_images_item_data.to_dict()
                featured_images.append(featured_images_item)

        group_topics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_topics, Unset):
            group_topics = self.group_topics.to_dict()

        image = self.image

        is_member = self.is_member

        members: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        name = self.name

        pinned_topics = self.pinned_topics

        public_url = self.public_url

        slug = self.slug

        things: dict[str, Any] | Unset = UNSET
        if not isinstance(self.things, Unset):
            things = self.things.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if featured is not UNSET:
            field_dict["featured"] = featured
        if featured_images is not UNSET:
            field_dict["featured_images"] = featured_images
        if group_topics is not UNSET:
            field_dict["group_topics"] = group_topics
        if image is not UNSET:
            field_dict["image"] = image
        if is_member is not UNSET:
            field_dict["is_member"] = is_member
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name
        if pinned_topics is not UNSET:
            field_dict["pinnedTopics"] = pinned_topics
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if slug is not UNSET:
            field_dict["slug"] = slug
        if things is not UNSET:
            field_dict["things"] = things
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_schema_featured_images_item import GroupSchemaFeaturedImagesItem
        from ..models.group_schema_featured_item import GroupSchemaFeaturedItem
        from ..models.group_schema_group_topics import GroupSchemaGroupTopics
        from ..models.group_schema_members import GroupSchemaMembers
        from ..models.group_schema_things import GroupSchemaThings

        d = dict(src_dict)
        id = d.pop("id")

        creator = d.pop("creator", UNSET)

        description = d.pop("description", UNSET)

        _featured = d.pop("featured", UNSET)
        featured: list[GroupSchemaFeaturedItem] | Unset = UNSET
        if _featured is not UNSET:
            featured = []
            for featured_item_data in _featured:
                featured_item = GroupSchemaFeaturedItem.from_dict(featured_item_data)

                featured.append(featured_item)

        _featured_images = d.pop("featured_images", UNSET)
        featured_images: list[GroupSchemaFeaturedImagesItem] | Unset = UNSET
        if _featured_images is not UNSET:
            featured_images = []
            for featured_images_item_data in _featured_images:
                featured_images_item = GroupSchemaFeaturedImagesItem.from_dict(
                    featured_images_item_data
                )

                featured_images.append(featured_images_item)

        _group_topics = d.pop("group_topics", UNSET)
        group_topics: GroupSchemaGroupTopics | Unset
        if isinstance(_group_topics, Unset):
            group_topics = UNSET
        else:
            group_topics = GroupSchemaGroupTopics.from_dict(_group_topics)

        image = d.pop("image", UNSET)

        is_member = d.pop("is_member", UNSET)

        _members = d.pop("members", UNSET)
        members: GroupSchemaMembers | Unset
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = GroupSchemaMembers.from_dict(_members)

        name = d.pop("name", UNSET)

        pinned_topics = d.pop("pinnedTopics", UNSET)

        public_url = d.pop("public_url", UNSET)

        slug = d.pop("slug", UNSET)

        _things = d.pop("things", UNSET)
        things: GroupSchemaThings | Unset
        if isinstance(_things, Unset):
            things = UNSET
        else:
            things = GroupSchemaThings.from_dict(_things)

        url = d.pop("url", UNSET)

        group_schema = cls(
            id=id,
            creator=creator,
            description=description,
            featured=featured,
            featured_images=featured_images,
            group_topics=group_topics,
            image=image,
            is_member=is_member,
            members=members,
            name=name,
            pinned_topics=pinned_topics,
            public_url=public_url,
            slug=slug,
            things=things,
            url=url,
        )

        group_schema.additional_properties = d
        return group_schema

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
