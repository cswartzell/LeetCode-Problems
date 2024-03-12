# 03-09-2024 Leetcode 2578. Split With Minimum Sum
# https://leetcode.com/problems/split-with-minimum-sum/
# Time: 6 mins Challenge: 2/10


class Solution:
    def splitNum(self, num: int) -> int:
        mnu = sorted([int(x) for x in str(num)])
        num1 = 0
        num2 = 0

        for idx, num in enumerate(mnu):
            if idx & 1:
                num1 *= 10
                num1 += num
            else:
                num2 *= 10
                num2 += num

        return num1 + num2
