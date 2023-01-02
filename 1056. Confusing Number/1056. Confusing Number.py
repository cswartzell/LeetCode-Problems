# 01-01-2022 Leetcode 1056. Confusing Number
# https://leetcode.com/problems/confusing-number/description/

# Just for fun, lets NOT convert to chars or string


class Solution:
    def confusingNumber(self, n: int) -> bool:
        n_forward = n
        n_backward = 0
        while n:
            next_digit = n % 10
            n //= 10
            if next_digit in {2, 3, 4, 5, 7}:
                return False
            elif next_digit == 6:
                next_digit = 9
            elif next_digit == 9:
                next_digit = 6
            n_backward *= 10
            n_backward += next_digit

        return n_forward != n_backward
