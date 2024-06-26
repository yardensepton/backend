from typing import List

from src.models.item import Item
from src.filter_pattern.filter import Filter


class GenderFilter(Filter):
    def __init__(self, gender):
        self.gender = gender

    def apply(self, items: List[Item]) -> List[Item]:
        return [item for item in items if item.gender == self.gender or item.gender == "all"]
