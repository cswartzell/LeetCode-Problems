# 04-08-2023 Leetcode 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/description/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda x, y: x ^ y, range(start, start + 2 * n, 2))
