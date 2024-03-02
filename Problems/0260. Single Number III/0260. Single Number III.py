# 03-01-2024 Leetcode 0260. Single Number III
# https://leetcode.com/problems/single-number-iii/
# Time: 45 Challenge: 9/10 

# I LOVE this problem.


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # axorb = functools.reduce(lambda x, y: x^y, nums)

        axorb = 0
        for num in nums:
            axorb ^= num

        first_dif_bit = 1
        while first_dif_bit < 32:
            if first_dif_bit & axorb:
                break
            first_dif_bit <<= 1

        a = 0
        for num in nums:
            if num & first_dif_bit:
                a ^= num
        return [a, axorb^a]
