# 12-08-2022 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

# huh. Obviously yes, there are trivially simple ways to do this. It can be done
# in one line with just a single function call. But how to do it efficiently?
# insertion into a list is not fast. Moving the slice is not fast. Can we do
# something clever? Swap elements maybe?

# nums1 is the output, so we can use numsj as a holding space


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i, x in enumerate(nums2):
                nums1[i] = x
            return
        if n == 0:
            return

        i, j, k = 0, 0, 0
        knums1 = nums1[: len(nums1) - len(nums2)]

        while i < len(nums1):
            if j > len(nums2) - 1 or k < len(knums1) and knums1[k] < nums2[j]:
                nums1[i] = knums1[k]
                k += 1
            elif k > len(knums1) - 1 or j < len(nums2) and knums1[k] >= nums2[j]:
                nums1[i] = nums2[j]
                j += 1
            i += 1
