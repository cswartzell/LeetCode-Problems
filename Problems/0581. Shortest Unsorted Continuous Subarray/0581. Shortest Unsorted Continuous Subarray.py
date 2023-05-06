"""05-02-2022 Leetcode 581. Shortest Unsorted Continuous Subarray"""

# Cheesy Petes this could be tough if you don't start with
# "just sort it, then figure out what changed".


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        sorted_nums = sorted(nums)

        i = 0
        while i < len(nums) and nums[i] == sorted_nums[i]:
            i += 1
        j = len(nums)
        while j > 0 and nums[j - 1] == sorted_nums[j - 1] and j > i:
            j -= 1
        return j - i


tester = Solution()
print(tester.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
