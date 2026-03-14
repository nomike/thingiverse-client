from enum import Enum


class GetSearchTermTypethingsSort(str, Enum):
    MAKES = "makes"
    NEWEST = "newest"
    POPULAR = "popular"
    RELEVANT = "relevant"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
