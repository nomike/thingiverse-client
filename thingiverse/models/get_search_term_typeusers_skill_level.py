from enum import Enum


class GetSearchTermTypeusersSkillLevel(str, Enum):
    ADVANCED = "Advanced"
    INTERMEDIATE = "Intermediate"
    NOVICE = "Novice"

    def __str__(self) -> str:
        return str(self.value)
