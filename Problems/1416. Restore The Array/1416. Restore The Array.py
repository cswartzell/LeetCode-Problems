# 04-19-2023 Leetcode 1416. Restore The Array
# https://leetcode.com/problems/restore-the-array/


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * (len(s) + 1)

        def DFS(i):
            if dp[i]:
                return dp[i]
            if s[i] == "0":
                return 0
            if i == len(s):
                return 1

            count = 0
            j = i + 1
            while j <= len(s) and int(s[i : j + 1]) <= k:
                count += DFS(j)
                j += 1
            dp[i] = count
            return count

        return DFS(0)

        # dp = [0]*len(s)
        # first_skipped = 0
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == "0":
        #         if not first_skipped:
        #             first_skipped = i
        #         continue
        #     if first_skipped and int(s[i:first_skipped + 1]) >  k:
        #         return 0

        #     dp[i] = 1
        #     j = max(i + 1, first_skipped+1)
        #     while j < len(s) and int(s[i:j+1]) <= k:
        #         dp[i] += dp[j] % (10**9 + 7)
        #         j += 1
        #     first_skipped = 0

        # return dp[0]
