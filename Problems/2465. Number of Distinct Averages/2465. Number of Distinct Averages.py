# 01-09-2023 Leetcode 2465. Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/description/


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # return len(set((x + y)/2 for x, y in zip(sorted(nums)[:len(nums)//2], sorted(nums, reverse = True)[:len(nums)//2])))
        return len(
            set(
                (sorted(nums)[i] + sorted(nums, reverse=True)[i]) / 2
                for i in range(len(nums) // 2)
            )
        )

        # nums.sort()
        # num_averages = set()
        # for i in range(len(nums) // 2):
        #     num_averages.add(  (nums[i] + nums[len(nums) - 1 - i]) / 2  )
        # return len(num_averages)
