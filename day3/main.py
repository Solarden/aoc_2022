from string import ascii_letters
from typing import List, Tuple, Dict, Union

from input import elvish_rucksack


def divide_chunks(l: list, n: int) -> list:
    for i in range(0, len(l), n):
        yield l[i:i + n]


class RucksackOrganizer:
    def __init__(self, elvish_rucksack: str):
        self.elvish_rucksack: List[str] = elvish_rucksack.split("\n")[1:-1]
        self.split_rucksacks: Tuple[Tuple[str]] = ()
        self.reappearing_items = []
        self.item_priority: Dict[str, int] = {}
        self.elvish_group_badges: List[str] = []
        self._set_rucksack_item_priority()
        self._split_rucksack_for_two_compartments()
        self._find_reappearing_items_of_given(self.split_rucksacks, "items")
        self._find_reappearing_items_of_given(list(divide_chunks(self.elvish_rucksack, 3)), "badges")

    def _set_rucksack_item_priority(self) -> None:
        for index, letter in enumerate(ascii_letters):
            self.item_priority[letter] = index + 1

    def _split_rucksack_for_two_compartments(self) -> None:
        for rucksack in self.elvish_rucksack:
            self.split_rucksacks += ((rucksack[:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):]),)

    def _find_reappearing_items_of_given(self, given_list: Union[List, Tuple], reappearing_type: str) -> None:
        for i in given_list:
            for v in i[0]:
                if reappearing_type == "items" and v in i[1]:
                    self.reappearing_items.append(v)
                    break
                elif reappearing_type == "badges" and v in i[1] and v in i[2]:
                    self.elvish_group_badges.append(v)
                    break

    def _get_priority_sum_of_given(self, given_list: List) -> int:
        priority_sum: int = 0
        for item in given_list:
            priority_sum += self.item_priority[item]
        return priority_sum

    def get_priority_sum_of_reappearing_items(self) -> int:
        return self._get_priority_sum_of_given(self.reappearing_items)

    def get_priority_sum_of_elvish_badges(self) -> int:
        return self._get_priority_sum_of_given(self.elvish_group_badges)


if __name__ == "__main__":
    rucksack_organizer = RucksackOrganizer(elvish_rucksack=elvish_rucksack)
    print(rucksack_organizer.get_priority_sum_of_reappearing_items())
    print(rucksack_organizer.get_priority_sum_of_elvish_badges())
