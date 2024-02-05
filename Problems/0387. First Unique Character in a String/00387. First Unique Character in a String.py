# 02-04-2024 0387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/?envType=daily-question&envId=2024-02-05
# Time: 5 mins Challenge: 1/10

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Verbose simple 2 pass. I forewent Counter just to be more basic
        # count = {}
        # for char in s:
        #     count[char] = count.get(char, 0) + 1
        # for idx, char in enumerate(s):
        #     if count[char] == 1:
        #         return idx

        # return -1

        # as dicts are ordered now, you can do this in one pass:
        # Dicts arent directly indexable though, so you still
        # have to retrieve its contents
        one_count = {}
        plural = set()

        for idx, char in enumerate(s):
            if char not in one_count and char not in plural:
                one_count[char] = idx
            elif char in one_count:
                del one_count[char]
                plural.add(char)
        
        return list(one_count.values())[0] if one_count != dict() else -1
