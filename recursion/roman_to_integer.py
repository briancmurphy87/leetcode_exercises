from collections import defaultdict
from functools import reduce

ROMAN_NUMERAL_INFO_HIGH_TO_LOW: list[tuple[str, int | None, int]] = [
    ("M", None, 1000),
    ("CM", 1, 900),
    ("D", 1, 500),
    ("CD", 1, 400),
    ("C", 3, 100),
    ("XC", 1, 90),
    ("L", 1, 50),
    ("XL", 1, 40),
    ("X", 3, 10),
    ("IX", 1, 9),
    ("V", 1, 5),
    ("IV", 1, 4),
    ("I", 3, 1),
]


def convert_int_to_roman_numerals(val: int) -> str:
    div_m = val // 1000
    rem = val - (div_m * 1000)

    div_cm = rem // 900
    rem = rem - (div_cm * 900)

    div_d = rem // 500
    rem = rem - (div_d * 500)

    div_cd = rem // 400
    rem = rem - (div_cd * 400)

    div_c = rem // 100
    rem = rem - (div_c * 100)

    div_xc = rem // 90
    rem = rem - (div_xc * 90)

    div_l = rem // 50
    rem = rem - (div_l * 50)

    div_xl = rem // 40
    rem = rem - (div_xl * 40)

    div_x = rem // 10
    rem = rem - (div_x * 10)

    div_ix = rem // 9
    rem = rem - (div_ix * 9)

    div_v = rem // 5
    rem = rem - (div_v * 5)

    div_iv = rem // 4
    rem = rem - (div_iv * 4)

    assert 0 <= rem < 4, rem
    div_i = rem

    return "".join(
        roman_numeral * roman_numeral_count
        for roman_numeral, roman_numeral_count in [
            ("M", div_m),
            ("CM", div_cm),
            ("D", div_d),
            ("CD", div_cd),
            ("C", div_c),
            ("XC", div_xc),
            ("L", div_l),
            ("XL", div_xl),
            ("X", div_x),
            ("IX", div_ix),
            ("V", div_v),
            ("IV", div_iv),
            ("I", div_i),
        ]
    )

def convert_roman_numeral_to_int_v1(roman_numeral: str) -> int:
    output_int_value = 0
    return convert_roman_numeral_to_int_helper(
        roman_numeral=roman_numeral,
        roman_numerals_in_order_rev=ROMAN_NUMERAL_INFO_HIGH_TO_LOW[::-1],
        roman_numeral_candidate_index=0,
        roman_numeral_substr_index_finish=len(roman_numeral),  # work from the back of the string
        output_int_value=output_int_value,
    )


def convert_roman_numeral_to_int_helper(
    roman_numeral: str,
    roman_numerals_in_order_rev: list[tuple[str, int | None, int]],
    roman_numeral_candidate_index: int,
    roman_numeral_substr_index_finish: int,
    output_int_value: int,
) -> int:
    candidate_len1, candidate_len1_max_count, candidate_len1_int_val = (
        roman_numerals_in_order_rev[roman_numeral_candidate_index]
    )
    assert len(candidate_len1) == 1

    if candidate_len1 == "M":
        # TODO:
        assert False

    # else:
    roman_numeral_candidate_index += 1
    candidate_len2, candidate_len2_max_count, candidate_len2_int_val = (
        roman_numerals_in_order_rev[roman_numeral_candidate_index]
    )
    assert len(candidate_len2) == 2
    assert candidate_len2_max_count == 1

    # len2 - try first
    if roman_numeral[(roman_numeral_substr_index_finish - 2):roman_numeral_substr_index_finish] == candidate_len2:
        # roman_numeral_sub = roman_numeral[roman_numeral_substr_index_start:roman_numeral_substr_index_finish]
        output_int_value += candidate_len2_int_val

        # continue working from back of string (using next-expected candidate)
        return convert_roman_numeral_to_int_helper(
            roman_numeral=roman_numeral,
            roman_numerals_in_order_rev=roman_numerals_in_order_rev,
            roman_numeral_candidate_index=roman_numeral_candidate_index + 1,
            roman_numeral_substr_index_finish=(roman_numeral_substr_index_finish - 2),
            output_int_value=output_int_value,
        )

    # len1 - try next
    elif roman_numeral[(roman_numeral_substr_index_finish - 1):roman_numeral_substr_index_finish] == candidate_len1:
        roman_numeral_substr_index_start = (roman_numeral_substr_index_finish - 1)
        roman_numeral_sub = roman_numeral[roman_numeral_substr_index_start:roman_numeral_substr_index_finish]
        assert roman_numeral_sub == candidate_len1

        candidate_len1_count = 0
        while roman_numeral_sub == candidate_len1:
            output_int_value += candidate_len1_int_val
            roman_numeral_substr_index_start -= 1
            roman_numeral_sub = roman_numeral[roman_numeral_substr_index_start]
            candidate_len1_count += 1
        assert candidate_len1_count <= candidate_len1_max_count

        # continue working from back of string (using next-expected candidate)
        return convert_roman_numeral_to_int_helper(
            roman_numeral=roman_numeral,
            roman_numerals_in_order_rev=roman_numerals_in_order_rev,
            roman_numeral_candidate_index=roman_numeral_candidate_index + 1,
            roman_numeral_substr_index_finish=roman_numeral_substr_index_start + 1,
            output_int_value=output_int_value,
        )

    else:
        # neither candidate matches -> on to the next one
        return convert_roman_numeral_to_int_helper(
            roman_numeral=roman_numeral,
            roman_numerals_in_order_rev=roman_numerals_in_order_rev,
            roman_numeral_candidate_index=roman_numeral_candidate_index + 1,
            roman_numeral_substr_index_finish=roman_numeral_substr_index_finish,
            output_int_value=output_int_value,
        )

    # for roman_index_rev in range(len(roman_numeral) - 1, -1, -1):

