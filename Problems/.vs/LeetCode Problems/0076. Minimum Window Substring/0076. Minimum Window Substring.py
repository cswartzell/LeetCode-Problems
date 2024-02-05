# 02-04-2024 Leetcode Weekly 0076. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/?envType=daily-question&envId=2024-02-04
# Time: 25 minutes?! Challenge: 5/10 Really easy for a HARD

# What if we use just ONE counter, not two? We start adding to the counter for elements
# in s, and SUBTRACTING for elements in T. Keep a set for counts that are negative.
# Do this til our i == len(t). This is the setup, we cant have a smaller window than 
# T itself of course. (oh, base check that s >= t). From here its just a basic sliding
# window problem: If there are no negative counts in our set, then there is at least one
# copy of every element in T in our window- try reducing the window by dropping the Leftmost
# letter. If instead there ARE negative counts, we need to acquire more letters- move R and
# add in new letters, possibly fulfilling negative counts. Anytime len(neg_counts) == 0
# min it to see if its smaller: ans = min(ans, L-R)

# Am I missing something? This seems like a solid medium. 


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        ltr_count = collections.Counter()
        neg_counts = set()

        for i in range(len(t)):
            ltr_count[t[i]] -= 1
            ltr_count[s[i]] += 1

            if ltr_count[s[i]] >= 0:
                neg_counts.discard(s[i])

            if ltr_count[t[i]] < 0:
                neg_counts.add(t[i])

        if neg_counts == set():
            return s[:len(t)]

        ans = None

        L, R = 0, len(t)  # L is INCLUDED in the count, R is YET TO BE INCLUDED. iterate til R == len(s)
        while L <= len(s) - len(t):
            if neg_counts == set() or R == len(s):
                if neg_counts == set() and (ans == None or len(ans) > R - L):
                    ans = s[L:R]
                ltr_count[s[L]] -= 1                   
                if ltr_count[s[L]] < 0:
                    neg_counts.add(s[L])
                L += 1

            elif R < len(s):
                ltr_count[s[R]] += 1
                if ltr_count[s[R]] >= 0:
                    neg_counts.discard(s[R])
                R += 1

        return ans if ans != None else ""