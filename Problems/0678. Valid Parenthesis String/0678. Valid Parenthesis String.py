# 04-06-2024 Leetcode 0678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/?envType=daily-question&envId=2024-04-07

# time: 25, challenge: 4/10

class Solution:
    def checkValidString(self, s: str) -> bool:
        curr_sum, stars_found = 0, 0
        for char in s:
            if char == "*":
                stars_found += 1
            elif char == "(":
                curr_sum += 1
            else:
                if curr_sum == 0 :
                    if stars_found:
                        stars_found -= 1
                    else:
                        return False
                else:
                    curr_sum -= 1
        if curr_sum > stars_found:
            return False
        
        curr_sum, stars_found = 0, 0
        for char in s[::-1]:
            if char == "*":
                stars_found += 1
            elif char == ")":
                curr_sum += 1
            else:
                if curr_sum == 0:
                    if stars_found:
                        stars_found -= 1
                    else:
                        return False
                else:
                    curr_sum -= 1
        if curr_sum > stars_found:
            return False
        
        return True






# 02-01-2024 Neetcode 0678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/
# Time: like... 25 then 70 debug. Challenge: 7/10


# An interesting one. I guess recursion? The char limit is just 100
# and we caan process chars withing a frame and only recurse on '*'?
# Pass current index and number of open parens. If its ever negative, 
# return the branch is invalid. Or branches. Check if the current char 
# idx is == len(s) (one PASSED) and open parens == 0  and return True?

# Am I being dumb? Kinda. Each star can be a blank and we just count normal.
# Can I naively just count stars and move on? If we ever dip below open = 0,
# then we can just borrow stars. As long as we dont run out of stars we are fine.
# If we get to the end and open > 0, can we naively borrow remaining stars? As long
# as their is enough of them to cover the discrepency DOES the order matter? We can
# ALWAYS add an open paren, but are limited to when we CLOSE parens. Presumably by
# removing borrowed stars AS we dipped below open < 0 as we counted we've handled
# all the illegal uses of close parens so any remaining stars SHOULD be able to be
# closes without violation... Any remaining after the discrepency can be blank

#

# Still dont know why my recursive solution failed, it looks ok.
# IT WAS A SINGLE TYPO! A "==" comparison instead of a "=" assignment
# Over an hour looking and thinking on it and it was a typo.
# Also my rcursive method was pretty close to the O(n) greedy approach. I even
# recognized the key pattern that each star expands a "possibility window" for
# the balance count by one on either end, and all the middle values stay the same.
# I MISSED that this means we can ignore the middle values and only process the hi
# and lo, and we can thus do this iteratively instead of recursively. At least I 
# memoized it and it passed.


# from functools import cache
 

# class Solution:
#     def checkValidString(self, s: str) -> bool:
        # num_stars = 0
        # open_count = 0

        # for char in s:
        #     if char == '(':
        #         open_count += 1
        #     elif char == ')':
        #         open_count -= 1
        #         if open_count == -1:
        #             if num_stars > 0:
        #                 num_stars -= 1
        #                 open_count = 0
        #             else:
        #                 return False
        #     else:
        #         num_stars += 1

        # return open_count - num_stars <= 0

        # @cache
        # def recurse(idx, open):
        #     valid = True

        #     while idx < len(s) and valid:
        #         if open < 0:
        #             valid = False
        #             break
        #         if s[idx] == "(":
        #             open += 1
        #         elif s[idx] == ")":
        #             open -= 1
        #         else:
        #             valid = recurse(idx + 1, open - 1) | recurse(idx + 1, open) | recurse(idx + 1, open + 1)
        #             break
        #         idx += 1
                            
        #     if idx == len(s):
        #         valid = open == 0

        #     return valid

        # return recurse(0,0)
