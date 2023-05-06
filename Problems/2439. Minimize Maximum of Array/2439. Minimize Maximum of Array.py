# 04-085-2023 Leetcode 2439. Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/description/

# keep making the operation til the list is monotonically decreasing guarentees the solution.
# you COULD terminate early, but im not sure how youd tell


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pre_sum = 0
        min_max = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            min_max = max( min_max, math.ceil(pre_sum/(i + 1)))
        return min_max

        #I maintain that this works, but is less than ideal.
        # # return math.ceil(sum(nums)/len(nums))
        # i = 1
        # while i < len(nums):      
        #     if nums[i] > nums[i-1]:        #not monotonically decreasing order          
        #         num_sum = (nums[i] + nums[i-1])
        #         nums[i] = num_sum //2
        #         nums[i-1] = num_sum - nums[i]
        #         i = max(1, i - 1)
        #         continue
        #     i += 1

        # return max(nums)