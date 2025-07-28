def binary_search(array: list[int], target: int) -> int:
    if len(array) == 0:
        return -1

    left, right = 0, len(array) - 1
    while left < right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if array[left] == target:
        return left
    return -1
