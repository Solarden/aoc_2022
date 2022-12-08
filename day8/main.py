from typing import List

from input import tree_map


class TreeMapAnalyzer:
    def __init__(self, tree_map: str):
        self.tree_map: List[List[int]] = [[int(tree) for tree in row] for row in tree_map.split("\n")[1:-1]]

    def get_visible_trees(self) -> int:
        visible_trees: int = (len(self.tree_map[0]) * 2) + (len(self.tree_map) * 2) - 4
        for r_index, row in enumerate(self.tree_map[1:-1]):
            for c_index, tree in enumerate(row[1:-1]):
                if max(self.tree_map[r_index + 1][c_index + 2:]) < tree:
                    visible_trees += 1
                elif max(self.tree_map[r_index + 1][: c_index + 1]) < tree:
                    visible_trees += 1
                elif max([row[c_index + 1] for row in self.tree_map[: r_index + 1]]) < tree:
                    visible_trees += 1
                elif max([row[c_index + 1] for row in self.tree_map[r_index + 2:]]) < tree:
                    visible_trees += 1
        return visible_trees

    @staticmethod
    def _count_tree_scenic_score(tree_list: List[int], current_tree: int) -> int:
        tree_score: int = 0
        for index, next_tree in enumerate(tree_list):
            if index == 0 and next_tree >= current_tree:
                tree_score = 1
                break
            elif next_tree < current_tree:
                tree_score += 1
            elif next_tree >= current_tree:
                tree_score += 1
                break
        return tree_score

    def get_best_scenic_tree(self) -> int:
        best_scenic_score: int = 0
        for r_index, row in enumerate(self.tree_map[1:-1]):
            for c_index, tree in enumerate(row[1:-1]):
                right_tree: int = self._count_tree_scenic_score(self.tree_map[r_index + 1][c_index + 2:], tree)
                left_tree: int = self._count_tree_scenic_score(
                    list(reversed(self.tree_map[r_index + 1][: c_index + 1])), tree
                )
                top_tree: int = self._count_tree_scenic_score(
                    list(reversed([row[c_index + 1] for row in self.tree_map[: r_index + 1]])), tree
                )
                bottom_tree: int = self._count_tree_scenic_score(
                    [row[c_index + 1] for row in self.tree_map[r_index + 2:]], tree
                )
                scenic_score: int = right_tree * left_tree * top_tree * bottom_tree
                if scenic_score > best_scenic_score:
                    best_scenic_score = scenic_score
        return best_scenic_score


if __name__ == "__main__":
    map_analyzer = TreeMapAnalyzer(tree_map=tree_map)
    print(map_analyzer.get_visible_trees())
    print(map_analyzer.get_best_scenic_tree())
