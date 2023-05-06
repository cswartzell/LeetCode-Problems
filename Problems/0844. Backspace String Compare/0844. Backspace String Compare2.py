# 01-02-2023 Leetcode 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        skip_s = 0
        skip_t = 0

        s_i = len(s) - 1
        t_i = len(s) - 1

        while s_i >= 0 and t_i >= 0:
            while s_i >= 0 and s[s_i] == "#":
                skip_s += 1
                s_i -= 1
            while sk




        # s_stack = []
        # t_stack = []

        # for i in range(len(s)):
        #     if s[i] != "#":
        #         s_stack.append(s[i])
        #     elif s_stack:
        #         s_stack.pop()
        
        # for i in range(len(t)):
        #     if t[i] != "#":
        #         t_stack.append(t[i])
        #     elif t_stack:
        #         t_stack.pop()

        # return s_stack == t_stack 
            