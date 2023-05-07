# 04-01-2023 Leetcode 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/description/

#How to quickly zero in on the root? 
# Oh, duh. This is just binary search

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if num in {1,2}: return True
        
        # L, R = 0, num // 2
        # while L <= R:
        #     mid = L + (R - L)//2
        #     if mid**2 > num:
        #         R = mid - 1
        #     elif mid**2 < num:
        #         L = mid + 1
        #     else:
        #         return True
        # return False

        # return num in set(i**2 for i in range(46341))
        # return any(i**2 == num for i in range(46341))
        return any(map(lambda i: math.pow(i,2) == num, range(46341)))