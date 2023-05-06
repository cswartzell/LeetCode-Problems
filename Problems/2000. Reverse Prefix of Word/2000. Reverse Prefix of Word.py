# 03-19-2023 Leetcode 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/description/

# I could do this with array iteration but lets golf


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        return word[idx::-1] + word[idx + 1 :] if idx != -1 else word