def convert_roman_numeral_to_int_v2(roman_numeral: str) -> int:
    ## APPROACH 1
    # rom_nums_len1: set[str] = set()
    # rom_nums_len2: set[str] = set()
    # for (rom_num, _, _) in roman_numerals_in_order:
    #     if len(rom_num) == 1:
    #         rom_nums_len1.add(rom_num)
    #     else:
    #         rom_nums_len2.add(rom_num)

    # ## APPROACH 2
    # rom_nums_len1, rom_nums_len2 = map(
    #     frozenset,
    #     (
    #         (r for r, _, _ in ROMAN_NUMERAL_INFO_HIGH_TO_LOW if len(r) == 1),
    #         (r for r, _, _ in ROMAN_NUMERAL_INFO_HIGH_TO_LOW if len(r) == 2),
    #     ),
    # )

    ## APPROACH 3 - SINGLE PASS
    """
    how it works...
    
    For each (r, _, _) in roman_numerals_in_order, we yield a tuple:
    ({r}, set()) if len(r) == 1
    (set(), {r}) if len(r) == 2
    
    zip(*) transposes this into two iterables: 
      - one for all the “len==1” sets, 
      - one for “len==2”.
    
    map(frozenset, ...) merges them into frozensets in a single pass
    """
    # roman_numerals_len1, roman_numerals_len2 = map(
    #     frozenset,
    #     zip(*(
    #         ({r}, set())
    #         if len(r) == 1
    #         else
    #         (set(), {r})
    #         for r, _, _ in ROMAN_NUMERAL_INFO_HIGH_TO_LOW
    #     ))
    # )

    ## APPROACH 4 - SINGLE PASS
    """
    Start with accumulator ( [], [] ).
    For each (r, _, _) append r to the correct list.
    At the end, convert both lists into frozensets in one shot.
    """
    roman_numerals_len1, roman_numerals_len2 = (
        lambda reduced_list_len1, reduced_list_len2: (frozenset(reduced_list_len1), frozenset(reduced_list_len2))
    )(*reduce(
        lambda tuple2_accumulator_len_1_and_2, tuple3_roman_numeral_info: (
            tuple2_accumulator_len_1_and_2[0] + [tuple3_roman_numeral_info[0]]
            if len(tuple3_roman_numeral_info[0]) == 1
            else tuple2_accumulator_len_1_and_2[0],
            tuple2_accumulator_len_1_and_2[1] + [tuple3_roman_numeral_info[0]]
            if len(tuple3_roman_numeral_info[0]) == 2
            else tuple2_accumulator_len_1_and_2[1],
        ),
        ROMAN_NUMERAL_INFO_HIGH_TO_LOW,
        ([], []),
    ))

    roman_numeral_val_lookup: dict[str, int] = {
        roman_numeral: roman_numeral_val
        for (roman_numeral, _, roman_numeral_val) in ROMAN_NUMERAL_INFO_HIGH_TO_LOW
    }

    # work from the back of the string
    roman_numeral_vals_realized: defaultdict[str, int] = defaultdict(int)
    roman_numeral_substr_index_finish = len(roman_numeral)

    while roman_numeral_substr_index_finish > 0:

        # try len = 2 first
        if (
                roman_numeral_substr_index_finish >= 2
                and roman_numeral[
                    (roman_numeral_substr_index_finish-2):roman_numeral_substr_index_finish
                ] in roman_numerals_len2
        ):
            offset = 2
        else:
            offset = 1

        # get this subcomponent of the roman numeral tally
        roman_numeral_substr = (
            roman_numeral[
                (roman_numeral_substr_index_finish - offset):roman_numeral_substr_index_finish
            ]
        )
        assert roman_numeral_substr in roman_numeral_val_lookup, roman_numeral_substr

        # update observed counts of that numeral
        roman_numeral_vals_realized[roman_numeral_substr] += 1

        # decrement for next iter
        roman_numeral_substr_index_finish -= offset

    # now do tally
    return sum([
        roman_numeral_val_lookup[roman_numeral] * roman_numeral_count
        for roman_numeral, roman_numeral_count in roman_numeral_vals_realized.items()
    ])

# leet-code solution
ROMAN_NUMERAL_VAL_LOOKUP = {
    roman_numeral: val
    for (roman_numeral, _, val) in ROMAN_NUMERAL_INFO_HIGH_TO_LOW
}

def convert_roman_numeral_to_int_v3(self, s: str) -> int:
    total = ROMAN_NUMERAL_VAL_LOOKUP.get(s[-1])
    for i in reversed(range(len(s) - 1)):
        if ROMAN_NUMERAL_VAL_LOOKUP[s[i]] < ROMAN_NUMERAL_VAL_LOOKUP[s[i + 1]]:
            # e.g. IV, IX, XL, XC, et. al.
            total -= ROMAN_NUMERAL_VAL_LOOKUP[s[i]]
        else:
            total += ROMAN_NUMERAL_VAL_LOOKUP[s[i]]
    return total


if __name__ == "__main__":
    """
    Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    
    Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    
    Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    print(convert_roman_numeral_to_int_v2("MCMXCIV"))