# 02-01-2023  Leetcode 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

# I dont think there is a more clever way to do this other than sorting...
# Can either sort(abs(x) for x in nums) first, or just square first then sort
# Its O(n) either way


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x**2 for x in nums)
