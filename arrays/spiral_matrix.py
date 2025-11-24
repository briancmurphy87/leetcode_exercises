# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         pass

def check_range(range_min_max: tuple[int, int], label: str) -> None:
    assert range_min_max[0] <= range_min_max[1], f"bad range: {range_min_max} |label: {label}"

def go_right(
    matrix: list[list[int]],
    matrix_i_range: tuple[int, int],
    matrix_j_range: tuple[int, int],
    i_fixed: int,
    j_range: tuple[int, int],
) -> tuple[list[int], tuple[int , int]] | None:
    check_range(matrix_i_range, "go-right-matrix_i_range")
    assert matrix_i_range[0] <= i_fixed <= matrix_i_range[1]

    check_range(matrix_j_range, "go-right-matrix_j_range")

    # can't move?
    if matrix_j_range[0] == matrix_j_range[1]:
        return [], (i_fixed, j_range[0])

    for item in j_range:
        assert matrix_j_range[0] <= item <= matrix_j_range[1], f"bad j: {item} |matrix_i_range={matrix_i_range} |matrix_j_range={matrix_j_range}"

    return (
        [matrix[i_fixed][j] for j in range(j_range[0], j_range[1] + 1)],
        (i_fixed, j_range[1])
    )

def go_left(
    matrix: list[list[int]],
    matrix_i_range: tuple[int, int],
    matrix_j_range: tuple[int, int],
    i_fixed: int,
    j_range: tuple[int, int],
) -> tuple[list[int], tuple[int , int]]:
    check_range(matrix_i_range, "go_left-matrix_i_range")
    assert matrix_i_range[0] <= i_fixed <= matrix_i_range[1]

    check_range(matrix_j_range, "go_left-matrix_j_range")
    # can't move?
    if matrix_j_range[0] == matrix_j_range[1]:
        return [], (i_fixed, j_range[0])

    for item in j_range:
        assert matrix_j_range[0] <= item <= matrix_j_range[1], f"bad j: {item} |matrix_i_range={matrix_i_range} |matrix_j_range={matrix_j_range}"

    # going in reverse order
    return (
        [matrix[i_fixed][j] for j in range(j_range[1], j_range[0] - 1, -1)],
        (i_fixed, j_range[0])
    )


def go_up(
        matrix: list[list[int]],
        matrix_i_range: tuple[int, int],
        matrix_j_range: tuple[int, int],
        j_fixed: int,
        i_range: tuple[int, int],
) -> tuple[list[int], tuple[int , int]] | None:
    check_range(matrix_j_range, "go_up-matrix_j_range")
    assert matrix_j_range[0] <= j_fixed <= matrix_j_range[1]

    check_range(matrix_i_range, "go_up-matrix_i_range")
    for item in i_range:
        assert matrix_i_range[0] <= item <= matrix_i_range[1], f"bad i: {item} |matrix_i_range={matrix_i_range}"

    # can't move?
    if matrix_j_range[0] == matrix_i_range[1]:
        return [], (i_range[0], j_fixed)

    # go in reverse order
    return (
        [matrix[i][j_fixed] for i in range(i_range[1], i_range[0] - 1, -1)],
        (i_range[0], j_fixed)
    )

def go_down(
        matrix: list[list[int]],
        matrix_i_range: tuple[int, int],
        matrix_j_range: tuple[int, int],
        j_fixed: int,
        i_range: tuple[int, int],
) -> tuple[list[int], tuple[int , int]] | None:
    check_range(matrix_j_range, "go_down-matrix_j_range")
    assert matrix_j_range[0] <= j_fixed <= matrix_j_range[1]

    check_range(matrix_i_range, "go_down-matrix_i_range")

    # can't move?
    if matrix_i_range[0] == matrix_i_range[1]:
        return [], (i_range[0], j_fixed)

    # otherwise, verify good indices
    for item in i_range:
        assert matrix_i_range[0] <= item <= matrix_i_range[1], f"bad i: {item} |matrix_i_range={matrix_i_range} |matrix_j_range"
    # then return:
    # 1. matrix elements gathered from this move
    # 2. final (i,j) of this move (i.e. where we landed)
    return (
        [matrix[i][j_fixed] for i in range(i_range[0], i_range[1] + 1)],
        (i_range[1], j_fixed)
    )

