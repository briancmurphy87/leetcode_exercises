from collections import defaultdict

from trie.trie_impl import TrieNode


# def length_of_longest_sub(source_string: str) -> int:
#     # # for char_index in range(1, len(source_string))
#     # max_sub_len = 1
#     # curr_sub_len = 1
#     # for char_index in range(1, len(source_string)):
#     #     # if char_index == 0:
#     #     #     max_sub_len = 1
#     #     #     continue
#     #     if source_string[char_index] != source_string[char_index - 1]:
#     #         curr_sub_len += 1
#     #     elif curr_sub_len > max_sub_len:  # i, j chars equal
#     #         max_sub_len = curr_sub_len
#     #         curr_sub_len = 1
#     #
#     # if curr_sub_len > max_sub_len:
#     #     max_sub_len = curr_sub_len
#     #
#     # return max_sub_len
#
#     substring_len_start = 2
#     substring_len_finish = 7
#     for substring_len in range(substring_len_start, substring_len_finish + 1):
#         # TODO: not the right approach
#         tracked_substrings_without_repeating, tracked_substrings = non_repeating_sub_of_len(
#             source_string,
#             substring_len,
#         )
#         x = 0
#
#
# def non_repeating_sub_of_len(
#         source_string: str,
#         substring_len: int,
# ) -> tuple[frozenset[str], defaultdict[str, list[int]]]:
#     tracked_substrings: defaultdict[str, list[int]] = defaultdict(list)
#     for index_substring_start in range(0, len(source_string) - substring_len):
#         index_substring_finish = index_substring_start + substring_len
#         tracked_substrings[source_string[index_substring_start:index_substring_finish]].append(
#             index_substring_start
#         )
#
#     tracked_substrings_without_repeating: frozenset[str] = frozenset([
#         substring
#         for substring, substring_start_indices in tracked_substrings.items()
#         if len(substring_start_indices) == 1
#     ])
#     return tracked_substrings_without_repeating, tracked_substrings
#

def length_of_longest_sub(input_string: str) -> int:
    if not input_string:
        return 0

    # output
    winner: tuple[int, int, int] = (0, 0, 1)

    # initial search
    curr_sub_i = 0
    for curr_sub_i in range(len(input_string)):
    # while (curr_sub_i + 1) < len(input_string):
        # search substr at next starting point
        _, candidate_j = evaluate_current_substring_candidate(
            input_string=input_string,
            sub_i=curr_sub_i,
            sub_j=curr_sub_i + 1,
            sub_char_lookup={input_string[curr_sub_i]},
        )
        # evaluate this substr candidate
        candidate_len = candidate_j - curr_sub_i + 1
        print(f"candidate: {input_string[curr_sub_i:(candidate_j + 1)]} |sub_i={curr_sub_i} |len={candidate_len}")
        if candidate_len > winner[-1]:
            winner = (curr_sub_i, candidate_j, candidate_len)

        # # advance to next substr evaluation
        # curr_sub_i = candidate_i + 1

    print(f"winner: {input_string[winner[0]:(winner[1] + 1)]} |len={winner[-1]}")
    return winner[-1]

def evaluate_current_substring_candidate(
        input_string: str,
        sub_i: int,
        sub_j: int,
        sub_char_lookup: set[str]
) -> tuple[int, int]:

    if sub_j >= len(input_string):
        return sub_i, sub_j - 1

    char_j = input_string[sub_j]
    if char_j in sub_char_lookup:
        return sub_i, sub_j - 1

    # record this char as part of current substr
    sub_char_lookup.add(char_j)

    # step ahead to next char
    next_sub_j = sub_j + 1
    # unless at end of string
    if next_sub_j >= len(input_string):
        return sub_i, sub_j

    return evaluate_current_substring_candidate(
        input_string=input_string,
        sub_i=sub_i,
        sub_j=next_sub_j,
        sub_char_lookup=sub_char_lookup,
    )


"""
official solution as shown here: 
https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/127839/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=string
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res
if __name__ == "__main__":
    print(length_of_longest_sub("abcabcbb"))
    x = 0