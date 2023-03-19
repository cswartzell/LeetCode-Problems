# 12-09-2022 Leetcode 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/

# Isnt this just XOR?
# WRONG REVERSE MORON
# READ THE DAMNED PROMPTS
# This literally means reverst the ORDER


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans <<= 1
            ans += n & 1
            n >>= 1
        return ans

        # return n^(2**32-1)
