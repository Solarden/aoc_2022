from typing import List
from aenum import Enum, MultiValue
from input import rpc_strategy


class RPSDraw(Enum):
    _init_ = "value fullname"
    _settings_ = MultiValue

    ROCK = 1, "A"
    ROCK_X = 1.1, "X"
    PAPER = 2, "B"
    PAPER_Y = 2.1, "Y"
    SCISSORS = 3, "C"
    SCISSORS_Z = 3.1, "Z"

    def __int__(self):
        return self.value


class RPSWinningPoints(Enum):
    _init_ = "value fullname"
    _settings_ = MultiValue

    LOST = 0, "X"
    DRAW = 3, "Y"
    WIN = 6, "Z"

    def __int__(self):
        return self.value


class RPSStrategyResolver:
    def __init__(self, strategy: str):
        self.strategy: List[str] = strategy.split("\n")[1:-1]
        self.parsed_strategy: List[List[RPSDraw]] = [[RPSDraw(row[0]), RPSDraw(row[-1])] for row in self.strategy]
        self.parsed_grand_strategy: List[List[RPSDraw, RPSWinningPoints]] = [
            [RPSDraw(row[0]), RPSWinningPoints(row[-1])] for row in self.strategy
        ]
        self.total_points: int = 0

    @staticmethod
    def _rps_match_resolver(user_draw: int, opponent_draw: int) -> int:
        if user_draw == 1 and opponent_draw == 3:
            return user_draw
        elif user_draw == 2 and opponent_draw == 1:
            return user_draw
        elif user_draw == 3 and opponent_draw == 2:
            return user_draw
        else:
            return 0

    def resolve_strategy(self) -> int:
        self.total_points = 0
        for opponent_draw, user_draw in self.parsed_strategy:
            if int(user_draw.value) == opponent_draw.value:
                self.total_points += 3 + opponent_draw.value
            else:
                match_result: int = self._rps_match_resolver(int(user_draw.value), opponent_draw.value)
                if match_result > 0:
                    self.total_points += 6 + match_result
                else:
                    self.total_points += int(user_draw.value)
        return self.total_points

    @staticmethod
    def _rps_winning_draw(opponent_draw: RPSDraw) -> int:
        if opponent_draw == RPSDraw.ROCK:
            return int(RPSDraw.PAPER)
        elif opponent_draw == RPSDraw.PAPER:
            return int(RPSDraw.SCISSORS)
        elif opponent_draw == RPSDraw.SCISSORS:
            return int(RPSDraw.ROCK)

    @staticmethod
    def _rps_losing_draw(opponent_draw: RPSDraw) -> int:
        if opponent_draw == RPSDraw.ROCK:
            return int(RPSDraw.SCISSORS)
        elif opponent_draw == RPSDraw.PAPER:
            return int(RPSDraw.ROCK)
        elif opponent_draw == RPSDraw.SCISSORS:
            return int(RPSDraw.PAPER)

    def resolve_grand_strategy(self) -> int:
        self.total_points = 0
        for opponent_draw, match_result in self.parsed_grand_strategy:
            if match_result == RPSWinningPoints.DRAW:
                self.total_points += 3 + opponent_draw.value
            elif match_result == RPSWinningPoints.WIN:
                self.total_points += 6 + self._rps_winning_draw(opponent_draw)
            elif match_result == RPSWinningPoints.LOST:
                self.total_points += self._rps_losing_draw(opponent_draw)
        return self.total_points


if __name__ == "__main__":
    rpc_resolver = RPSStrategyResolver(strategy=rpc_strategy)
    print(rpc_resolver.resolve_strategy())
    print(rpc_resolver.resolve_grand_strategy())
