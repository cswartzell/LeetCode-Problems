"""02-15-2022 Leetcode 231. Power of Two"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return(n in (set(2**x for x in range(-31,32))))

        return n & (-n) == n if n != 0 else 0
        # interstingly this is the clever and with its 2s compliment solution
        # and is NO FASTER than my dumn "generate the powers of 2 and search set"

        return bin(n).count("1") == len(bin(n)) - 2
