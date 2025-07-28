# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         pass


def find_k_closest_elements_binary_search(
        array_sorted_asc: list[int],
        k: int,
        x: int,
) -> list[int]:
    if len(array_sorted_asc) == k:
        return array_sorted_asc

def find_k_closest_elements_naive(
        array_sorted_asc: list[int],
        k: int,
        x: int,
) -> list[int]:

    if k == 0:
        return []

    if not array_sorted_asc:
        return []

    k_closest: list[tuple[int, int, int]] = []

    for elt_index, elt in enumerate(array_sorted_asc):
        elt_dist = get_distance(x, elt)
        if len(k_closest) < k:
            k_closest.append((elt_index, elt, elt_dist))
            if len(k_closest) == k:
                k_closest = sort_k_closest(k_closest)

        else:
            _, rhs_val, rhs_dist = k_closest[-1]
            if get_distance_comparator_impl(
                lhs_val=elt,
                lhs_dist=elt_dist,
                rhs_val=rhs_val,
                rhs_dist=rhs_dist,
            ):
                k_closest[-1] = (elt_index, elt, elt_dist)
                k_closest = sort_k_closest(k_closest)


    return sorted([k_closest_val for (_, k_closest_val, _) in k_closest])


def get_distance(x: int, val: int) -> int:
    return abs(x - val)


def get_distance_comparator_impl(
        lhs_val: int,
        lhs_dist: int,
        rhs_val: int,
        rhs_dist: int,
) -> int:
    if lhs_dist == rhs_dist:
        return lhs_val < rhs_val
    else:
        return lhs_dist < rhs_dist


def sort_k_closest(k_closest: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    return sorted(
        k_closest,
        key=lambda t3_index_val_dist: t3_index_val_dist[2]
    )


if __name__ == "__main__":
    """
    Example 1:

    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
    
    Example 2:
    
    Input: arr = [1,1,2,3,4,5], k = 4, x = -1
    
    Output: [1,1,2,3]
"""
    print(find_k_closest_elements(array_sorted_asc=[1, 2, 3, 4, 5], k=4, x=3))