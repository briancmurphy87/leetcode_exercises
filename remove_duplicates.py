def removeDuplicates(self, nums: list[int]) -> int:

    i_out = 0

    for i_in in range(1, len(nums)):
        if nums[i_in] == nums[i_out]:
            continue

        i_out += 1
        nums[i_out] = nums[i_in]

    # for i_unused in range(i_out, len(nums)):
    #     nums[i_unused] = 0

    return i_out + 1


def removeDuplicates2(self, nums: list[int]) -> int:

    i_out = 0

    curr_dup_count = 0
    for i_in in range(1, len(nums)):
        is_dup = nums[i_in] == nums[i_out]
        is_dup_allowed = is_dup and curr_dup_count < 1
        if is_dup and not is_dup_allowed:
            continue


        if is_dup:
            curr_dup_count += 1
        else:
            curr_dup_count = 0

        i_out += 1
        nums[i_out] = nums[i_in]

    return i_out + 1