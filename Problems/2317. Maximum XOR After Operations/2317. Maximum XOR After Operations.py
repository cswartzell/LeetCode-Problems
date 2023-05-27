# 05-27-2023 Leetcode 2317. Maximum XOR After Operations
# https://leetcode.com/problems/maximum-xor-after-operations/description/

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x | y, nums)