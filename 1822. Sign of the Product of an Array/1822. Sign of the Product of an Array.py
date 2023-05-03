# 05-02-2023 Leetcode 1822. Sign of the Product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        parity = reduce(lambda a, b: a * b, nums)
        return parity // abs(parity) if parity != 0 else 0
