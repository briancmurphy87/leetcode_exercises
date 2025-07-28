

# CLRS assumes 1-based indexing
def quick_sort(arr: list[int]) -> None:
    quick_sort_helper(arr, 1, len(arr))

def quick_sort_helper(arr: list[int], p: int, r: int) -> None:
    if p < r:
        q = partition(arr, p, r)
        quick_sort_helper(arr, p, q - 1)
        quick_sort_helper(arr, q + 1, r)

def partition(arr: list[int], p: int, r: int) -> int:
    x = arr[r-1]
    i = p - 1
    for j in range(p, (r - 1) + 1):
        if arr[j - 1] <= x:
            i += 1
            # exchange a_i with a_j
            tmp = arr[j - 1]
            arr[j - 1] = arr[i - 1]
            arr[i - 1] = tmp

    # exchange a_i+1 with a_r
    tmp = arr[r - 1]
    arr[r-1] = arr[(i + 1) - 1]
    arr[(i + 1) - 1] = tmp

    return i + 1