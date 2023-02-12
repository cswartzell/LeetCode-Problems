# 02-11-2023 Leetcode: 1129. Shortest Path with Alternating Colors
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

# Typically, quickest path implies BFS
# In this case we can prune early if there isnt a route
# That maintains the pattern


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        # create an adjacency dict... dunno why these are never just given
        # Note: a DIRECTED graph for once, so edges are one way
        redEdgeDict = collections.defaultdict(list)
        for a, b in redEdges:
            redEdgeDict[a].append(b)

        blueEdgeDict = collections.defaultdict(list)
        for a, b in blueEdges:
            blueEdgeDict[a].append(b)

        # Lets do this recursively since I never do and am out of practice

        def node_dive(nodesViaRed, nodesViaBlue, currNode, LastColor, steps):
            ans[currNode] = min(ans[currNode], steps)

            if LastColor == 1:
                for next_node in blueEdgeDict[currNode]:
                    if next_node not in nodesViaBlue:
                        nodesViaBlue.add(next_node)
                        node_dive(nodesViaRed, nodesViaBlue, next_node, -1, steps + 1)
            else:
                for next_node in redEdgeDict[currNode]:
                    if next_node not in nodesViaRed:
                        nodesViaRed.add(next_node)
                        node_dive(nodesViaRed, nodesViaBlue, next_node, 1, steps + 1)

        ans = [101] * n
        ans[0] = 0
        # red = 1, blue = -1
        for next_node in redEdgeDict[0]:
            node_dive(set([next_node]), set(), next_node, 1, 1)

        for next_node in blueEdgeDict[0]:
            node_dive(set([next_node]), set(), next_node, -1, 1)

        for i in range(len(ans)):
            ans[i] = ans[i] if ans[i] != 101 else -1
        return ans
