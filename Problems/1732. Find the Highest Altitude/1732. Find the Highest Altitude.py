# 06-30-2023 Leetcode 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/description/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # curr_a = 0
        # max_a = curr_a
        # for step in gain:
        #     curr_a += step
        #     max_a = max(max_a, curr_a)
        # return max_a
        return max(accumulate(gain, initial= 0))