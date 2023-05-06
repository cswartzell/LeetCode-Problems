# 12-09-2022 Leetcode 66. Plus One
# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while i >= 0 and carry:
            carry = False
            if digits[i] == 9:
                if i == 0:
                    digits = [1, 0] + digits[1:]
                    break
                digits[i] = 0
                carry = True
            else:
                digits[i] += 1
                break
            i -= 1

        return digits
