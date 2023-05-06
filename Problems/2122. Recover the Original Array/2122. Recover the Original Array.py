# 04-08-2023 Leetcode 2122. Recover the Original Array
# https://leetcode.com/problems/recover-the-original-array/description/

from collections import Counter


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        smallest, largest = nums[0], nums[-1]
        nums_counter = Counter(nums)
        knums = list(nums_counter.keys())

        for knum in knums[1:]:
            # technically this is 2k here, but thats less useful.
            # Lets say K = 2k
            K = knum - smallest
            if K & 1 or knum not in nums_counter or largest - K not in nums_counter:
                continue

            ans = []
            numsc = nums_counter.copy()

            for num in knums:
                # already took last of this number and counted for it
                if numsc[num] == 0:
                    continue
                if num + K not in numsc or numsc[num + K] == 0:
                    break

                count = min(numsc[num], numsc[num + K])

                numsc[num] -= count
                numsc[num + K] -= count
                ans += [num + K // 2] * count

            if len(ans) == len(nums) // 2:
                return ans
