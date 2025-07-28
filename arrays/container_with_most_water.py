# class Solution:
#     def maxArea(self, height: List[int]) -> int:
import math
from typing import NamedTuple


class CandidateInfo(NamedTuple):
    area: int
    width: int
    height: int
    endpoints: tuple[int, int]


def max_area(height: list[int]) -> int:
    area, left, right = 0, 0, len(height) - 1
    while left < right:
        width = right - left
        area = max(area, min(height[left], height[right]) * width)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return area
    # n = len(height)
    # # Sort by:
    # # 1. value descending (i.e., -val)
    # # 2. max(i, n - 1 - i) descending (i.e., farther from center)
    # sorted_height_and_indices: list[tuple[int, int]] = sorted(
    #     list(enumerate(height)),
    #     key=lambda pair: (-pair[1], -max(pair[0], n - 1 - pair[0]))
    # )
    #
    # width_max = n - 1
    #
    # candidate_solution: CandidateInfo = max_area_helper(
    #     heights=height,
    #     width_current=width_max,
    #     candidate_solution=None,
    #     sorted_height_and_indices=sorted_height_and_indices,
    # )
    # return candidate_solution.area


def max_area_helper(
    heights: list[int],
    width_current: int,
    candidate_solution: CandidateInfo | None,
    sorted_height_and_indices: list[tuple[int, int]],
) -> CandidateInfo:

    lhs_i_start = 0
    rhs_i_start = lhs_i_start + width_current

    rhs_i, lhs_i = rhs_i_start, lhs_i_start
    while rhs_i < len(heights):
        rhs_h, lhs_h = heights[rhs_i], heights[lhs_i]
        realized_height = min(lhs_h, rhs_h)
        realized_area = realized_height * width_current

        if candidate_solution is None or realized_area > candidate_solution.area:
            candidate_solution = CandidateInfo(
                area=realized_area,
                width=width_current,
                height=realized_height,
                endpoints=(rhs_i, lhs_i),
            )

        # next iter
        rhs_i += 1
        lhs_i += 1

    width_next = width_current - 1
    if width_next == 0:
        return candidate_solution

    if candidate_solution is not None:
        height_next_required = math.ceil(candidate_solution.area / width_next)
        max_height_index, max_height = sorted_height_and_indices[0]
        if height_next_required > max_height:
            return candidate_solution

    return max_area_helper(
        heights=heights,
        width_current=width_next,
        candidate_solution=candidate_solution,
        sorted_height_and_indices=sorted_height_and_indices,
    )

    # for rhs in range(rhs_i_start, n):
    #     lhs = r


if __name__ == '__main__':
    print(max_area([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))
    # print(max_area([1, 1]))
    # print(max_area([1,8,6,2,5,4,8,3,7]))
"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""