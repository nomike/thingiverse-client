from enum import Enum


class GetSearchTermTypeusersSort(str, Enum):
    DESIGNS = "designs"
    FOLLOWERS = "followers"
    MAKES = "makes"
    RELEVANT = "relevant"

    def __str__(self) -> str:
        return str(self.value)
