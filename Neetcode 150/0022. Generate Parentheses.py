# 09-12-2023 Neetcode 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/
# Time: 30 mins

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        stack = [(["("], 1)]
        while stack:
            curr_string, open_count = stack.pop()
            if len(curr_string) == 2 * n:
                ans.append("".join(curr_string))
                continue
            if open_count < n and open_count + 1 < 2*n - len(curr_string):
                stack.append((curr_string + ["("], open_count + 1))
            if open_count > 0:
                stack.append((curr_string + [")"], open_count - 1))
        
        return ans

