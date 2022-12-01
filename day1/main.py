from typing import List, Dict, Union

from input import list_of_elvish_calories


class ElvishCaloriesList:
    def __init__(self, elvish_list: str):
        self.elvish_list: List[str] = elvish_list.split("\n")
        self.elf_counter: int = 1
        self.elvish_calories_dict: Dict[Union[str, Dict[str, List[str], str, int]]] = {}
        self.most_calories: int = 0
        self.elf_with_most_calories: str = ""
        self.list_of_most_calories: List[int] = []

    def _create_dict_of_elvish_list(self) -> None:
        for row in self.elvish_list:
            if row == "":
                self.elvish_calories_dict[f"elf_{self.elf_counter}"] = {"calories_list": [], "total_calories": 0}
                self.elf_counter += 1
                continue
        self.elf_counter = 1

    def _populate_dict_of_elvish_data(self) -> None:
        for row in self.elvish_list[1:]:
            if row == "":
                self.elf_counter += 1
                continue

            self.elvish_calories_dict[f"elf_{self.elf_counter}"]["calories_list"].append(row)
            self.elvish_calories_dict[f"elf_{self.elf_counter}"]["total_calories"] += int(row)

    def get_elf_with_most_calories(self) -> str:
        self._create_dict_of_elvish_list()
        self._populate_dict_of_elvish_data()
        for elf, elf_list in self.elvish_calories_dict.items():
            self.list_of_most_calories.append(elf_list["total_calories"])
            if elf_list["total_calories"] > self.most_calories:
                self.most_calories = elf_list["total_calories"]
                self.elf_with_most_calories = elf

        return f"{self.elf_with_most_calories} - {self.most_calories}"

    def get_sum_of_top_three_elf_calories(self) -> int:
        return sum(sorted(self.list_of_most_calories)[-3:])


if __name__ == "__main__":
    elvish_calories = ElvishCaloriesList(elvish_list=list_of_elvish_calories)
    print(elvish_calories.get_elf_with_most_calories())
    print(elvish_calories.get_sum_of_top_three_elf_calories())
