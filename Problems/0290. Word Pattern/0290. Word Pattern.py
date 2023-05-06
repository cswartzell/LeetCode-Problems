# 12-31-2022 Leetcode 290. Word Pattern
# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern, s) -> bool:
        s = s.split(" ")
        pattern = [x for x in pattern]

        if len(set(s)) != len(set(pattern)) or len(s) != len(pattern):
            return False

        sp_dict = dict()

        for i in range(len(s)):
            if s[i] not in sp_dict:
                 sp_dict[s[i]] = pattern[i]
            elif sp_dict[s[i]] != pattern[i]:
                return False
        
        return True
        # return set(sp_dict.values()) == set(pattern)

