# 03-12-2023 Leetcode 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/description/


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Lets start by mapping vals to their indecies in nums2 so we dont have
        # to repeatedly scan
        j_dict = collections.defaultdict()
        for j, val in enumerate(nums2):
            j_dict[val] = j

        # There doesnt seem to be a point in precomputing the next greater... not if its a
        # linear scan anyhow. May as well just do the linear scan when we need to
        # Besides, we only need to do it for vals in nums1, so precomputing all
        # of num2 would be a waste. We COULD save time with a binary search...
        # but then we'd need to create an ordered 2d array with "all numbers after i"
        # for each i to search on.
        ans = []
        for val in nums1:
            j = j_dict[val]  # This is the index in nums2 that matches the val in nums1
            NGE = 1000001
            for i in range(j + 1, len(nums2)):
                if nums2[i] > nums2[j] and nums2[i] < NGE:
                    NGE = nums2[i]
                    break
            ans.append(NGE if NGE != 1000001 else -1)

        return ans
