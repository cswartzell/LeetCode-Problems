# 11-13-2023 Neetcode 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Time: 20 mins

# First check if its not rotated/rotated a multiple of its len
# Then use binary search to find m where m > m + 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums) == 1:
            return nums[0]

        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L + R) //2
            if nums[M] > nums[0]:
                L = M + 1
            elif nums[M] > nums[max(M - 1, 0)]:
                R = M - 1
            else:
                return min(nums[M], nums[min(M+1, len(nums) - 1)])

            # if nums[R] > nums[M]:
            #     R = M - 1
            # elif nums[M] > nums[L]:
            #     L = M + 1
            # else:
            #     return min(nums[L], nums[M])
