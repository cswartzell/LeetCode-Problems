# 04-22-2023 Leetcode 1312. Minimum Insertion Steps to Make a String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/


class Solution:
    def minInsertions(self, s: str) -> int:
        # 1d bottom-up
        N = len(s)
        dp = [0] * (N + 1)
        for start in reversed(range(N)):
            prev = 0
            for end in range(start, N):
                tmp = dp[end]
                if s[start] == s[end]:
                    dp[end] = prev
                else:
                    dp[end] = 1 + min(dp[end], dp[end - 1])
                prev = tmp
        return dp[N - 1]

        # 2d bottom-up
        N = len(s)
        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for start in reversed(range(N)):
            for end in range(start, N):
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1]
                else:
                    dp[start][end] = 1 + min(dp[start + 1][end], dp[start][end - 1])

        return dp[0][N - 1]

        # top-down
        @cache
        def dfs(start, end):
            if start > end:
                return 0
            if start == end:
                return 0
            if s[start] == s[end]:
                return dfs(start + 1, end - 1)
            else:
                return 1 + min(dfs(start + 1, end), dfs(start, end - 1))

        N = len(s)
        return dfs(0, N - 1)
