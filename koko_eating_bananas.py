
def min_eating_speed(piles: list[int], max_hours_to_eat: int) -> int:
    num_piles = len(piles)

    # trivial case 1
    max_pile_count = max(piles)
    if max_hours_to_eat == num_piles:
        return max_pile_count

    # trivial case 2
    total_banana_count = sum(piles)
    if max_hours_to_eat >= total_banana_count:
        return 1

    # trivial case 3
    if num_piles == 1:
        return ceil_division(max_hours_to_eat, total_banana_count)

    # # trivial case 4
    # if (not any(elt != piles[0] for elt in piles[1:])) and max_hours_to_eat > piles[0]:
    #     return max_pile_count

    return find_min_k_binary_search(
        piles=piles,
        max_hours_to_eat=max_hours_to_eat,
        total_banana_count=total_banana_count,
    )
    # return find_min_k_naive(
    #     max_hours_to_eat=max_hours_to_eat,
    #     max_pile_count=max_pile_count,
    #     total_banana_count=total_banana_count,
    # )

def find_min_k_binary_search(
    piles: list[int], max_hours_to_eat: int, total_banana_count: int,
) -> int:
    from functools import reduce
    min_value, max_value = reduce(
        lambda acc, x: (
            min(acc[0], x), max(acc[1], x)
        ),
        piles[1:],
        (piles[0], piles[0])
    )
    assert is_feasible(
        theo_k=max_value,
        piles=piles,
        total_banana_count=total_banana_count,
        max_hours_to_eat=max_hours_to_eat,
    )
    return find_min_k_binary_search_in_range(
        piles_high_to_low=sorted(piles, reverse=True),
        max_hours_to_eat=max_hours_to_eat,
        total_banana_count=total_banana_count,
        theo_k_bounds=(max_value, 1),
    )
    # if is_feasible(
    #     theo_k=min_value,
    #     piles=piles,
    #     total_banana_count=total_banana_count,
    #     max_hours_to_eat=max_hours_to_eat,
    # ):
    #     return find_min_k_binary_search_in_range(
    #         piles_high_to_low=sorted(piles, reverse=True),
    #         max_hours_to_eat=max_hours_to_eat,
    #         total_banana_count=total_banana_count,
    #         theo_k_bounds=(max_value, 1),
    #     )
    # else:
    #     return find_min_k_binary_search_iter(
    #         piles_high_to_low=sorted(piles, reverse=True),
    #         max_hours_to_eat=max_hours_to_eat,
    #         total_banana_count=total_banana_count,
    #         curr_theo_k_index=0,
    #     )


def find_min_k_binary_search_iter(
        piles_high_to_low: list[int],
        max_hours_to_eat: int,
        total_banana_count: int,
        curr_theo_k_index: int,
) -> int:

    # invariant: upper-bound candidate always feasible
    assert is_feasible(
        theo_k=piles_high_to_low[curr_theo_k_index],
        piles=piles_high_to_low,
        total_banana_count=total_banana_count,
        max_hours_to_eat=max_hours_to_eat,
    )

    # see if we can get a lower value
    # -> find next pile count distinct from reference pile count
    next_theo_k_index = next(
        (
            piles_index + curr_theo_k_index
            for piles_index, piles_value in enumerate(piles_high_to_low[curr_theo_k_index:])
            if piles_value != piles_high_to_low[curr_theo_k_index]
        ),
        None
    )
    if next_theo_k_index is None:
        return find_min_k_binary_search_in_range(
            piles_high_to_low=piles_high_to_low,
            max_hours_to_eat=max_hours_to_eat,
            total_banana_count=total_banana_count,
            theo_k_bounds=(piles_high_to_low[curr_theo_k_index], 1),
        )

    assert next_theo_k_index > curr_theo_k_index

    theo_k_ub = piles_high_to_low[curr_theo_k_index]
    theo_k_lb = piles_high_to_low[next_theo_k_index]

    theo_k_lb_is_feasible = is_feasible(
        theo_k=piles_high_to_low[next_theo_k_index],
        piles=piles_high_to_low,
        total_banana_count=total_banana_count,
        max_hours_to_eat=max_hours_to_eat,
    )
    if theo_k_lb_is_feasible:
        return find_min_k_binary_search_iter(
            piles_high_to_low=piles_high_to_low,
            max_hours_to_eat=max_hours_to_eat,
            total_banana_count=total_banana_count,
            curr_theo_k_index=curr_theo_k_index+1,
        )
    else:
        # not theo_k_lb_is_feasible
        return find_min_k_binary_search_in_range(
            piles_high_to_low=piles_high_to_low,
            max_hours_to_eat=max_hours_to_eat,
            total_banana_count=total_banana_count,
            theo_k_bounds=(theo_k_ub, theo_k_lb),
        )

