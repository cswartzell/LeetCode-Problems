# 03-31-2023 Leetcode 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        ans = 0
        while s and g:
            child = g.pop()
            while s:
                cookie = s.pop()
                if cookie >= child:
                    ans += 1
                    break
        return ans
