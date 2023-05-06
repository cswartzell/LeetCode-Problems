# 04-20-2023 Leetcode 728. Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/description/

# Sure, we can test them all, but can we skip some?
# For instance, any number ending in anything BUT 0 or 5 wont be divisible BY 5
# Possible ending digits (note, no zero):
# 0: N/A
# 1: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 2: [2, 4, 6, 8]
# 3: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4: [2, 4, 6, 8]
# 5: [5]
# 6: [2, 4, 6, 8]
# 7: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 8: [2, 4, 6, 8]
# 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# So wait, I think there are 3 rules:
# If zero is a digit, bail
# If ANY of the digits are even, it must end in an even number
# If 5 is one of the digits, the last digit must be 5

# Using this shortcuts more than half the potential work


class Solution:
    def selfDividingNumbers(self, l: int, r: int) -> List[int]:
        # ans = []
        # for num in range(left, right + 1):
        #     last_digit = num % 10
        #     digitize = num * 1
        #     self_dividing = True
        #     while digitize:
        #         next_digit = digitize % 10
        #         if (next_digit == 0) or (next_digit == 5 and last_digit != 5) or (last_digit & 1 and not (next_digit & 1)) or num % next_digit != 0:
        #             self_dividing = False
        #             break
        #         digitize //= 10
        #     if self_dividing:
        #         ans.append(num)
        # return ans

        # ans = []
        # for num in range(left, right + 1):
        #     digitize = num
        #     self_dividing = True
        #     while digitize:
        #         next_digit = digitize % 10
        #         if next_digit == 0 or num % next_digit != 0:
        #             self_dividing = False
        #             break
        #         digitize //= 10
        #     if self_dividing:
        #         ans.append(num)
        # return ans

        return [
            n
            for n in range(l, r + 1)
            if all(c != "0" and n % int(c) == 0 for c in str(n))
        ]
