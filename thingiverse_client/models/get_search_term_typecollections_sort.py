from enum import Enum


class GetSearchTermTypecollectionsSort(str, Enum):
    NEWEST = "newest"
    POPULAR = "popular"
    RELEVANT = "relevant"
    THINGS = "things"

    def __str__(self) -> str:
        return str(self.value)
