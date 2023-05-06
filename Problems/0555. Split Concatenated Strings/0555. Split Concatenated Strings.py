# 04-09-2023 Leetcode 555. Split Concatenated Strings
# https://leetcode.com/problems/split-concatenated-strings/

# There are two choices for each string, and 1000 strings, so 2^1000
# THEN we can break any of these at any point for sum(len[str_i] for str_i i strings)
# Meaning: we cant just try it. Itd take eons.

#So, we need properties of the strings themselves. A string is either monotonic or its not

# Lexigraphical order goes char by char, so we MUST start with the "largest" char, regardless of
# any other choice: AAAZABCD permuted would always choose the Z first not caring what that does to the 
# rest of the string. I think we can take this "next char is the only one that matter" idea as the basis
# for our program. This would work great if the chars were unique... they arent. So we look in our set 
# find ALL remaining strings with the next highest letter. From all these we choose the one that has
# the NEXT highest letter adjacent to THAT one... recursively, til we find the correct string and orientation

# This seems... challenging. We can use a dict to store what strings have which chars 
# But the cut and looping thing just makes this harder. If we reverse a string and cut it to get say a Z
# we dont just discard that: we've chosen that this half goes at the end of the main string as well.
# We only get to make one cut though, so I guess ite not so bad? Can we still be greedy here?

# It may be handy to turn all strings into just lists of their numbers. Then we can make parallel strings
# that include not only the letters number, but add its neighbors values. 

#Do this for every string...

# Jesus, this is complicated. I hope there is a simple answer and Im just dumb.

# Ok, well lets just start: First, dict of sts with given letter in it
# Now pull all the words with the largest letter. For each, find the cut point and
# orientation so it is largest. Note the str may have MULTIPLE copies of the largest letter
#I hate this problem
# So for each index with the max starting letter, check its neighbors. NO WRAPPING

class Solution:
    # def splitLoopedString(self, strs: List[str]) -> str:
        # words_with = collections.defaultdict(list)
        # for idx in range(len(strs)):
        #     word_set = set()
        #     for letter in strs[idx]:
        #         if letter not in word_set:
        #             words_with[letter].append(idx)
        #             word_set.add(letter)
        #         if len(word_set) == 26:
        #             break
        
        # first_candidates = words_with[max(words_with.keys())]
    def splitLoopedString(self, strs):
        max_ch = max([max(s) for s in strs])
        strs = [max([s, s[::-1]]) for s in strs]
        output = ''.join(strs)
        for i, s in enumerate(strs):
            if max_ch not in s:
                continue
            l = ''.join(strs[i+1:]+strs[:i])
            for j in range(len(s)):
                if s[j] == max_ch:
                    output = max([output, s[j:]+l+s[:j], s[:j+1][::-1]+l+s[j+1:][::-1]])
        
        return output