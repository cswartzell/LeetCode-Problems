"""03-12-2022 Leetcode 20. Valid Parentheses"""
import queue


class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = queue.LifoQueue()
        for char in s:
            if char == "{" or char == "(" or char == "[":
                open_stack.put(char)
            else:
                last_opened = open_stack.get()
                if char == "}" and last_opened != "{":
                    return False
                if char == "]" and last_opened != "[":
                    return False
                if char == ")" and last_opened != "(":
                    return False
        return True


stringy = "(({[[()]]}))"
truedat = Solution.isValid(stringy)
print(truedat)
