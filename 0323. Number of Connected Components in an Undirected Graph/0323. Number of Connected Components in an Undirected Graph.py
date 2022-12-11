# 12-07-2022 Leetcode 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

# this is len of disjoint unions right?
# Do we do floyds cycle chaser? Seems cumbersome

from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        disjoint_unions = {x: {x} for x in range(n)}

        for parent, child in edges:
            disjoint_unions[child].add(parent)
            disjoint_unions[parent].add(child)

        seen = set()
        num_sets = 0

        for x in range(n):
            if x in seen:
                continue
            num_sets += 1
            new_group = disjoint_unions[x]
            new_seen = {x}
            while new_group:
                ele = new_group.pop()
                if ele not in new_seen:
                    new_group |= disjoint_unions[ele] - seen
                    new_seen.add(ele)
            seen |= new_seen

        return num_sets
