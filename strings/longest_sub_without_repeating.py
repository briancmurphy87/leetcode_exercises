from collections import defaultdict


def length_of_longest_sub(source_string: str) -> int:
    # # for char_index in range(1, len(source_string))
    # max_sub_len = 1
    # curr_sub_len = 1
    # for char_index in range(1, len(source_string)):
    #     # if char_index == 0:
    #     #     max_sub_len = 1
    #     #     continue
    #     if source_string[char_index] != source_string[char_index - 1]:
    #         curr_sub_len += 1
    #     elif curr_sub_len > max_sub_len:  # i, j chars equal
    #         max_sub_len = curr_sub_len
    #         curr_sub_len = 1
    #
    # if curr_sub_len > max_sub_len:
    #     max_sub_len = curr_sub_len
    #
    # return max_sub_len

    substring_len_start = 2
    substring_len_finish = 7
    for substring_len in range(substring_len_start, substring_len_finish + 1):
        # TODO: not the right approach
        tracked_substrings_without_repeating, tracked_substrings = non_repeating_sub_of_len(
            source_string,
            substring_len,
        )
        x = 0


def non_repeating_sub_of_len(
        source_string: str,
        substring_len: int,
) -> tuple[frozenset[str], defaultdict[str, list[int]]]:
    tracked_substrings: defaultdict[str, list[int]] = defaultdict(list)
    for index_substring_start in range(0, len(source_string) - substring_len):
        index_substring_finish = index_substring_start + substring_len
        tracked_substrings[source_string[index_substring_start:index_substring_finish]].append(
            index_substring_start
        )

    tracked_substrings_without_repeating: frozenset[str] = frozenset([
        substring
        for substring, substring_start_indices in tracked_substrings.items()
        if len(substring_start_indices) == 1
    ])
    return tracked_substrings_without_repeating, tracked_substrings


if __name__ == "__main__":
    print(length_of_longest_sub("abcabcbb"))
    x = 0