def spiral_order_impl(
        matrix: list[list[int]],
        matrix_i_range: tuple[int, int],
        matrix_j_range: tuple[int, int],
        level: int,
) -> list[int]:
    i_start, i_finish = matrix_i_range
    row_n = i_finish - i_start + 1

    j_start, j_finish = matrix_j_range
    col_n = j_finish - j_start + 1

    valid_count_rows = row_n > 0
    valid_count_cols = col_n > 0
    # if one invalid -> both invalid
    # assert valid_count_rows == valid_count_cols, f"|matrix_i_range={matrix_i_range} |matrix_j_range={matrix_j_range}"
    if not (valid_count_rows and valid_count_cols):
        # shrunk down to a stopping condition
        return []

    assert row_n > 0, f"|row_n={row_n} |matrix_i_range={matrix_i_range} |matrix_j_range={matrix_j_range}"
    assert col_n > 0, f"|col_n={col_n} |matrix_i_range={matrix_i_range} |matrix_j_range={matrix_j_range}"

    forbid_vertical = row_n == 1
    forbid_horizontal = col_n == 1
    if forbid_vertical and forbid_horizontal:
        assert matrix_i_range == matrix_j_range, f"|matrix_i_range={matrix_i_range} |matrix_j_range={matrix_j_range}"
        return [
            matrix[matrix_i_range[0]][matrix_j_range[0]]
        ]

    """
    edge cases...IF 
    - forbid vert/horz = F/T 
      - can only go DOWN ; by consequence cannot go back UP
    - forbid vert/horz = T/F
      - can only go RIGHT ; by consequence cannot go back LEFT
    """
    start_ij_down: tuple[int, int] = i_start, j_start
    out_right, end_ij_right = go_right(
        matrix=matrix,
        matrix_i_range=matrix_i_range,
        matrix_j_range=matrix_j_range,
        i_fixed=i_start,
        j_range=(j_start, j_finish),
    )
    if not forbid_horizontal:
        start_ij_down = end_ij_right[0] + 1, end_ij_right[1]

    if forbid_vertical:
        # early exit
        return out_right

    # go down
    out_down, end_ij_down = go_down(
        matrix=matrix,
        matrix_i_range=matrix_i_range,
        matrix_j_range=matrix_j_range,
        j_fixed=start_ij_down[1],
        i_range=(start_ij_down[0], i_finish),
    )
    if forbid_horizontal:
        return out_right + out_down

    out_left, end_ij_left = go_left(
        matrix=matrix,
        matrix_i_range=matrix_i_range,
        matrix_j_range=matrix_j_range,
        i_fixed=end_ij_down[0],
        j_range=(j_start, end_ij_down[1] -1),
    )

    out_up, end_ij_up = go_up(
        matrix=matrix,
        matrix_i_range=matrix_i_range,
        matrix_j_range=matrix_j_range,
        j_fixed=end_ij_left[1],
        i_range=(i_start + 1, end_ij_left[0] - 1),
    )
    # spiral complete - repeat with inner square
    # (apply 'shrink' of square via the 'range' param)
    return out_right + out_down + out_left + out_up + spiral_order_impl(
        matrix=matrix,
        matrix_i_range=(
            matrix_i_range[0] + 1, matrix_i_range[1] - 1
        ),
        matrix_j_range=(
            matrix_j_range[0] + 1, matrix_j_range[1] - 1
        ),
        level=(level + 1),
    )

def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    row_n = len(matrix)
    col_n = len(matrix[0])

    return spiral_order_impl(
        # output=[],
        matrix=matrix,
        matrix_i_range=(0, row_n - 1),
        matrix_j_range=(0, col_n - 1),
        level=0,
    )

# region: editorial solution
# https://leetcode.com/problems/spiral-matrix/solutions/1408316/spiral-matrix-by-leetcode-3e24/
def spiral_order_editorial(matrix: list[list[int]]) -> list[int]:
    VISITED = 101
    rows, columns = len(matrix), len(matrix[0])
    # Four directions that we will move: right, down, left, up.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Initial direction: moving right.
    current_direction = 0
    # The number of times we change the direction.
    change_direction = 0
    # Current place that we are at is (row, col).
    # row is the row index; col is the column index.
    row = col = 0
    # Store the first element and mark it as visited.
    result = [matrix[0][0]]
    matrix[0][0] = VISITED

    while change_direction < 2:

        while True:
            # Calculate the next place that we will move to.
            next_row = row + directions[current_direction][0]
            next_col = col + directions[current_direction][1]

            # Break if the next step is out of bounds.
            if not (0 <= next_row < rows and 0 <= next_col < columns):
                break
            # Break if the next step is on a visited cell.
            if matrix[next_row][next_col] == VISITED:
                break

            # Reset this to 0 since we did not break and change the direction.
            change_direction = 0
            # Update our current position to the next step.
            row, col = next_row, next_col
            result.append(matrix[row][col])
            matrix[row][col] = VISITED

        # Change our direction.
        current_direction = (current_direction + 1) % 4
        # Increment change_direction because we changed our direction.
        change_direction += 1

    return result
# endregion
if __name__ == '__main__':
    """
    https://leetcode.com/problems/spiral-matrix/
    EX1
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    EX2
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """
    # print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
    # print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

    # failing case
    print(spiral_order([[2,5],[8,4],[0,-1]]))
    # print(spiral_order(matrix=[[3],[2]]))

    # matrix_5x5 = [
    #     [j for j in range(0, 5)]
    #     for i in range(0, 5)
    # ]
    # print(spiral_order(matrix_5x5))
