# 04-19-2023 Leetcode 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/description/

# sliding window?


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # arr = [0 for _ in range(len(s))]
        arr = []
        stack = []
        for i in range(len(s)):
            arr.append(0)
            if s[i] == "(":
                stack.append(i)
            elif stack:
                match = stack.pop()
                arr[i], arr[match] = 1, 1

        longest = 0
        i = 0
        while i < len(arr):
            consecutive = 0
            while i < len(arr) and arr[i] == 1:
                consecutive += 1
                i += 1
            i += 1
            longest = max(longest, consecutive)

        return longest
