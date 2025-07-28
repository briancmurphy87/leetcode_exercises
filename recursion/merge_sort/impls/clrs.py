

def merge_sort(arr: list[int], p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


def merge(arr: list[int], p: int, q: int, r: int) -> None:
    arr_tmp = [0] * len(arr)

    i = p
    j = q + 1
    for k in range(1, (r - p + 1) + 1):
        if (
                i > q
                or (j <= r and arr[i-1] > arr[j-1])
        ):
            arr_tmp[k-1] = arr[j-1]
            j += 1
        else:
            arr_tmp[k-1] = arr[i-1]
            i += 1

    for k in range(1, r - p + 1):
        arr[(p+k-1) - 1] = arr_tmp[k-1]