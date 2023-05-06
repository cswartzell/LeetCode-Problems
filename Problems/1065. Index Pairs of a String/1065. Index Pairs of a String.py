# 04-30-2023 Leetcode 1065. Index Pairs of a String
# https://leetcode.com/problems/index-pairs-of-a-string/description/

# Efficiency? I guess make a Trie. Hardly and easy problem
# IRL id just use regex
# class Trie:
#     def __init__(self):
#         self.root = {}
#         self.WORD_DELIM = '#'

#     def addWord(self, word):
#         cur = self.root
#         for c in word:
#             if c not in cur:
#                 cur[c] = {}
#             cur = cur[c]
#         cur[self.WORD_DELIM] = word

#     def addWords(self, words):
#         for word in words:
#             self.addWord(word)

# class Solution:
#     def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
#         trie = Trie()
#         trie.addWords(words)
#         res = []
#         for i in range(len(text)):
#             cur = trie.root
#             for j in range(i, len(text)):
#                 if not cur or text[j] not in cur:
#                     break
#                 cur = cur[text[j]]
#                 if trie.WORD_DELIM in cur:
#                     res.append([i,j])
#         return res


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        words = set(words)
        for i in range(len(text) + 1):
            for j in range(i + 1, len(text) + 1):
                if text[i:j] in words:
                    ans.append([i, j - 1])
        return ans
