# 04-22-2023 Leetcode 2231. Largest Number After Digit Swaps by Parity
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/


class Solution:
    def largestInteger(self, num: int) -> int:
        # even = {"0", "2", "4", "6", "8"}
        # strnum = str(num)
        # evens, odds = [], []

        # for digit in strnum:
        #     if digit in even:
        #         evens.append(digit)
        #     else:
        #         odds.append(digit)

        # evens.sort()
        # odds.sort()

        # return int("".join([evens.pop() if digit in even else odds.pop() for digit in strnum]))

        evens, odds = [], []
        numb = copy.copy(num)
        while numb:
            curr_digit = numb % 10
            numb //= 10
            if curr_digit & 1:
                odds.append(curr_digit)
            else:
                evens.append(curr_digit)

        evens.sort(reverse=True)
        odds.sort(reverse=True)

        ans = 0
        mul = 1
        while num:
            curr_digit = num % 10
            num //= 10
            if curr_digit & 1:
                ans += mul * odds.pop()
            else:
                ans += mul * evens.pop()
            mul *= 10

        return ans
