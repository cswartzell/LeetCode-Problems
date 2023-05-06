# 04-07-2023 Leetcode 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # nums1, nums2 = set(nums1), set(nums2)
        # return [nums1-nums2, nums2-nums1]

        # this is weirdly faster. I think it doesnt convert to set each time, but resuses.
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]
