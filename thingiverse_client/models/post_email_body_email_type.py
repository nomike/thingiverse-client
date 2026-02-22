from enum import Enum


class PostEmailBodyEmailType(str, Enum):
    FORGOT = "forgot"
    VERIFICATION = "verification"
    WELCOME = "welcome"

    def __str__(self) -> str:
        return str(self.value)
