# 04-05-2023 Leetcode 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/

# I think this can be done with two pointers: L and R start at zero,
# advance R and count number of zeros encountered. Once num_zeros == k + 1
# we know we have a substring with ONE too many zeros. Record max(prev_max, R-L -1)
# as we could have kept the previous srting with k zeros and flipped them. Now
# advance L until there num_zeros ==k, meaning we could continue from here.
# This may be a string of k zeros and no ones. Repeat til R > len(nums)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeros = 0
        L, R = 0, 0
        ans = 0
        while R < len(nums):
            while R < len(nums) and num_zeros <= k:
                if nums[R] == 0:
                    num_zeros += 1
                R += 1

            ans = max(ans, R - L - 1)

            while num_zeros > k:
                if nums[L] == 0:
                    num_zeros -= 1
                L += 1
        return ans if num_zeros > k else max(ans, R - L)
