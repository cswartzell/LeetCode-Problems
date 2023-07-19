# 07-17-2023 Leetcode 1433. Check If a String Can Break Another String
# https://leetcode.com/problems/check-if-a-string-can-break-another-string/description/

# This seems all but trivial? Sort the two, one reversed, check by index?

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        # Not 100% you can cast a string as a list.
        # Obviously can do something else like [x for x in s1]
        s1list = sorted(list(s1))
        s2list = sorted(list(s2))

        s1_all_smaller = True
        s1_all_bigger = True

        compare = zip(s1list, s2list)
        for x, y in compare:
            if x > y:
                s1_all_smaller = False
            
            if x < y:
                s1_all_bigger = False 
        
        return s1_all_smaller or s1_all_bigger


        # return not any(x > y for x,y in zip(sorted(list(s1)), sorted(list(s2), reverse=True)))