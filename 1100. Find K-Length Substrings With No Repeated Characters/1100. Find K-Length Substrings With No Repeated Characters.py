# 03-19-2023 Leetcode 1100. Find K-Length Substrings With No Repeated Characters
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/

# sliding window with some sort of advanced trick to quickly check repeats.
# Maybe a counter and a seperate set of "over" chars. If ANY in over, then
# we dont need to bother. that way we are just dealing with adding one
# and removing one char from the counter at a time, and possibly from over
# which is hashed.


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        L, R = 0, k
        ltr_count = collections.Counter(s[L:R])
        over = set()
        for ltr in ltr_count:
            if ltr_count[ltr] > 1:
                over.add(ltr)

        ans = 0

        while R < len(s):
            if not over:
                ans += 1

            ltr_count[s[L]] -= 1
            if ltr_count[s[L]] == 0:
                del ltr_count[s[L]]
            if ltr_count[s[L]] == 1:
                over.remove(s[L])
            L += 1

            ltr_count[s[R]] += 1
            if ltr_count[s[R]] > 1:
                over.add(s[R])
            R += 1

        if not over:
            ans += 1
        return ans
