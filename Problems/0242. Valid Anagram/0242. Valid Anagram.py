# 12-09-2022 Leetcode 0242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

# Trivial with or without Python Counter. Could just do the same
# using a standard dict, or even binary flag array


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
