# 05-01-2023 Leetcode 330. Patching Array
# https://leetcode.com/problems/patching-array/description/

# Hmm... so you MUST have 1 and 2 at least. After that... you can get a way with a lot
# using just some random digits. 1,2,4 covers through 7 without needing 3, but 1,2,5
# cant produce a 4.

# I wonder if its something like the fibonacci sequence, starting with 1,2 and you need
# ANY number equal to or less than the sum of all current nums? The sum of all current nums
# is the most you can make so you do indeed need a higher number to continue. And if you
# WERE able to cover to say n, adding n iteslf clearly allows you to cover n+1, n+2... n + n

# So, while the sum of the set we are building is less than our target, pop the next num. If the next
# num is less than our current sum, add it to our sum. If GREATER, then add sum to itself, and add
# one to our counter of "nums needed to add". Repeat until our sum is greater than our target
# noting that this has nothing to do with the number of elements in nums. We may end early, we
# may need to add dozens beyond the end.


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        added = 0
        i = 0
        sumd = 0

        while sumd < n:
            if i < len(nums) and sumd >= nums[i] - 1:
                sumd += nums[i]
                i += 1
            else:
                sumd += sumd + 1
                added += 1

        return added
