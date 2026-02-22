from enum import Enum


class GetBanner0PageAdType(str, Enum):
    AD_CARD_REPLACEMENT = "Ad card replacement"
    AMAZON_PROGRAM = "Amazon Program"
    LINK_GENERATOR = "Link Generator"
    MANAGE_PRINTERS = "Manage Printers"
    REMOVE_ALL_ADS = "Remove All Ads"

    def __str__(self) -> str:
        return str(self.value)
