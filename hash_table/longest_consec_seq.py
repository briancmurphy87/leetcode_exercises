# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

class SeqStartCandidate:
    def __init__(self) -> None:
        self.prec = None
        self.next = None
        self.next_count = 0

    def set_next(self, next) -> None:
        assert self.next is None
        self.next = next
        self.next_count = self.next.next_count + 1

    def length_of_sequence_as_start(self):
        return self.next_count + 1

def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    seq_starts_lookup: dict[int, SeqStartCandidate] = {
        nums[0]: SeqStartCandidate(),
    }


    seq_start_max_val_and_len: tuple[int, int] = (1, nums[0])
    for i in range(1, len(nums)):
        ai = nums[i]
        if ai in seq_starts_lookup:
            # duplicate value
            continue

        seq_starts_lookup[ai] = SeqStartCandidate()

        # this node's subsequent value is present
        next_val_node = seq_starts_lookup.get(ai+1)
        if next_val_node is not None:
            seq_starts_lookup[ai].set_next(next_val_node)
            # modify - check for update to seq len
            if seq_starts_lookup[ai].length_of_sequence_as_start() > seq_start_max_val_and_len[0]:
                seq_start_max_val_and_len = (
                    seq_starts_lookup[ai].length_of_sequence_as_start(),
                    ai
                )
        # this node's preceding value is present
        prec_val_node = seq_starts_lookup.get(ai-1)
        if prec_val_node is not None:
            prec_val_node.set_next(seq_starts_lookup[ai])
            # modify - check for update to seq len
            if prec_val_node.length_of_sequence_as_start() > seq_start_max_val_and_len[0]:
                seq_start_max_val_and_len = (
                    prec_val_node.length_of_sequence_as_start(),
                    ai-1
                )

    return seq_start_max_val_and_len[0]

# region: solutions: https://leetcode.com/problems/longest-consecutive-sequence/solutions/127576/longest-consecutive-sequence-by-leetcode-k96v/

# Approach 3: HashSet and Intelligent Sequence Building
def longest_consecutive_v3(nums: list[int]) -> int:
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
# endregion
if __name__ == "__main__":
    """
    https://leetcode.com/problems/longest-consecutive-sequence/
    Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    
    Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    Example 3:
    
    Input: nums = [1,0,1,2]
    Output: 3
    """
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
    # print(longest_consecutive([100,4,200,1,3,2]))