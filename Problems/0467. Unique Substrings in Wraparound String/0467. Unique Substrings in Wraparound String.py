# 04-05-2024 Leetcode 0467. Unique Substrings in Wraparound String
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/
# Time: 20: challenge: 3/10

# The key to this one is just remembering that for a set of len(n), there are nth triangular
# numbers of CONTIGUOUS subsets not including the empty set. So this is just two
# pointer, move right as long as we are sequentially, then add R-L * (R-L * 1)//2 to the total
# then move L to R and continue.

# Watch the final case. May need to catch it after the loop, or make the loop condition a 
# little complex

# Oh. I didnt read the problem now did I? Its how many UNIQUE subntrings. We need to store them
# as we find them. THe naive way would be to simply store the substring itself, and for most
# purposes that isnt too bad. But lets assume there is going to be a tricky test case
# that has a substring that wraps a dozen times. Realistically, still not a problem, but we
# could store this more compactly: keep a set of tuples of (starting letter: substring length).

# Wait, no I need to actually break down each contiguous secction into its subsections and store
# all of them. Oh neat! Ok, so step 1: find a contiguous seciton. Step 2, Break it down:
# A seperate 2 pointer pass: start L on the left, and for substrings starting with that L, more
# R back to the left. We can stop once weve found an extent substring and thus move L up one.
# We keep doing that til L is exhausted:

# Say previously we'd found ABC. Now we have ABCDE. Starting with A thats a new substring, so
# add ABCDE to the list, and move R down. Also new, add ABCD. Move R: we've seen ABC, no need
# to decomposed it, we must have done that already. Now move L: BCDE is new, as is BCD, but NOT
# BC. Conitnue. 


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        L, R = 0, 1

        def follows(R):
            return ord(s[R]) == ord(s[R-1]) + 1 or (s[R] == "a" and s[R-1] == "z")

        seen = set()

        while R < len(s):
            # Find contiguos sub section
            while R < len(s) and follows(R):
                R += 1
            
            _R = R
            while L < R:
                while _R > L and (s[L], _R - L) not in seen:
                    seen.add((s[L], _R - L))
                    _R -= 1
                _R = R
                L += 1
            R += 1
        
        _R = R
        while L < len(s):
            while _R > L and (s[L], _R - L) not in seen:
                seen.add((s[L], _R - L))
                _R -= 1
            _R = R
            L += 1
        R += 1
        
        return len(seen)
