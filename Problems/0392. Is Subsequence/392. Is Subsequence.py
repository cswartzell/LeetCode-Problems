class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        curr_s_char = 0
        for i in range(len(t)):
            if t[i] == s[curr_s_char]:
                curr_s_char += 1
            if curr_s_char == len(s):
                return True
        return False
