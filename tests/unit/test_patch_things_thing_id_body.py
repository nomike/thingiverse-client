"""Unit tests for PatchThingsThingIdBody (tags/ancestors as primitive arrays)."""

import pytest

from thingiverse.models import PatchThingsThingIdBody


def test_from_dict_accepts_tags_as_list_of_strings() -> None:
    """tags is deserialized as list[str], not list of objects."""
    body = PatchThingsThingIdBody.from_dict({
        "name": "My thing",
        "tags": ["foo", "bar", "baz"],
    })
    assert body.tags == ["foo", "bar", "baz"]


def test_from_dict_accepts_ancestors_as_list_of_ints() -> None:
    """ancestors is deserialized as list[int], not list of objects."""
    body = PatchThingsThingIdBody.from_dict({
        "name": "My thing",
        "ancestors": [2000, 2001],
    })
    assert body.ancestors == [2000, 2001]


def test_from_dict_tags_and_ancestors_roundtrip() -> None:
    """from_dict then to_dict preserves tags and ancestors as primitives."""
    data = {
        "name": "My thing",
        "tags": ["a", "b"],
        "ancestors": [100, 200],
    }
    body = PatchThingsThingIdBody.from_dict(data)
    out = body.to_dict()
    assert out["tags"] == ["a", "b"]
    assert out["ancestors"] == [100, 200]
