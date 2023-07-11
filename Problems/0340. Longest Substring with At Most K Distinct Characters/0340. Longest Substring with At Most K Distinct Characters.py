# 07-10-2023 Leetcode 340. Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

# THIS is just sliding window

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        L, R = 0, min(len(s)-1,k-1)
        ltr_count = collections.Counter(s[:R+1])
        while R < len(s) - 1:
            R += 1
            ltr_count[s[R]] += 1
        
            if len(ltr_count) > k:
                ltr_count[s[L]] -= 1
                if ltr_count[s[L]] == 0:
                    del ltr_count[s[L]]
                L += 1
        return R - L + 1
            
            
                
