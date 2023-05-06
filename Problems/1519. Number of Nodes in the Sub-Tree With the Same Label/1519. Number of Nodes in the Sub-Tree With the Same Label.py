# 1-10-2023 Leetcode 1519. Number of Nodes in the Sub-Tree With the Same Label
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

# This is a "Trie"

# We only look DOWN from a given node through its subtrees, so this is actually a directed graph
# Which means we dont need to double up our adjacency array: no adj[x] += y, adj[y] += x
# NEVERMIND YOU MOTHER FUCKERS: [[0,2],[0,3],[1,2]].
# So the edges ARE undirected and there is no simple way to tell what is a parent and what
# is a child. Therfore, we cannot simply pass on a parent node to NOT visit as we dont
# know which IS a parent node. We could built the tree and THEN traverse it assigning
# parents, but this is insane. I guess we need to keep a list of visited nodes then for
# each pass. Getting costly.

# Wait, shit. Keeping track of visited DOESNT somehow prevent us from goin up the tree?!
# How do we stop from climbing? We have to have a way of storing parents...
# Value doesnt help, node 2 can be a parent of node 1. Order in edges doesnt help,
# [parent, child] and [child, parent] are both given freely...

# Do we have to DFS it once just to build a parent dict? Seems logical?

# We can maybe cache the function so we arent overly repetitive, but we do DFS the tree
# STARTING at each node in the tree itself. A LOT of repeated work. There may be a far
# more clever DP array we could keep, but cache is at least a good step?
# Its already written in such a way that chaching is easy

import functools


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        num_nodes = len(edges) + 1
        ans = []

        ##adj is an adjacency graph, UNDIRECTED so does not and cannot have parent info
        # parent dict is then developed after adj to notate the parents of each node
        adj = dict()
        parent = dict()  # ?!?!?!?

        # instantiate UNDIRECTED graph, note no info about parents can be gleaned yet
        for x, y in edges:
            if x not in adj:
                adj[x] = {y}
            else:
                adj[x].add(y)
            if y not in adj:
                adj[y] = {x}
            else:
                adj[y].add(x)

        # build PARENT dict
        visited = set()

        def dfs_birth(node, parnt):
            visited.add(node)
            parent[node] = parnt
            for child in adj[node]:
                if child not in visited:
                    dfs_birth(child, node)

        dfs_birth(0, None)

        # @cache #Doesnt Work?
        @functools.cache
        def dfs_matching_labels(node, label) -> int:
            submatches = 0
            for child in adj[node]:
                if child != parent[node]:
                    submatches += dfs_matching_labels(child, label)
            return submatches + 1 if labels[node] == label else submatches

        for i in range(num_nodes):
            ans.append(dfs_matching_labels(i, labels[i]))

        return ans
