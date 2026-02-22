from enum import Enum


class GetBannerLocation(str, Enum):
    DOWNLOAD = "download"
    EXPLORE = "explore"
    HOME = "home"
    MAKE = "make"
    SEARCH = "search"
    THING = "thing"
    USER_PROFILE = "user_profile"

    def __str__(self) -> str:
        return str(self.value)
