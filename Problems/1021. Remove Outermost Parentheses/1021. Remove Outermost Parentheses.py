# 03-26-2023 Leetcode 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/description/

# The WORDING makes it awful.
# I guess the actual code isnt too bad. The ole, count up count down
# Once we get back to zero, thats a primitive. 

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        L,R = 0,1
        #It is a valid (thus non empty) P-String, so it MUST have "(" as its firt char
        count = 1
        while R < len(s):
            if s[R] == ")":
                count -= 1
            else:
                count += 1
            if count == 0:
                ans += s[L+1:R]
                #Again, we can jump ahead. IF there is more string, it IS valid, so the next
                #char either doesnt exist and we are done (R > n), which will be caught
                #at the top of the loop, or we can skip the next char as we know it will be
                # a "(" assuming it exists at all
                L = R + 1
                R = R + 1
                count = 1
            R += 1
        
        return ans