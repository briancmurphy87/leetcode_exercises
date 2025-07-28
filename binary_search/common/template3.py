def binary_search(array: list[int], target: int) -> int:
    if len(array) == 0:
        return -1

    left, right = 0, len(array) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if array[left] == target: return left
    if array[right] == target: return right
    return -1