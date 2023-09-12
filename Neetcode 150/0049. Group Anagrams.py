# 09-11-2023 Neetcode 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Time: 


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)
        for word in strs:
            ans_dict[tuple(sorted(list(word)))].append(word)
        return list(ans_dict.values())


        # return (d:=dict())

        # # anagroups = collections.defaultdict(list)
        # # for word in strs:
        # #     # anagroups["".join(sorted(word))].append(word)
        # #     anagroups[tuple(sorted(word))].append(word)
        # # return anagroups.values()