# def backtrack_nqueen(row = 0, count = 0):
#     for col in range(n):
#         # iterate through columns at the curent row.
#         if is_not_under_attack(row, col):
#             # explore this partial candidate solution, and mark the attacking zone
#             place_queen(row, col)
#             if row + 1 == n:
#                 # we reach the bottom, i.e. we find a solution!
#                 count += 1
#             else:
#                 # we move on to the next row
#                 count = backtrack_nqueen(row + 1, count)
#             # backtrack, i.e. remove the queen and remove the attacking zone.
#             remove_queen(row, col)
#     return count

PlacedQueen = tuple[int, int]
AttackZones = list[list[tuple[int, int]]]
PlacedQueenInfo = tuple[PlacedQueen, AttackZones]

class Solution:
    def __init__(self, n: int) -> None:
        self.n = n
        self._board_state: list[list[str]] = [
            "." * n
            for _ in range(0, n)
        ]

        self._placed_queen_states: dict[PlacedQueen, AttackZones] = {}

    def solve_n_queens(self, n: int) -> list[list[str]]:
        # iterate through each ROW of the board
        return self.backtrack_n_queens(row=0, count=0, n=self.n)


    def backtrack_n_queens(self, row: int, count: int, n: int):
        for col in range(n):
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(row, col)
                if (row + 1) == n:
                    # we reach the bottom, i.e. we find a solution!
                    count += 1
                else:
                    # we move on to the next row
                    count = self.backtrack_n_queens(row=row + 1, count=count, n=n)

                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(row, col)

        # end of for-loop -> return tally
        return count

    def is_not_under_attack(self, row: int, col: int) -> bool:
        if (row, col) in self._placed_queen_states:
            return False

        for other_queen_place in self._placed_queen_states.keys():
            # if row == other_queen_row and col == other_queen_col:
            #     return False

            for other_queen_attack_direction in self._placed_queen_states[other_queen_place]:
                for (other_queen_attack_row, other_queen_attack_col) in other_queen_attack_direction:
                    if row == other_queen_attack_row and col == other_queen_attack_col:
                        return False
        return True

    def remove_queen(self, row: int, col: int) -> None:
        del self._placed_queen_states[(row, col)]

    def place_queen(self, row: int, col: int) -> None:
        self._placed_queen_states[(row, col)] = (
            _place_queen_get_new_attack_zones(self.n, row, col)
        )
        # x = 0


def _place_queen_get_new_attack_zones(n: int, row: int, col: int) -> list[list[tuple[int, int]]]:
    return [
        new_attack_zone_callables(n, row, col)
        for new_attack_zone_callables in [
            get_attack_zones_up,
            get_attack_zones_up_and_right,
            get_attack_zones_right,
            get_attack_zones_down_and_right,
            get_attack_zones_down,
            get_attack_zones_down_and_left,
            get_attack_zones_left,
            get_attack_zones_up_and_left,
        ]
    ]



def get_attack_zones_left(n: int, row: int, col: int) -> list[tuple[int, int]]:
    return [
        (row, next_col)
        for next_col in range(col - 1, -1, -1)
    ]


def get_attack_zones_right(n: int, row: int, col: int) -> list[tuple[int, int]]:
    return [
        (row, next_col)
        for next_col in range(col + 1, n)
    ]


def get_attack_zones_up(n: int, row: int, col: int) -> list[tuple[int, int]]:
    return [
        (next_row, col)
        for next_row in range(row - 1, -1, -1)
    ]

def get_attack_zones_down(n: int, row: int, col: int) -> list[tuple[int, int]]:
    return [
        (next_row, col)
        for next_row in range(row + 1, n)
    ]


def get_attack_zones_up_and_left(n: int, row: int, col: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []

    next_row = row - 1
    next_col = col - 1
    while next_row >= 0 and next_col >= 0:
        out.append((next_row, next_col))
        next_row -= 1
        next_col -= 1
    return out


def get_attack_zones_down_and_left(n: int, row: int, col: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []

    next_row = row + 1
    next_col = col - 1
    while next_row < n and next_col >= 0:
        out.append((next_row, next_col))
        next_row += 1
        next_col -= 1
    return out

def get_attack_zones_down_and_right(n: int, row: int, col: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []

    next_row = row + 1
    next_col = col + 1
    while next_row < n and next_col >= 0:
        out.append((next_row, next_col))
        next_row += 1
        next_col += 1
    return out

def get_attack_zones_up_and_right(n: int, row: int, col: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []

    next_row = row - 1
    next_col = col + 1
    while next_row >= 0 and next_col < n:
        out.append((next_row, next_col))
        next_row -= 1
        next_col += 1
    return out


if __name__ == "__main__":
    """
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
    """
    print(Solution(n=4).solve_n_queens(n=4))