# 03-01-2024 Leetcode 136. Single Number
# https://leetcode.com/problems/single-number/
# Time: 2 Challenge 1/10

# Trivial

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x^y, nums)