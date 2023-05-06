# 02-14-2023 Leetcode 989. Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/description/

# I actually question how I am supposed to go about this. Like... obviously
# I can just use built in tools to cast it, performt he math, then convert
# it back to an array form. Thats too easy though.
# Ok, its already an array of ints. How about we conver k to an array,
# then do addition digit by digit/index by index with a carry value.
# That way we are at least manually doing something.


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # k_array = list(str(k)[::-1])
        k_array = []
        while k:
            k_array += [k % 10]
            k //= 10

        if len(num) < len(k_array):
            num = [0] * (len(k_array) - len(num)) + num

        elif len(k_array) < len(num):
            k_array = k_array + [0] * (len(num) - len(k_array))

        num.reverse()

        carry = 0
        for i in range(len(num)):
            carry += num[i] + k_array[i]
            num[i] = carry % 10
            carry //= 10

        if carry:
            num += [1]

        # why not, a different method of revesing while we are at it
        return num[::-1]
