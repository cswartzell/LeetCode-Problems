# 12-1-2022 LeetCode 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# an extension of the three sum problem. I solved that one
# on my own in kind of a whacky way. Im going to try the
# recomended two pointer technique here I guess. O(n**2)
# The brute force solution of course would be O(n**3)
# Oh. Which with only 500 nums really isnt that bad.
# "Only" 1.24m combinations.


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        closest_sum = 30000001
        for i in range(len(sorted_nums) - 1):
            j, k = i + 1, len(sorted_nums) - 1

            while j != k:
                sumd = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if abs(target - sumd) < abs(target - closest_sum):
                    closest_sum = sumd
                if sumd < target:
                    j += 1
                elif sumd > target:
                    k -= 1
                # if the "Closest" is zero away from target, we cant beat that
                else:
                    return closest_sum
        return closest_sum
