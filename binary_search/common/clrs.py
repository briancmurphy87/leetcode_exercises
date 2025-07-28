def binary_search(array: list[int], target: int) -> int:
    return binary_search_helper(
        array=array,
        target=target,
        left_i=0,
        right_i=len(array)-1,
    )

def binary_search_helper(
        array: list[int],
        target: int,
        left_i: int,
        right_i: int,
) -> int:
    if left_i > right_i:
        return -1

    mid_i = (left_i + right_i) // 2
    if array[mid_i] == target:
        return mid_i

    elif array[mid_i] < target:
        return binary_search_helper(
            array=array,
            target=target,
            left_i=mid_i + 1,
            right_i=len(array) -1,
        )

    else:
        # mid_val > target
        return binary_search_helper(
            array=array,
            target=target,
            left_i=0,
            right_i=mid_i - 1,
        )
