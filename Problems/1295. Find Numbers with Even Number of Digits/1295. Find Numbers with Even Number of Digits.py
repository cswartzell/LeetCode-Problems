# 04-02-2023 Leetcode 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum((len(str(num)) + 1)&1 for num in nums)