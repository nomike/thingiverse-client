from enum import Enum


class PostThingsBodyLicense(str, Enum):
    BSD = "bsd"
    CC = "cc"
    CC_NC_ND = "cc-nc-nd"
    CC_NC_SA = "cc-nc-sa"
    CC_ND = "cc-nd"
    CC_SA = "cc-sa"
    GPL = "gpl"
    LGPL = "lgpl"
    PD0 = "pd0"

    def __str__(self) -> str:
        return str(self.value)
