# Isnt this just Manachers? NOT going to learn that.
# In theory we can reuse precomputed sections. 

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)

        for center in range(len(s) * 2):
            L, R = center//2, math.ceil((center + 2)/2)
            while L >= 0 and R < len(s):
                if s[L] != s[R]:
                    break
                ans += 1
                L -= 1
                R += 1

        return ans
                