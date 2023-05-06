# 04-28-2023 Leetcode 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

# this is a segment tree question, and I dont know those


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        num_vowels = [0]
        for char in s:
            num_vowels.append(num_vowels[-1] + int(char in vowels))

        L, R = 0, k
        max_vowels = 0
        while R <= len(s):
            max_vowels = max(max_vowels, num_vowels[R] - num_vowels[L])
            R += 1
            L += 1

        return max_vowels
