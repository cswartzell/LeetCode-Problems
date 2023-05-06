# 12-16-2022 Leetcode 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=study-plan&id=level-1

#Trivial

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        return nums