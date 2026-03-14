from enum import Enum


class CommentSchemaTargetType(str, Enum):
    APP = "app"
    GROUPTOPIC = "grouptopic"
    MAKE = "make"
    MESSAGE = "message"
    THING = "thing"

    def __str__(self) -> str:
        return str(self.value)
