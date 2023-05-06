# 04-29-2023 Leetcode 258. Add Digits
# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        # while num > 9:
        #     num = sum(int(x) for x in str(num))
        # return num
        
        # while num > 9:
        #     new_num = 0
        #     while num:
        #         new_num += num % 10
        #         num //= 10
        #     num = new_num
        # return num
        
        