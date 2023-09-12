# 09-12-2023 Neetcode 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/
# Time: 2 mins

class Solution:
    def isValid(self, s: str) -> bool:
        close = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char not in close:
                stack.append(char)
            else:
                if stack and stack[-1] == close[char]:
                    stack.pop()
                else: 
                    return False
        return stack == []
