# 12-31-2022 Leetcode 290. Word Pattern
# https://leetcode.com/problems/word-pattern/description/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_parts = set(pattern.split())
        map_char = {}
        map_word = {}

        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True
