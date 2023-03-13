# 03-12-2023 Leetcode 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Two pointers. Set L equal to index 0 and R to 1. Advance both until
# the values are the same, at which point leave L behind. Continue to
# advance R ...

# No wait, THREE pointers. One is a write pointer, then a L and to discover
# blocks of contiguous chars


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Base case of a single char is a given.
        # write, L, R = 0, 0, 0
        # while R < len(nums):
        #     write += 1
        #     while R < len(nums) - 1 and nums[L] == nums[R]:
        #         R += 1
        #     L = R
        #     R += 1
        #     nums[write] = nums[L]

        # return write + 1

        write = 1
        for R in range(1, len(nums)):
            if nums[R - 1] != nums[R]:
                nums[write] = nums[R]
                write += 1
        return write
