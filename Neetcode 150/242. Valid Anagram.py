# 09-11-2023 Leetcode 0242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
# Time: 60 seconds

# Trivial with or without Python Counter. Could just do the same
# using a standard dict, or even binary flag array


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)