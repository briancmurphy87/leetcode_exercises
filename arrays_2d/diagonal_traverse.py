from enum import Enum

class ShiftMode(Enum):
    UP_AND_RIGHT = 1
    DOWN_AND_LEFT = 2
    COMPLETE = 3

def do_shift_up_and_right(i: int, j: int) -> tuple[int, int]:
    return i - 1, j + 1

# def transition_to_down_and_left(i: int, j: int) -> tuple[int, int]:
#     return i, j + 1

def do_shift_down_and_left(i: int, j: int) -> tuple[int, int]:
    return i + 1, j - 1

# def transition_to_up_and_right(i: int, j: int) -> tuple[int, int]:
#     return i + 1, j


def do_shift_step(shift_mode: ShiftMode, i: int, j: int) -> tuple[int, int]:
    if shift_mode == ShiftMode.UP_AND_RIGHT:
        return do_shift_up_and_right(i, j)

    elif shift_mode == ShiftMode.DOWN_AND_LEFT:
        return do_shift_down_and_left(i, j)

    else:
        raise ValueError(f"Invalid shift mode: {shift_mode.name}")


def post_shift_out_of_bounds(
        shift_mode: ShiftMode,
        m_and_n: tuple[int, int],
        i_and_j: tuple[int, int],
) -> tuple[ShiftMode, tuple[int, int]]:
# ) -> tuple[bool, bool]:

    new_i_and_j = do_shift_step(shift_mode=shift_mode, i=i_and_j[0], j=i_and_j[1])

    if shift_mode == ShiftMode.UP_AND_RIGHT:
        exit_row_top = new_i_and_j[0] < 0
        exit_col_right = new_i_and_j[1] >= m_and_n[1]
        if not exit_row_top and not exit_col_right:
            return shift_mode, new_i_and_j

        elif exit_row_top and exit_col_right:
            # exit mat via top row + right col -> next row; reset col to max value
            return (
                ShiftMode.DOWN_AND_LEFT,
                (
                    i_and_j[0] + 1,
                    m_and_n[1] - 1,
                )
            )

        elif exit_row_top:
            # exit mat via top row -> next col; reset row = 0
            return (
                ShiftMode.DOWN_AND_LEFT,
                (
                    0,
                    i_and_j[1] + 1,
                )
            )
        else:
            # exit_col_right == True
            # exit mat via right column -> next row; reset col to max value
            return (
                ShiftMode.DOWN_AND_LEFT,
                (
                    i_and_j[0] + 1,
                    m_and_n[1] - 1,
                )
            )

    elif shift_mode == ShiftMode.DOWN_AND_LEFT:

        exit_col_left = new_i_and_j[1] < 0
        exit_row_bottom = new_i_and_j[0] >= m_and_n[0]
        if not exit_col_left and not exit_row_bottom:
            return shift_mode, new_i_and_j

        elif exit_col_left and exit_row_bottom:
            # exit mat via left column + bottom row
            # -> reset row to max val; next col
            return (
                ShiftMode.UP_AND_RIGHT,
                (
                    m_and_n[0] - 1,
                    i_and_j[1] + 1,
                )
            )

        elif exit_col_left:
            # exit mat via left column -> next row; reset col = 0
            return (
                ShiftMode.UP_AND_RIGHT,
                (
                    i_and_j[0] + 1,
                    0,
                )
            )

        else:
            # exit_row_bottom == True
            # exit mat via bottom row
            # -> next col; reset row to max val
            return (
                ShiftMode.UP_AND_RIGHT,
                (
                    m_and_n[0] - 1,
                    i_and_j[1] + 1,
                )
            )

    else:
        raise ValueError(f"Invalid shift mode: {shift_mode.name}")


def do_shift_helper(
        shift_mode: ShiftMode,
        m_and_n: tuple[int, int],
        i_and_j: tuple[int, int],
) -> tuple[ShiftMode, tuple[int, int]]:

    # new_i_and_j = do_shift_step(shift_mode=shift_mode, i=i_and_j[0], j=i_and_j[1])
    return post_shift_out_of_bounds(
        shift_mode=shift_mode,
        m_and_n=m_and_n,
        i_and_j=i_and_j,
    )
    # if post_shift_transition_state is None:
    #     # continuing in the same direction
    #     return shift_mode, new_i_and_j
    #
    # else:
    #     # change course
    #     post_shift_mode, post_shift_i_and_j = post_shift_transition_state
    #     return post_shift_mode, post_shift_i_and_j

def do_shift(
        mat: list[list[int]],
        output: list[int],
        shift_mode: ShiftMode,
        m_and_n: tuple[int, int],
        i_and_j: tuple[int, int],
) -> tuple[ShiftMode, tuple[int, int]]:
    post_shift_mode, post_shift_i_and_j = do_shift_helper(
        shift_mode=shift_mode,
        m_and_n=m_and_n,
        i_and_j=i_and_j,
    )

    # add new value to output
    output.append(mat[post_shift_i_and_j[0]][post_shift_i_and_j[1]])

    # check for completion
    if post_shift_i_and_j[0] >= (m_and_n[0] -1) and post_shift_i_and_j[1] >= (m_and_n[1]-1):
        return (
            ShiftMode.COMPLETE,
            (-1, -1),
        )
    else:
        return post_shift_mode, post_shift_i_and_j

def diag_traverse(mat: list[list[int]]) -> list[int]:
    if not mat:
        return []

    m = len(mat)
    n = len(mat[0])
    if m == n == 1:
        return mat[0]

    output: list[int] = []

    shift_mode = ShiftMode.UP_AND_RIGHT
    curr_i, curr_j = 0, 0
    output.append(mat[curr_i][curr_j])


    while shift_mode != ShiftMode.COMPLETE:
        shift_mode, (curr_i, curr_j) = do_shift(
            mat=mat,
            output=output,
            shift_mode=shift_mode,
            m_and_n=(m, n),
            i_and_j=(curr_i, curr_j),
        )

    return output

if __name__ == '__main__':
    """
    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]
    """

    out = diag_traverse([[1]])
    print(out)

    print(diag_traverse([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))

    mat1 = [[1,2,3],[4,5,6],[7,8,9]]
    out1 = diag_traverse(mat1)
    print(out1)

    mat2 = [[1, 2], [3, 4]]
    out2 = diag_traverse(mat2)
    print(out2)