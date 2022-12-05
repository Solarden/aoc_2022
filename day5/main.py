from typing import List, Dict
import re
from input import crane_operations
from test_input import test_crane_operations


class CraneOperationsResolver:
    def __init__(self, crane_operations: str):
        self.crane_operations: List[str] = crane_operations.split("\n")[1:-1]
        self.stack_visualization: List[str] = []
        self.parsed_stack_visualization: Dict[str, List[str]] = {}

    def _parse_crane_operation(self) -> None:
        for index, value in enumerate(self.crane_operations):
            if value == "":
                self.crane_operations = self.crane_operations[index + 1:]
                break
            self.stack_visualization.append(value)

    def _parse_stack_visualization(self) -> None:
        self._parse_crane_operation()
        self.parsed_stack_visualization = {}
        parsed_row: List[List[str]] = []
        for row in self.stack_visualization:
            crates_in_row: List[str] = []
            for index, crate in enumerate(row):
                if index % 4 == 0:
                    crates_in_row.append(row[index:index + 3])
            parsed_row.append(crates_in_row)
        self.stack_visualization = parsed_row[:-1]
        for i in range(0, len(crates_in_row)):
            self.parsed_stack_visualization[f"{i + 1}"] = []
        for row in self.stack_visualization:
            for index, column in enumerate(row):
                if column[0] == "[":
                    self.parsed_stack_visualization[f"{index + 1}"].insert(0, column[1])

    def get_top_crates(self) -> str:
        self._parse_stack_visualization()
        top_crates: str = ""
        for operation in self.crane_operations:
            operation = re.match(r"^move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)$", operation).groupdict()
            for _ in range(1, int(operation['move']) + 1):
                self.parsed_stack_visualization[operation["to"]].append(
                    self.parsed_stack_visualization[operation["from"]][-1])
                del self.parsed_stack_visualization[operation["from"]][-1]
        for _, value in self.parsed_stack_visualization.items():
            top_crates += value[-1]
        return top_crates

    def get_top_crates_of_crate_mover_9001(self) -> str:
        self._parse_stack_visualization()
        top_crates: str = ""
        for operation in self.crane_operations:
            operation = re.match(r"^move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)$", operation).groupdict()
            self.parsed_stack_visualization[operation["to"]].extend(
                self.parsed_stack_visualization[operation["from"]][-int(operation["move"]):])
            del self.parsed_stack_visualization[operation["from"]][-int(operation["move"]):]
        for _, value in self.parsed_stack_visualization.items():
            top_crates += value[-1]
        return top_crates


if __name__ == "__main__":
    operations = CraneOperationsResolver(crane_operations=crane_operations)
    # print(operations.get_top_crates())
    print(operations.get_top_crates_of_crate_mover_9001())
