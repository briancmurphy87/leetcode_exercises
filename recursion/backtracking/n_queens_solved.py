class Solution:

    def solve_n_queens_impl(self, n: int) -> list[list[str]]:
        output = []
        cols: set[int] = set()
        diagonals: set[int] = set()
        anti_diagonals: set[int] = set()

        backtrack(
            n=n,
            row=0,
            cols=cols,
            diagonals=diagonals,
            anti_diagonals=anti_diagonals,
            state=[["."] * n for _ in range(n)], # empty board
            output=output,
        )
        return output


def backtrack(
        n: int,
        row: int,
        cols: set[int],
        diagonals: set[int],
        anti_diagonals: set[int],
        state: list[list[str]],
        output: list,
) -> None:
    # Base case - N queens have been placed
    if row == n:
        output.append(create_board(state))
        return

    for col in range(n):
        curr_diagonal = row - col
        curr_anti_diagonal = row + col
        # If the queen is not placeable
        if (
                col in cols
                or curr_diagonal in diagonals
                or curr_anti_diagonal in anti_diagonals
        ):
            continue

        # "Add" the queen to the board
        cols.add(col)
        diagonals.add(curr_diagonal)
        anti_diagonals.add(curr_anti_diagonal)
        state[row][col] = "Q"

        # Move on to the next row with the updated board state
        # backtrack(row + 1, diagonals, anti_diagonals, cols, state)
        backtrack(
            n=n,
            row=row + 1,
            cols=cols,
            diagonals=diagonals,
            anti_diagonals=anti_diagonals,
            state=state,
            output=output,
        )

        # "Remove" the queen from the board since we have already
        # explored all valid paths using the above function call
        cols.remove(col)
        diagonals.remove(curr_diagonal)
        anti_diagonals.remove(curr_anti_diagonal)
        state[row][col] = "."

    x = 0

def create_board(state: list[list[str]]) -> list[str]:
    return [
        "".join(row)
        for row in state
    ]
    # for row in state:
    #     board.append("".join(row))
    # return board


if __name__ == "__main__":
    """
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
    """
    print(Solution().solve_n_queens_impl(n=4))
