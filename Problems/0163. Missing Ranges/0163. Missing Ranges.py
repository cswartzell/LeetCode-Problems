# 06-18-2023 Leetcode 163. Missing Ranges
# https://leetcode.com/problems/missing-ranges/description/

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # I am dumb. This is obviously too slow for sparse lists. 
        # nums = set(nums)
        # ans = []
        # x = lower
        # while x <= upper:
        #     if x not in nums:
        #         first_missing = x
        #         while x+1 <= upper and x+1 not in nums:
        #             x += 1
        #         ans.append([first_missing, x])
        #     x += 1
        # return ans
        
        # if len(nums) == 1:
        #     return []

        nums = [lower-1] + nums + [upper + 1]
        ans = []

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1] - 1:
                ans.append([nums[i]+1, nums[i+1]-1])
        
        return ans
