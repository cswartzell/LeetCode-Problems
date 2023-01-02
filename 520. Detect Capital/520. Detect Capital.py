# 01-01-2023 Leetcode 520. Detect Capital
# https://leetcode.com/problems/detect-capital/description/


class Solution:
    def detectCapitalUse(self, word) -> bool:
        # Yes, its terrible on purpose. Golf.
        # return set(word[1:]).intersection(set(string.ascii_uppercase)) == set() or set(word).intersection(set(string.ascii_lowercase)) == set()

        if len(word) == 1:
            return True

        # Flag if word is ALLCAPS
        rest_caps = word[1] in string.ascii_uppercase

        # To do the minimum amount of processing, we split into two cases here.
        # Sure, with a single logical operator this could be just one line, but then we
        # are doing that operation on each loop. Why not just check once?

        if rest_caps:
            for i in range(len(word)):
                if word[i] not in string.ascii_uppercase:
                    return False
        else:
            for i in range(1, len(word)):
                if word[i] in string.ascii_uppercase:
                    return False

        return True
