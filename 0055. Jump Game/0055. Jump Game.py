# 12-26-2022 Leetcode 55. Jump Game
# https://leetcode.com/problems/jump-game/description/


# Huh. This actually seems like an easy. I guess this is DP.
# You could go crazy with like Union Find off the bat but there
# is no need when a simple O(n) solution like this works


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_pos = len(nums) - 1
        i = curr_pos - 1
        while i >= 0:
            if i + nums[i] >= curr_pos:
                curr_pos = i
            i -= 1
        return curr_pos == 0
