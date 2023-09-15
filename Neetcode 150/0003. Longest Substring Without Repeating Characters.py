# 11-14-2023 Neetcode 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time: 15 mins

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        L, R = 0, 0
        unique = set(s[R])
        duplicate = None
        max_window = 0
        
        while R < len(s) - 1:
            R += 1
            if s[R] in unique:
                duplicate = s[R]
            else:
                unique.add(s[R])
            while duplicate:
                if s[L] == duplicate:
                    duplicate = None
                else:
                    unique.remove(s[L])
                L += 1
            max_window = max(max_window, R - L + 1) 
        
        return max_window
