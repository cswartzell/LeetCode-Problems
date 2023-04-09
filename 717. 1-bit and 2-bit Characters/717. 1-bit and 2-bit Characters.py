# 04-06-2023 Leetcode 717. 1-bit and 2-bit Characters
# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits.pop()
        odd_ones = 1
        while bits and bits[-1] == 1:
            bits.pop()
            odd_ones = (odd_ones + 1) % 2
        return odd_ones
