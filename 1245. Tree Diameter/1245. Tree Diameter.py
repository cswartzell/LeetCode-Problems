# 03-26-2023 Leetcode 1245. Tree Diameter
# https://leetcode.com/problems/tree-diameter/description/

# So for a tree, obviously the longest route is going to start at a leaf,
# run up to the root, then down to another leaf. Seems kinda obvious that
# this would just be the two deepest leaves, by heights. So lets just
# sotre the height of the leaves after a DFS and return the sum of the largets two

# Oh, we arent given a root. Just a undirected graph. Thats actually an interesting
# on its own. "Locate the root of a tree given just undirected graph edges". Is it possible?
# No, all roots are valid, its just a matter or where you origami it. Assuming its acyclical


# Recursive DFS because I am weaker on that, and generally opt for iterative BFS
# EXNAY

# Ok, what about DP: start a dp array with "0" for every n, this is the
# longest time it took to get to that node. Every node takes zero time to get
# to. Then we BFS from EVERY node, adding one each time we visit an adjacent node.
# If the existing DP time is larger than the current path we stop.
# Return the longest time in the DP array. Its the same solution as the
# "longest cycle in a DAG" problem


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj_map = collections.defaultdict(list)
        for x, y in edges:
            adj_map[x].append(y)
            adj_map[y].append(x)

        def BFS_Distance(node):
            curr_row = None
            next_row = [node]
            visted = set()
            distance = -1
            extreme_node = None
            while next_row:
                curr_row = next_row
                next_row = []
                distance += 1
                while curr_row:
                    curr_node = curr_row.pop()
                    visted.add(curr_node)
                    for next_node in adj_map[curr_node]:
                        if next_node not in visted:
                            next_row.append(next_node)
                            extreme_node = next_node

            return extreme_node, distance

        extreme_node_1, _ = BFS_Distance(0)
        extreme_node_2, diameter = BFS_Distance(extreme_node_1)

        return diameter

        # None of this works because you cant just check the existing DP map. You need
        # to true BFS every node if you cant identify the extreme length nodes.
        # But you CAN identify them, and its brilliant and Im mad i didnt think of it

        # n = range(len(edges) + 1)
        # dp = [0 for _ in n]

        # adj_map = collections.defaultdict(list)
        # for x, y in edges:
        #     adj_map[x].append(y)
        #     adj_map[y].append(x)

        # #Now we could declare diameter = 0 here and write an extra if in the loop
        # #so it gets updated as we discover larger and larger routes. This is LESS efficient
        # #then just doing a linear scan at the end though. A linear scan is one IF for n more nodes
        # #but our loop is n at BEST. maybe n**2. best to save it til later

        # for x in n:
        #     stack = [x]
        #     currr_steps = 0
        #     visited = set()
        #     while stack:
        #         curr_node = stack.pop()
        #         visited.add(curr_node)
        #         currr_steps += 1
        #         for y in adj_map[curr_node]:
        #             if y not in visited and dp[y] <= currr_steps:
        #                 dp[y] = currr_steps
        #                 stack.append(y)

        # return max(dp)
