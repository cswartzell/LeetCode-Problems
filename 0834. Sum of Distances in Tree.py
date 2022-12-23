# 12-22-2022 leetcode 834. Sum of Distances in Tree
# https://leetcode.com/problems/sum-of-distances-in-tree/description/

# Not sure how to do this efficiently at least... I can start by literally
# constructing the tree, then DFS to leaves, and have them pass up their
# distances + 1 to their parents up to the root. When a node receives its
# leaf distances it can then record this to a dict.

# hmm...up to 30,000 nodes. Quite a lot

# this is mostly about memoization in some form.


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        ans = [0] * n

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
