# 04-08-2023 Leetcode 760. Find Anagram Mappings
# https://leetcode.com/problems/find-anagram-mappings/description/


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [
            (num_at_idx := {num: i for i, num in enumerate(nums2)})[num1]
            for num1 in nums1
        ]
