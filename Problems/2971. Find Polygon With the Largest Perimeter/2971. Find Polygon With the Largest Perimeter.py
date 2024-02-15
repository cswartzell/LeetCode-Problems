# 02-14-2024 Leetcode Daily 2971. Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/?envType=daily-question&envId=2024-02-15
# Time: 9mins Challenge: 2/10 

# Sort, prefix sum, compare sum at last index to val at last index. If larger, return sum
# If smaller, pop last val and last prefix sum and repeat. Do until found or len(sides) < 3


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # nums_sorted = sorted(nums)
        # prefix_sum = [nums_sorted[0]]
        # for num in nums_sorted[1:]:
        #     prefix_sum.append(prefix_sum[-1] + num)

        # len_idx = len(prefix_sum) - 2
        # curr_longest = len(nums_sorted) - 1

        # while curr_longest >= 2:
        #     if prefix_sum[len_idx] > nums_sorted[curr_longest]:
        #         return prefix_sum[len_idx + 1]
        #     else:
        #         len_idx -= 1
        #         curr_longest -= 1
        
        # return -1

        nums = sorted(nums)
        prefix_sum = sum(nums)

        idx = len(nums) - 1

        while idx >= 2:
            if prefix_sum - nums[idx] > nums[idx]:
                return prefix_sum
            prefix_sum -= nums[idx]
            idx -= 1
        
        return -1