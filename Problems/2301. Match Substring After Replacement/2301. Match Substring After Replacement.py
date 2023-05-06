# 04-30-2023 Leetcode 2301. Match Substring After Replacement
# https://leetcode.com/problems/match-substring-after-replacement/

#This seems pretty easy...

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        sub_set = set(sub) #get it?
        s_sub_indeces = collections.defaultdict(list)
        for index, letter in enumerate(s):
            s_sub_indeces[letter].append(index)

        #may as well check
        if set(s_sub_indeces.keys()) != sub_set:
            return False

        mapping = {old: new for old, new in mappings}

        #Check starting from each match of the first letter, or its swap
        for s_idx in s_sub_indeces[sub[0]] + s_sub_indeces[mapping[sub[0]]]:
            
