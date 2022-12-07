from typing import Dict, Any, List
import re
from input import commands


class CommandsResolver:
    def __init__(self, commands: str):
        self.commands: List[str] = commands.split('\n')[1:-1]
        self.file_structure: Dict[Any] = {}
        self._parse_terminal_commands()

    def _parse_terminal_commands(self) -> None:
        current_path: List[str] = []
        for row in self.commands:
            if row[:4] == "$ cd" and row[5:] != "..":
                current_path.append(row[5:])
                while True:
                    if current_path[-1] in self.file_structure:
                        current_path[-1] += '1'
                    else:
                        break
                self.file_structure[current_path[-1]] = {"files": [], "size": 0}
            elif row[:4] == "$ cd" and row[5:] == "..":
                del current_path[-1]
            elif row[0].isdigit():
                file: str = re.findall(r"^(\d+) \w*.\w*$", row)[0]
                self.file_structure[current_path[-1]]['files'].append(file)
                if len(current_path) > 1:
                    for folder in current_path:
                        self.file_structure[folder]['size'] += int(file)
                else:
                    self.file_structure[current_path[-1]]['size'] += int(file)

    def get_total_size_of_dir_below_n(self, n: int) -> int:
        total_size: int = 0
        for key, value in self.file_structure.items():
            if value['size'] < n:
                total_size += value['size']
        return total_size

    def get_smallest_dir_freeing_memory(self) -> int:
        needed_space: int = self.file_structure['/']['size'] - 40000000
        smallest_dir: int = self.file_structure['/']['size']
        for key, value in self.file_structure.items():
            if needed_space <= value['size'] < smallest_dir:
                smallest_dir = value['size']
        return smallest_dir

    def run(self):
        print(self.get_total_size_of_dir_below_n(100000))
        print(self.get_smallest_dir_freeing_memory())


if __name__ == "__main__":
    command_resolver = CommandsResolver(commands=commands)
    command_resolver.run()
