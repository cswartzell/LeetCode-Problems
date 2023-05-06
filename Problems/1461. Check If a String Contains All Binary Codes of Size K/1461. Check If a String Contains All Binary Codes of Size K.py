"""05-30-2022 Leetcode 1461. Check If a String Contains All Binary Codes of Size K"""

# Yikies. Sliding window?
# again... memoization here could help but its tough
# Oh, I misread it. Its a fixed window size, so just slide that
# once building a set of all extant combos OF length k
# not k and fewer. Stop if we get to
# 2**k combos as now weve seen them all. Fail if at the end
# our set does not have 2**K combos


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set(s[i - k : i] for i in range(k, len(s) + 1))) == 2 ** k


#         subs_required = 2**k
#         subsets = set()

#         l,r = 0, k
#         while r <= len(s) and len(subsets) < subs_required:
#             subsets.add(s[l:r])
#             l += 1
#             r += 1

#         return len(subsets) == subs_required
