"""05-06-2022 Leetcode 456. 132 Pattern"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # i = 10**9 + 1
        j = -(10 ** 9) - 1
        nums = nums[::-1]
        k = {nums[0]}

        for x in nums:
            # find first j>k
            if x > min(k) and j < -(10 ** 9):
                j = x
                k = {x for x in k if x < j}
                continue
            # update j to new larger value, update k to last j
            if x > j and j > -(10 ** 9) - 1:
                k.add(j)
                j = x
                continue
            # if we found a j, we are only looking for an i smaller than j
            if x < j and x < max(k) and j > -(10 ** 9) - 1:
                return True
            if x < j or j < -(10 ** 9):
                k.add(x)
        return False
