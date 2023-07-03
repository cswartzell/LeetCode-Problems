# 06-24-2023 Leetcode 1027. Longest Arithmetic Subsequence
# https://leetcode.com/problems/longest-arithmetic-subsequence/description/

# Take it or dont?

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        ans = 0
        
        for R in range(1, len(nums)):
            for L in range(R):
                dp[R][nums[R] - nums[L]] = dp[L][nums[R] - nums[L]] + 1
                if dp[R][nums[R] - nums[L]] > ans:
                    ans = dp[R][nums[R] - nums[L]]
        return ans + 1