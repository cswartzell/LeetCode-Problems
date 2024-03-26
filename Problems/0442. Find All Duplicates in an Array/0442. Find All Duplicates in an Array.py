# 03-23-2024 Leetcode 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/?envType=daily-question&envId=2024-03-25
# Time: 30, challenge: 4/10

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]
        for idx in range(len(nums)):
            nums[idx] = abs(nums[idx])
        
        return ans