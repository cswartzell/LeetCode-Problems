# 03-11-2024 Leetcode 0243. Shortest Word Distance
# https://leetcode.com/problems/shortest-word-distance/
# Time: 10 mins Challenge: 2/10

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_idxs = collections.defaultdict(list)
        for idx, word in enumerate(wordsDict):
            word_idxs[word].append(idx)
        
        w1i, w2i = 0, 0
        min_dist = 10**5
        while w1i < len(word_idxs[word1]) and w2i < len(word_idxs[word2]):
            min_dist = min( min_dist, abs(word_idxs[word2][w2i] - word_idxs[word1][w1i]))
            if word_idxs[word1][w1i] < word_idxs[word2][w2i]:
                w1i += 1
            else:
                w2i += 1

        return min_dist
