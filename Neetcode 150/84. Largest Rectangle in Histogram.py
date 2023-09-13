# 09-12-2023 Neetcode 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# Time: INFINITY- MEMORIZE THIS ONE. Too hard to originate. COMMONLY ASKED

# I really dont think I ever could have originated the solution to this.
# At least not the O(n) solution. The O(n**2) is trivial
# This is really a "gotta memorize it" one, and I find that obnoxious.

# I dont even really remember the answer... as long as its monotonically increasing
# push the index

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]

        for i in range(len(heights)):
                while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                    current_height = heights[stack.pop()]
                    current_width = i - stack[-1] - 1
                    max_area = max(max_area, current_height * current_width)
                stack.append(i)
        
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        
        return max_area
