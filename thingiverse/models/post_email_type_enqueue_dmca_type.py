from enum import Enum


class PostEmailTypeEnqueueDmcaType(str, Enum):
    COPYRIGHT = "copyright"
    IP = "ip"

    def __str__(self) -> str:
        return str(self.value)
