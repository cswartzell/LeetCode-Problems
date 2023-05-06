# 03-20-2023 Leetcode 2348. Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

# each zero in a row contributes to permutations of zero filled subarrays
# This adds the nth triangular number to the sum of subs, for n zeros in a row


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        zeros = 0

        # Need to go one more in case last element is a zero. In a for, we wont
        # hit both conditions in one iteration. Add an arbitrary nonzero to clear
        for x in nums + [1]:
            if x == 0:
                zeros += 1
            else:
                ans += (zeros * (zeros + 1)) // 2 if zeros else 0
                zeros = 0
        return ans
