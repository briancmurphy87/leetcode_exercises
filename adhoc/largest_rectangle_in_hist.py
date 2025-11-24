# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         pass

import math

DEBUG_MODE: bool = False

def largest_rectangle_area_impl(
        i_lhs: int,
        i_rhs: int,
        min_observed_height: int,
        max_area_info: tuple[int, int, int],
        heights: list[int],
) -> tuple[int, int, int]:
    assert i_rhs >= i_lhs, f"{i_rhs} != {i_lhs}"
    width = 1 if i_rhs == i_lhs else (i_rhs - i_lhs + 1)
    min_observed_height = min(min_observed_height, heights[i_rhs])

    area = width * min_observed_height
    if area >= max_area_info[0]:
        if DEBUG_MODE:
            print(f"[L2] updating max area: |i_lhs={i_lhs}| |i_rhs={i_rhs}| |width={width}| |height={min_observed_height}| |area={area} |area_old={max_area_info}")
        max_area_info = area, i_lhs, i_rhs

    # advance
    if i_rhs == len(heights) - 1:
        return max_area_info
    else:
        return largest_rectangle_area_impl(i_lhs, i_rhs + 1, min_observed_height, max_area_info, heights)

def largest_rectangle_area(heights: list[int]) -> int:
    all_max_area_info = 0, 0, 0
    for i_lhs in range(0, len(heights)):
        i_rhs = i_lhs
        this_max_area = (
            largest_rectangle_area_impl(i_lhs, i_rhs, heights[i_lhs], (0, 0, 0), heights)
        )
        if this_max_area[0] >= all_max_area_info[0]:
            if DEBUG_MODE:
                print()
                print(f"[L1] updating max area: |i_lhs={i_lhs}| |i_rhs={i_rhs} |area={this_max_area} |area_old={all_max_area_info}")
            all_max_area_info = this_max_area
    return all_max_area_info[0]

# region: solutions

def largest_rectangle_area_brute_force_v1(heights: list[int]) -> int:
    max_area = 0
    for i in range(len(heights)):
        for j in range(i, len(heights)):
            min_height = math.inf
            for k in range(i, j + 1):
                min_height = min(min_height, heights[k])
            max_area = max(max_area, min_height * (j - i + 1))
    return max_area

def largest_rectangle_area_brute_force_v2(heights: list[int]) -> int:
    max_area = 0
    for i in range(len(heights)):
        min_height = math.inf
        for j in range(i, len(heights)):
            min_height = min(min_height, heights[j])
            max_area = max(max_area, min_height * (j - i + 1))
    return max_area

# region: approach 3 - divide and conquer
def calculate_area(heights: list[int], start: int, end: int) -> int:
    if start > end:
        return 0
    min_index = start
    for i in range(start, end + 1):
        if heights[min_index] > heights[i]:
            min_index = i
    return max(
        heights[min_index] * (end - start + 1),
        calculate_area(heights, start, min_index - 1),
        calculate_area(heights, min_index + 1, end),
    )

def largest_rectangle_area_divide_and_conquer(heights: list[int]) -> int:
    return calculate_area(heights, 0, len(heights) - 1)
# endregion

# endregion
if __name__ == '__main__':
    """
    https://leetcode.com/problems/largest-rectangle-in-histogram/description/
    
    EX1
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    
    EX2
    Input: heights = [2,4]
    Output: 4
    """
    # print(largest_rectangle_area([2, 4]))
    # print(largest_rectangle_area([2,1,5,6,2,3]))
    print(largest_rectangle_area_divide_and_conquer([2, 1, 5, 6, 2, 3]))
