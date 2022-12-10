# 12-09-2022 Leetcode 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

# Trivial.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        i = len(s) - 1
        len_last_word = 0
        while i >= 0 and s[i] == " ":
            i -= 1
        j = i
        while j >= 0 and s[j] != " ":
            j -= 1
        return i - j
