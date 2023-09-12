# 09-11-2023 Neetcode 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Time: 60 seconds

# Could make my own counter if I wanted, iterate it manually etc


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return max(collections.Counter(nums).values()) > 1