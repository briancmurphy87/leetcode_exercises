from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        return subarray_sum(nums, k)

def subarray_sum(nums: list[int], k: int) -> int:
    memoized_sums: defaultdict[int, dict[int, int]] = defaultdict(dict)

    # TODO: use counter
    subarray_count = 0

    # for sum_width = 1
    for val in nums:
        if val == k:
            subarray_count += 1

    # for sum_width = N
    if len(nums) > 1 and k == sum(nums):
        subarray_count += 1

    # for sum_width in [2,N-1]
    for sum_width in range(2, len(nums)):
        subarray_count_at_width = subarray_sum_helper(
            k=k,
            nums=nums,
            sum_width=sum_width,
            memoized_sums=memoized_sums,
        )
        subarray_count += subarray_count_at_width

    return subarray_count

def subarray_sum_helper(
    k: int,
    nums: list[int],
    sum_width: int,
    memoized_sums: defaultdict[int, dict[int, int]],
) -> int:
    subarray_count = 0
    rhs_index_start = sum_width - 1
    for rhs_index in range(rhs_index_start, len(nums)):
        predecessor_subarray_sum = get_memoized_subarray_sum(
            nums=nums,
            sum_width=sum_width - 1,
            sum_rhs_index=rhs_index,
            memoized_sums=memoized_sums,
        )
        lhs_index = get_subarray_sum_lhs_index(rhs_index, sum_width)

        # calculate new sub-array sum
        this_subarray_sum = predecessor_subarray_sum + nums[lhs_index]

        # check condition
        if this_subarray_sum == k:
            subarray_count += 1

        # cache new sub-array sum
        memoized_sums[sum_width][rhs_index] = this_subarray_sum

    return subarray_count


def get_subarray_sum_lhs_index(rhs_index: int, sum_width: int) -> int:
    return rhs_index - (sum_width - 1)

def get_memoized_subarray_sum(
    nums: list[int],
    sum_width: int,
    sum_rhs_index: int,
    memoized_sums: defaultdict[int, dict[int, int]],
) -> int:
    assert sum_width > 0
    if sum_width == 1:
        return nums[sum_rhs_index]
    elif sum_width == len(nums):
        return sum(nums)
    else:
        memoized_sums_for_width = memoized_sums[sum_width]
        return memoized_sums_for_width[sum_rhs_index]

if __name__=='__main__':
    print(subarray_sum([1], 1))
    """
    Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2
    """
    print(subarray_sum([1, 1, 1], 2))
    """
    Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2
    """
    print(subarray_sum([1, 2, 3], 3))