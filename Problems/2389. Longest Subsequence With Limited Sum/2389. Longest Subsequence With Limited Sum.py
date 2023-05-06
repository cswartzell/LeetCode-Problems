# 12-25-2022 Leetcode 2389. Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

# caluculate the min subsequence from 0-num
# We can do this by sorting, then prefix sum
# a subsequence has an implied order, but because
# we are SUMMING these subsequences, the order cesaes to matter


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums = [0] + sorted(nums)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for x in queries:
            i = 1
            while i < len(nums) and nums[i] <= x:
                i += 1
            answer.append(i - 1)

        return answer
