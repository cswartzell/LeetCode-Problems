"""05-05-2022 Leetcode 8. String to Integer (atoi)"""

import string


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        ans = 0
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        x, y = 0, 0
        # Appartently string.digits includes fucking period as the radix point. Absurd.

        for x in range(len(s)):
            if s[x] == " ":
                continue
            elif s[x] == "-":
                sign *= -1
                break
            elif s[x] == "+":
                break
            elif s[x] in digits:
                x -= 1
                break
            else:
                return 0

        for y in range(x + 1, len(s)):
            if s[y] in digits:
                ans = (ans * 10) + ord(s[y]) - ord("0")
                # Cheating to use built in char to i? I could just as well write a dictionary
                # with the digit chars as keys and their value as the ... value

                # Speaking of cheating, we are allowing our int to go OVER 2*31 before checking it
                # The problem does not state that it can never go over, just if it will to cap it
                # The "better" solution would be to subtract our ans from intmax and see if multiplying
                # by ten, and after that if adding the next digit, is over this difference.
                # I'm curious how interviewers want this stated. The cumbersome method shows you can
                # think of edge cases, but then again we are not presented with the limitation... we are
                # inventing it from a mere suggestion about overflow. I actually think ignoring language
                # features and "doing it the hard way" does not show cleverness, particularly if we are
                # avoiding an imaginary pitfall. Asking about it might be better.
                if ans > (2 ** 31 - 1) and sign == 1:
                    ans = 2 ** 31 - 1
                    break
                if ans > (2 ** 31) and sign == -1:
                    ans = 2 ** 31
                    break
            else:
                break

        return ans * sign
