import copy


def remove_k_digits_impl(num: str, k: int) -> str:
    num_ints = tuple([int(elt) for elt in num])

    k_og = copy.copy(k)

    stack = []
    for digit in num_ints:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If k > 0, remove remaining k digits from the end of the stack
    stack = stack[:-k] if k > 0 else stack

    # Remove leading zeros
    result = ''.join(stack).lstrip('0')

    # Handle edge case where result might be empty
    return result if result else '0'

if __name__ == '__main__':
    res = remove_k_digits_impl("1432219", 3)
    print(res)