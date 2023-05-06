# 01-31-2023 Leetcode 734. Sentence Similarity
# https://leetcode.com/problems/sentence-similarity/description/


class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarDict = collections.defaultdict(set)

        # It doesnt EXPLICITLY state that similarity is Symmetric
        for word1, word2 in similarPairs:
            similarDict[word1].add(word2)
            similarDict[word2].add(word1)

        for i in range(len(sentence1)):
            # if not (    (sentence1[i] == sentence2[i]) or (sentence2[i] in similarDict[sentence1[i]]) or (sentence1[i] in similarDict[sentence2[i]])    ):
            if not (
                (sentence1[i] == sentence2[i])
                or (sentence2[i] in similarDict[sentence1[i]])
            ):
                return False
        return True
