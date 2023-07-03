# 07-02-2023 Leetcode 859. Buddy Strings
# https://leetcode.com/problems/buddy-strings/description/

#Can we do better than O(n**2)? Thats the trivial solution. 
# Yes, obvously. Compare the two letter by letter. If there are
# only two points that are different, then does swapping the two
# error locations result in the goal. Trivial indeed.

#Ah, and I was tripped up. If the two strings are the same and there is
# at least one letter that is included twice in the word, you can trivially
# swap those two! Darn

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        #NOT given
        if len(s) != len(goal):
            return False

        # Words are same, but there is at least one letter included more than once
        # such that it can be trivially swapped:
        if s == goal:
            return max(collections.Counter(s).values()) > 1

        errors = []
        for idx in range(len(s)):
            if s[idx] != goal[idx]:
                errors.append(idx)
            if len(errors) > 2:
                return False

        if len(errors) != 2:
            return False

        return s[errors[0]] == goal[errors[1]] and s[errors[1]] == goal[errors[0]]