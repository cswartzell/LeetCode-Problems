# 11-27-2022 LeetCode 446. Arithmetic Slices II - Subsequence
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

# Why so many Hard problems this week?

# Ok, we have up to 1000 inputs spanning a range of ... 4 byte ints.
# Well there goes my first idea.

# I literally have no idea. Maybe DP of some sort. If there is a run
# spanable by 2, then half the run (within one) is spanable by 4...

# Ok, so building top down: any x are in the same arithmatic class
# if x % class = 0. So we could work our way from the largest given
# int to the smallest, starting by modding them into classes:
# "Is it divisible by sevens? How about sixes?"
# We can then simplify these classes by dividing each number by the
# class number. Arithmetic sequences would then just be numeric
# sequences:
# [21,24,25,28,30,31,35,37,49,50,51,56,63] % 7 == 0 yields
# [21,28,35,49,56,63] / 7 = [3,4,5,7,8,9], so we can just see the arithmetic
# sequences. [3,4,5] [7,8,9]
# Using mathemagic we could speed this up by breaking dwon the classes
# into composites. The sequence thats made of things mod 4 is also made
# of mod2 subsequences. Surely there is some logic that can make this work
# but it seems like it might be tricky with off by one errors.

# note this includes subsequences where the diference is ZERO


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # use defaultdict(int) to easily get the difference in arithmetic subsequences ending with
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(i):

                # We are looking for the number of elements before j in the arithmetic subsequence that has nums[j]-nums[i] as difference.
                dif = nums[j] - nums[i]

                # Simply add it to the result.
                res += dp[j][dif]

                # Increase the number of elements in arithmetic subsequence at i with this dif.
                dp[i][dif] += dp[j][dif] + 1
        return res
