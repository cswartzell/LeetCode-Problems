# 04-10-2023 Leetcode 516. Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/description/

# Look... I dont want to or think I should have to memorize manachers algorithm.
# That being said, this is a SUBSEQUENCE so perhaps its not relevant.

# S is 1000 chars long and order matters, but I dont think we can simply test
# all 2^1000 combinations to see if they are palindromes. How can we cut down
# on the amount of work?

# First things first, at most one letter can lack a paired partner, and it would
# be the center of an odd len palindrome. Then, every other letter would be included
# in even pairs.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        dp = collections.defaultdict(int)

        def recurse(i, j) -> int:
            if i > j or i == len(s) or j < 0:
                return 0
            if i == j:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = (
                (2 + recurse(i + 1, j - 1))
                if s[i] == s[j]
                else max(recurse(i + 1, j), recurse(i, j - 1))
            )
            return dp[(i, j)]

        return recurse(0, len(s) - 1)
