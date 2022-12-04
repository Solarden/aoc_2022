import re
from typing import List, Tuple

from input import elvish_assignments


class ElvishAssignmentResolver:
    def __init__(self, elvish_assignments: str):
        self.elvish_assignments: List[List[str]] = [re.split(",|-", i) for i in elvish_assignments.split("\n")[1:-1]]

    @staticmethod
    def _parse_elvish_assignments(assignments: List[str]) -> Tuple[List[int], List[int]]:
        return [i for i in range(int(assignments[0]), int(assignments[1]) + 1)], [
            i for i in range(int(assignments[2]), int(assignments[3]) + 1)
        ]

    def get_overlapping_assignments(self) -> Tuple[int, int]:
        fully_overlapping_pairs: int = 0
        overlapping_pairs: int = 0

        for assignment in self.elvish_assignments:
            first_assignment, second_assignment = self._parse_elvish_assignments(assignment)
            if set(first_assignment).issubset(set(second_assignment)) or set(second_assignment).issubset(
                set(first_assignment)
            ):
                fully_overlapping_pairs += 1
            if len(set(first_assignment).intersection(second_assignment)) > 0:
                overlapping_pairs += 1
        return fully_overlapping_pairs, overlapping_pairs


if __name__ == "__main__":
    assigment_resolver = ElvishAssignmentResolver(elvish_assignments=elvish_assignments)
    print(assigment_resolver.get_overlapping_assignments())
