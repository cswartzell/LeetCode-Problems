# 02-01-2024 Leetcode 2966. Divide Array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2024-02-01
# Time: 11 mins Challenge: Dead easy

# Divide nums into n/3 sized arrays (must be divisible by 3 to do this)
# Each subarray can have at most a difference of k amongst its members. 
# If k is 4 this DOES NOT MEAN [4,8,12] is acceptable. The rule holds 
# for all three, not progressive.
# Return an empty array if not possible.  

# Is this NOT just sort, divide into arrays of len 3 and see if they are each valid?
# We dont have to check the middle member of each subarray. If the smallest and largest
# value are within k of eachother, then of course the middle is as well. 

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # base case for length
        if len(nums)%3 != 0:
            return []
        
        sorted_nums = sorted(nums)
        ans = []
        
        for i in range(0, len(sorted_nums), 3):
            if sorted_nums[i + 2] - sorted_nums[i] <= k:
                ans.append([sorted_nums[i], sorted_nums[i+1], sorted_nums[i+2]])
            else:
                return []

        return ans
