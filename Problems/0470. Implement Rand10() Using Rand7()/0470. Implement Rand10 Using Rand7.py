# 05-01-2023 Leetcode 470. Implement Rand10() Using Rand7()
# https://leetcode.com/problems/implement-rand10-using-rand7/description/

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        lo = 7
        while lo > 5:
            lo = rand7()
        
        hilo = 4
        while hilo == 4:
            hilo = rand7()

        return lo if hilo < 4 else lo + 5