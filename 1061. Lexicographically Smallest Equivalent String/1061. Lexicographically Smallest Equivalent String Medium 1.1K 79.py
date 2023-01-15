# 01-14-2023 Leetcode 1061. Lexicographically Smallest Equivalent String
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/


# Does python heap letters nicely?
# Oh wait, going about this wrong. This is defo a union find job

from collections import defaultdict
import heapq


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # lex_dict = defaultdict(list)

        # for i in range(len(s1)):
        #     heapq.heappush(lex_dict[s1[i]], s2[i])
        #     heapq.heappush(lex_dict[s2[i]], s1[i])

        parent = {x: x for x in string.ascii_lowercase}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                sorted_pair = sorted([px, py])
                parent[sorted_pair[1]] = sorted_pair[0]

        # waitwhat  = list(zip(s1,s2))
        for x, y in zip(s1, s2):
            union(x, y)

        return "".join([find(x) for x in baseStr])
