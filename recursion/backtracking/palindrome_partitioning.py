class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # return partition_backtracking(s)
        return partition_backtracking_with_dp(s)


def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def partition_backtracking(s: str) -> list[list[str]]:
    result = []
    dfs_backtracking(s, [], result)
    return result

def dfs_backtracking(s: str, path: list[str], result: list[list[str]]):
    if not s:
        result.append(path)
        return
    for i in range(1, len(s) + 1):
        if is_palindrome(s[:i]):
            # add current substring in the currentList
            dfs_backtracking(s[i:], path + [s[:i]], result)
            # backtrack and remove the current substring from currentList

def partition_backtracking_with_dp(s: str) -> list[list[str]]:
    len_s = len(s)
    dp = [[False] * len_s for _ in range(len_s)]
    result = []
    dfs_backtracking_with_dp(result, s, 0, [], dp)
    return result

def dfs_backtracking_with_dp(
    result: list[list[str]],
    s: str,
    start: int,
    current_list: list[str],
    dp: list[list[bool]],
):
    if start >= len(s):
        result.append(list(current_list))

    for end in range(start, len(s)):
        if s[start] == s[end] and (
            (end - start) <= 2
            or dp[start + 1][end - 1]
        ):
            dp[start][end] = True
            current_list.append(s[start: end + 1])
            dfs_backtracking_with_dp(result, s, end + 1, current_list, dp)
            current_list.pop()