def is_feasible_upper_bound(
    theo_k: int, max_hours_to_eat: int, piles: list[int],
) -> bool:
    theo_k_hours_per_pile = [
        ceil_division(theo_k, pile_count)
        for pile_count in piles
    ]
    theo_k_hours_total = sum(theo_k_hours_per_pile)
    return theo_k_hours_total <= max_hours_to_eat

def is_feasible_lower_bound(
    theo_k: int, total_banana_count: int, max_hours_to_eat: int,
) -> bool:
    total_hours_lower_bound = ceil_division(theo_k, total_banana_count)
    return total_hours_lower_bound <= max_hours_to_eat

def is_feasible(
    theo_k: int,
    piles: list[int],
    total_banana_count: int,
    max_hours_to_eat: int,
) -> bool:
    return (
        is_feasible_lower_bound(theo_k, total_banana_count, max_hours_to_eat)
        and is_feasible_upper_bound(theo_k, max_hours_to_eat, piles)
    )

def ceil_division(x: int, y: int) -> int:
    # if y is perfectly divisible by x, return y // x
    return (y + x - 1) // x

def get_avg_split(lhs: int, rhs: int) -> tuple[int, ...]:
    tally = lhs + rhs
    if tally % 2 == 0:
        return (tally // 2,)
    else:
        avg_down = tally // 2
        return avg_down, avg_down + 1

def is_complete_range(
        lower_bound: int, upper_bound: int, in_between_vals: tuple[int, ...],
) -> bool:
    bound_diff = upper_bound - lower_bound

    # edge case; (lower, upper) == in_between_vals
    if (
            bound_diff == 1
            and len(in_between_vals) == 2
            and in_between_vals[0] == lower_bound
            and in_between_vals[1] == upper_bound
    ):
        return True

    if len(in_between_vals) != (bound_diff - 1):
        return False

    if not in_between_vals:
        # there are no ints strictly between
        return bound_diff == 1

    return (
        in_between_vals[0] == lower_bound + 1
        and in_between_vals[-1] == upper_bound - 1
        and all(
            in_between_vals[i] + 1 == in_between_vals[i + 1]
            for i in range(len(in_between_vals) - 1)
        )
    )


def find_min_k_binary_search_in_range(
    piles_high_to_low: list[int],
    max_hours_to_eat: int,
    total_banana_count: int,
    theo_k_bounds: tuple[int, int],
) -> int:
    (theo_k_ub, theo_k_lb) = theo_k_bounds

    theo_k_lb_is_feasible = is_feasible(
        theo_k=theo_k_lb,
        piles=piles_high_to_low,
        total_banana_count=total_banana_count,
        max_hours_to_eat=max_hours_to_eat,
    )

    theo_k_candidates = get_avg_split(theo_k_ub, theo_k_lb)
    candidates_are_range_between_bounds = is_complete_range(
        lower_bound=theo_k_lb, upper_bound=theo_k_ub, in_between_vals=theo_k_candidates,
    )

    if candidates_are_range_between_bounds and theo_k_lb_is_feasible:
        return theo_k_lb

    # theo_k_candidate_feasible = -1
    # for theo_k in theo_k_candidates:
    #     if is_feasible(
    #             theo_k=theo_k,
    #             piles=piles_high_to_low,
    #             total_banana_count=total_banana_count,
    #             max_hours_to_eat=max_hours_to_eat,
    #     ):
    #         theo_k_candidate_feasible = theo_k
    #         break
    theo_k_candidate_feasible: int | None = next(
        (
            theo_k
            for theo_k in theo_k_candidates
            if is_feasible(
                theo_k=theo_k,
                piles=piles_high_to_low,
                total_banana_count=total_banana_count,
                max_hours_to_eat=max_hours_to_eat,
            )
        ),
        None
    )
    # out of candidates to evaluate -> return upper-bound
    if theo_k_candidate_feasible is None:
        if candidates_are_range_between_bounds:
            return theo_k_ub
        else:
            # evaluate a tightened range
            theo_k_lb_new = theo_k_candidates[-1] + 1
            return find_min_k_binary_search_in_range(
                piles_high_to_low=piles_high_to_low,
                max_hours_to_eat=max_hours_to_eat,
                total_banana_count=total_banana_count,
                theo_k_bounds=(theo_k_ub, theo_k_lb_new),
            )
    # else:
    if candidates_are_range_between_bounds:
        return theo_k_candidate_feasible
    else:
        # evaluate a tightened range
        theo_k_ub_new = theo_k_candidate_feasible
        assert theo_k_ub_new >= theo_k_lb
        return find_min_k_binary_search_in_range(
            piles_high_to_low=piles_high_to_low,
            max_hours_to_eat=max_hours_to_eat,
            total_banana_count=total_banana_count,
            theo_k_bounds=(theo_k_ub_new, theo_k_lb),
        )


def find_min_k_naive(
        max_hours_to_eat: int,
        max_pile_count: int,
        total_banana_count: int,
        go_in_reverse: bool = True,
) -> int:
    if go_in_reverse:
        gen_range = range(max_pile_count, 2, -1)
    else:
        gen_range = range(2, max_pile_count)

    # max_pile_count = piles_low_to_high[-1]
    feasible_k = max_pile_count
    for theo_k in gen_range:
        # eat from piles w/o constraint
        if not is_feasible_lower_bound(theo_k, total_banana_count, max_hours_to_eat):
            continue
        # total_hours_lower_bound = ceil_division(theo_k, total_banana_count)
        # # total_hours_lower_bound = math.ceil(float(total_banana_count) / float(theo_k))
        # if total_hours_lower_bound > max_hours_to_eat:
        #     continue

        if not is_feasible_upper_bound(theo_k, max_hours_to_eat, piles):
            continue
        # theo_k_hours_per_pile = [
        #     ceil_division(theo_k, pile_count)
        #     for pile_count in piles
        # ]
        # theo_k_hours_total = sum(theo_k_hours_per_pile)
        # if theo_k_hours_total > max_hours_to_eat:
        #     continue

        # low to high -> return first instance found
        if not go_in_reverse:
            return theo_k
        else:
            # high to low -> see if lower value is feasible
            feasible_k = theo_k

    assert feasible_k > 0
    return feasible_k
    # return -1


if __name__ == '__main__':
    piles = [30,11,23,4,20]
    h = 6
    h = 7

    # piles = [1000000000]
    # h = 2

    # piles = [1000000000,1000000000]
    # h = 3
    #
    piles = [1,1,1,999999999]
    h = 10

    # piles = [3, 6, 7, 11]
    # h = 8

    piles = [805306368, 805306368, 805306368]
    h = 1000000000

    res = min_eating_speed(piles=piles, max_hours_to_eat=h)
    print(f"min k: {res}; for 'h' = {h} and piles.len={len(piles)} piles={piles}")
    x = 0