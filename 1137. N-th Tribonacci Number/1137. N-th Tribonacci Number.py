# 01-30-2023 Leetcode 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/description/

# Trivial


class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0, 1, 1]
        if n < 3:
            return fib[n]
        for _ in range(n - 2):
            fib[0], fib[1], fib[2] = fib[1], fib[2], fib[0] + fib[1] + fib[2]

        return fib[2]
