from enum import Enum


class GetSubscriptions0DashboardType(str, Enum):
    ALL_ACTIVITY = "all-activity"
    FRIENDS_ACTIVITY = "friends-activity"
    MY_ACTIVITY = "my-activity"
    WATCHLIST = "watchlist"

    def __str__(self) -> str:
        return str(self.value)
