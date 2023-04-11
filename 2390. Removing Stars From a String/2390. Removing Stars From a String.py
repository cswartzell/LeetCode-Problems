# 04-10-2023 Leetcode 2390. Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/description/


class Solution:
    def removeStars(self, s: str) -> str:
        inky_void_s = []
        star_count = 0
        for char in s[::-1]:
            if char == "*":
                star_count += 1
            elif star_count > 0:
                star_count -= 1
            else:
                inky_void_s.append(char)
        return "".join(inky_void_s[::-1])