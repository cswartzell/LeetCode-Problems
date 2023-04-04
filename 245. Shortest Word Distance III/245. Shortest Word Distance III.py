# 04-01-2023 Leetcode 245. Shortest Word Distance III
# https://leetcode.com/problems/shortest-word-distance-iii/description/


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # word_i = collections.defaultdict(set)
        # for i, word in enumerate(wordsDict):
        #     word_i[word].add(i)
        # big_list = list(itertools.combinations(word_i[word1].union(word_i[word2]), 2))
        # return min(abs(x - y) if x != y else 10**5 + 1 for x,y in itertools.product(word_i[word1],word_i[word2]))

        min_dist = 10**5 + 1
        # Complains "may be unbound. Good practice, but unnecessary as conditions guarentee it its true
        # prev_word, prev_idx = "0", 0
        # find first occurance
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1 or wordsDict[i] == word2:
                prev_word = wordsDict[i]
                next_word = word1 if prev_word != word1 else word2
                prev_idx = i
                break

        next_idx = prev_idx + 1
        while next_idx < len(
            wordsDict
        ):  # (and min_dist > 1) Could terminate early. More checks done than it saves probably
            if wordsDict[next_idx] == next_word:
                min_dist = min(min_dist, next_idx - prev_idx)
                prev_word, next_word = next_word, prev_word
                prev_idx = next_idx
            elif wordsDict[next_idx] == prev_word:
                prev_idx = next_idx
            next_idx += 1
        return min_dist
