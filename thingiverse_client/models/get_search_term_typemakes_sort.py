from enum import Enum


class GetSearchTermTypemakesSort(str, Enum):
    NEWEST = "newest"
    POPULAR = "popular"
    RELEVANT = "relevant"

    def __str__(self) -> str:
        return str(self.value)
