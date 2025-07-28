from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum(nums, target)


def two_sum(nums: list[int], target: int) -> list[int]:
    if len(nums) == 2:
        return [0, 1]

    tracked_val_to_index: defaultdict[int, list[int]] = defaultdict(list)
    for val_index, val in enumerate(nums):
        tracked_val_to_index[val].append(val_index)

    return two_sum_helper(
        nums=nums,
        target=target,
        lhs_i=0,
        tracked_val_to_index=tracked_val_to_index,
    )

def two_sum_helper(
        nums: list[int], target: int,
        lhs_i: int,
        tracked_val_to_index: defaultdict[int, list[int]],
) -> list[int]:
    rem_val = target - nums[lhs_i]

    rem_val_indices = [
        rem_val_i
        for rem_val_i in tracked_val_to_index.get(rem_val, [])
        if rem_val_i != lhs_i
    ]
    if rem_val_indices:
        return [lhs_i, rem_val_indices[0]]

    return two_sum_helper(
        nums=nums,
        target=target,
        lhs_i=lhs_i + 1,
        tracked_val_to_index=tracked_val_to_index,
    )


if __name__ == "__main__":
    """
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    print(two_sum([2, 7, 11, 15], 9))

    """
    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:
    """
    print(two_sum([3, 2, 4], 6))

    """
    Input: nums = [3,3], target = 6
    Output: [0,1]
    """
    print(two_sum([3, 3], 6))