# 04-19-2023 Leetcode 2134. Minimum Swaps to Group All 1's Together II
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

# We need ALL the ones in the starting array, meaning we can leave out
# any number of added zeros on either side. As its circular, these zeros
# are contiguous and outside the starting group. We then merely count
# the remaining zeros IN the starting group


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        max_zeros = 0
        i = -len(nums)
        curr_zeros = 0
        twice_ones = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
                twice_ones += 1
            curr_zeros = 0
            while i < len(nums) and nums[i] == 0:
                curr_zeros += 1
                i += 1
            max_zeros = max(max_zeros, curr_zeros)

        return max(len(nums) - max_zeros - twice_ones // 2, 0)
