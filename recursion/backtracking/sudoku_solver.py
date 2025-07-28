from collections import defaultdict

SUB_BOX_DIM = 3
SUB_BOX_ELEMENT_COUNT = SUB_BOX_DIM * SUB_BOX_DIM


class Solution:
    def solveSudoku(self, board):
        return solve_sudoku(board)

def box_index(row: int, col: int) -> int:
    return (row // SUB_BOX_DIM) * SUB_BOX_DIM + col // SUB_BOX_DIM

def place_number(
        d: int,
        row: int,
        col: int,
        rows: list[defaultdict[int, int]],
        cols: list[defaultdict[int, int]],
        boxes: list[defaultdict[int, int]],
        board: list[list[str]]) -> None:
        """
        Place a number d in (row, col) cell
        """
        rows[row][d] += 1
        cols[col][d] += 1

        boxes[box_index(row, col)][d] += 1

        board[row][col] = str(d)

def could_place(
    d: int,
    row: int,
    col: int,
    rows: list[defaultdict[int, int]],
    cols: list[defaultdict[int, int]],
    boxes: list[defaultdict[int, int]],
):
    """
    Check if one could place a number d in (row, col) cell
    """
    return not (
            d in rows[row]
            or d in cols[col]
            or d in boxes[box_index(row, col)]
    )


def place_next_numbers(
    row: int,
    col: int,
    rows: list[defaultdict[int, int]],
    cols: list[defaultdict[int, int]],
    boxes: list[defaultdict[int, int]],
    board: list[list[str]],
    sudoku_solved: list[bool],
):
    """
    Call backtrack function in recursion to continue to place numbers
    till the moment we have a solution
    """
    if col == SUB_BOX_ELEMENT_COUNT - 1 and row == SUB_BOX_ELEMENT_COUNT - 1:
        sudoku_solved[0] = True
    else:
        if col == SUB_BOX_ELEMENT_COUNT - 1:
            backtrack(
                row=row+1,
                col=0,
                rows=rows,
                cols=cols,
                boxes=boxes,
                board=board,
                sudoku_solved=sudoku_solved,
            )
            # backtrack(row + 1, 0, board, sudoku_solved)
        else:
            backtrack(
                row=row,
                col=col+1,
                rows=rows,
                cols=cols,
                boxes=boxes,
                board=board,
                sudoku_solved=sudoku_solved,
            )
            # backtrack(row, col + 1, board, sudoku_solved)

def remove_number(
    d: int,
    row: int,
    col: int,
    rows: list[defaultdict[int, int]],
    cols: list[defaultdict[int, int]],
    boxes: list[defaultdict[int, int]],
    board: list[list[str]],
):
    """
    Remove a number that didn't lead to a solution
    """
    rows[row][d] -= 1
    cols[col][d] -= 1

    this_box_index = box_index(row, col)
    boxes[this_box_index][d] -= 1

    if rows[row][d] == 0:
        del rows[row][d]

    if cols[col][d] == 0:
        del cols[col][d]

    this_box_index = box_index(row, col)
    if boxes[this_box_index][d] == 0:
        del boxes[this_box_index][d]

    board[row][col] = "."

# region: function: 'backtrack'
def backtrack(
        row: int,
        col: int,
        rows: list[defaultdict[int, int]],
        cols: list[defaultdict[int, int]],
        boxes: list[defaultdict[int, int]],
        board: list[list[str]],
        sudoku_solved: list[bool],
):
    """
    Backtracking
    """
    if board[row][col] == ".":
        for d in range(1, 10):
            if could_place(
                d=d,
                row=row,
                col=col,
                rows=rows,
                cols=cols,
                boxes=boxes,
            ):
                place_number(
                    d=d,
                    row=row,
                    col=col,
                    rows=rows,
                    cols=cols,
                    boxes=boxes,
                    board=board,
                )
                place_next_numbers(
                    row=row,
                    col=col,
                    rows=rows,
                    cols=cols,
                    boxes=boxes,
                    board=board,
                    sudoku_solved=sudoku_solved,
                )
                if sudoku_solved[0]:
                    return
                remove_number(
                    d=d,
                    row=row,
                    col=col,
                    rows=rows,
                    cols=cols,
                    boxes=boxes,
                    board=board,
                )
    else:
        place_next_numbers(
            row=row,
            col=col,
            rows=rows,
            cols=cols,
            boxes=boxes,
            board=board,
            sudoku_solved=sudoku_solved,
        )

def solve_sudoku(board: list[list[str]]) -> list[list[str]]:

    rows: list[defaultdict[int, int]] = [
        defaultdict(int)
        for _ in range(SUB_BOX_ELEMENT_COUNT)
    ]
    cols: list[defaultdict[int, int]] = [
        defaultdict(int)
        for _ in range(SUB_BOX_ELEMENT_COUNT)
    ]
    boxes: list[defaultdict[int, int]] = [
        defaultdict(int)
        for _ in range(SUB_BOX_ELEMENT_COUNT)
    ]

    for i in range(SUB_BOX_ELEMENT_COUNT):
        for j in range(SUB_BOX_ELEMENT_COUNT):
            if board[i][j] != ".":
                d = int(board[i][j])
                place_number(
                    d=d,
                    row=i,
                    col=j,
                    rows=rows,
                    cols=cols,
                    boxes=boxes,
                    board=board,
                )
                # place_number(d, i, j)

    sudoku_solved = [False]
    backtrack(
        row=0,
        col=0,
        rows=rows,
        cols=cols,
        boxes=boxes,
        board=board,
        sudoku_solved=sudoku_solved,
    )
    return board