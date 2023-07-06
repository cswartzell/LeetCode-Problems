# 07-05-2023 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/


# Basic Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        curr_sum = 0
        min_size = 100001
        while R < len(nums):
            while R < len(nums) and curr_sum < target:
                curr_sum += nums[R]
                R += 1
            while L < len(nums) and L < R and curr_sum >= target:
                min_size = min(min_size, R - L)
                curr_sum -= nums[L]
                L += 1
        
        return min_size if min_size != 100001 else 0 
                