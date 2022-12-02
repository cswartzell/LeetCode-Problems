#12-1-2022 LeetCode 27. Remove Element
# https://leetcode.com/problems/remove-element/

#Trivial in python right? Or does rebuilding
#the list in O(n) violates the spirit of the challenge?
#Lets try a hacky "pretend we cant just use replace or remove
#on a list and modify it as we go without slicing"

#linearly scan til we find a copy of the element we want to remove,
# Add 1 to shift_left, continue linearly scanning right, shifting each
#element shift_left toward the left. Increase shift left as more
#of the target is discovered. Return the string sliced[:shift_left]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # shift_left = 0
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         shift_left += 1
        #         continue
        #     if i >= shift_left:
        #         nums[i-shift_left] = nums[i]
        # return len(nums) - shift_left

        #this seems bugged? It def reassigns vals of nums to nums less val...
        #but the reporting lists values IN nums that arent there in the inspector
        #I guess this bugs the checking algo
        # nums = [x for x in nums if x != val]
        # return len(nums)