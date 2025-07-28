# class FibMemo:
#     def __init__(self, n: int):
#         pass


class Solution:
    def __init__(self) -> None:
        self._fib_cache: dict[int, int] = {
            0: 0, 1: 1,
        }

    def fib(self, n: int) -> int:
        # calculate and store in cache
        return self._get_or_calculate_fib(n)

    def _get_or_calculate_fib(
        self, n: int,
    ) -> int:
        fib_cached: int | None = self._fib_cache.get(n, None)
        if fib_cached is not None:
            return fib_cached

        # calculate
        fib_n_2 = self._get_or_calculate_fib(n - 2)
        fib_n_1 = self._get_or_calculate_fib(n - 1)
        fib_n = fib_n_1 + fib_n_2

        # add to cache
        self._fib_cache[n] = fib_n

        return fib_n

if __name__ == '__main__':
    # solution = Solution()
    print(Solution().fib(1))
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(4))
"""
Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""