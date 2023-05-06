# 04-05-02022 Leetcode 541. Reverse String II
# https://leetcode.com/problems/reverse-string-ii/description/


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        i = 0
        while i < len(s):
            replace = s[i : min(len(s), i + k)]
            replace = replace[::-1]
            for j in range(len(replace)):
                s[i + j] = replace[j]
            i += 2 * k
        return "".join(s)
