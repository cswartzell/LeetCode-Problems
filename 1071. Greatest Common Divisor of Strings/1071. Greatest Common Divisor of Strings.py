# 01-31-2023 Leetcode 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

# What an odd question. Well, start with the shorter string and see if its
# len is a divisor of the two strings, and keep working backwards eliminating
# letters until thats true. Then... just check if it is? Eventually the str
# will be blank so return that


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # divisor = str1 if len(str1) <= len(str2) else str2

        # while len(divisor) > 0:
        #     # if len(str1) % len(divisor) == 0 and len(str1) % len(divisor) == 0:
        #     if divisor * (len(str1) // len(divisor)) == str1 and divisor * (len(str2) // len(divisor)) == str2:
        #         return divisor
        #     divisor = divisor[:len(divisor) - 1]

        # return ""

        return (
            str1[: math.gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""
        )
