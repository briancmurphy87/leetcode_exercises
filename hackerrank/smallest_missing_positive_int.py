#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def find_smallest_missing_positive(order_numbers: list[int]) -> int:
    """
    Given an unsorted array of integers,
    find the smallest positive integer not present in the array
    in O(n) time and O(1) extra space.
    """
    n = len(order_numbers)

    # Step 1: Replace non-positive numbers and numbers > n with a dummy (n+1)
    for i in range(n):
        if order_numbers[i] <= 0 or order_numbers[i] > n:
            order_numbers[i] = n + 1

    # Step 2: Use index marking: for every number in [1..n], mark index (num-1)
    for num in order_numbers:
        num = abs(num)
        if 1 <= num <= n:
            # Negating the value at index = num - 1 flags that num is present.
            idx = num - 1
            if order_numbers[idx] > 0:
                order_numbers[idx] = -order_numbers[idx]

    # Step 3: Find the first positive index (missing number)
    for i in range(n):
        if order_numbers[i] > 0:
            return i + 1

    # If all numbers [1..n] are present
    return n + 1


if __name__ == '__main__':
    pass
    # orderNumbers_count = int(input().strip())
    #
    # orderNumbers = []
    #
    # for _ in range(orderNumbers_count):
    #     orderNumbers_item = int(input().strip())
    #     orderNumbers.append(orderNumbers_item)
    #
    # result = findSmallestMissingPositive(orderNumbers)
    #
    # print(result)