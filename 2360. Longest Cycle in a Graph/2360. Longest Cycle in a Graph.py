# 03-26-2023 2360. Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/
# Multi-floyd? No

# Without knowing better, create an adjacency map.
# Start with ALL root nodes (those that dont have an incoming edge)
# AND/OR terminal nodes and remove them from adjacency
# aaaand is that it? As they can only have one outgoing edge it either
# terminates, or is part of a ring. The whole thing is connected so
# does that mean there can only BE one cycle? I think so.
# A node clearly cant be part of two cycles as it requires two edges.
# And any other node is either part OF the cycle, or points at it. it
# cant create its own cycle or the two cycles cant be connected.

# Wait, its represented as just an array. We can just use a recursive
# Find operation, reassign to "terminal" rather than root, and the
# FIRST cycle we come upon, return its length

# class Solution:
#     def longestCycle(self, edges: List[int]) -> int:
# to_fro = collections.defaultdict(list)
# fro_to = collections.defaultdict(list)

# WAit, I think if there is only one outgoing edge
# hit a node in the visited set, empty it and start a new visited set, keep
# traversing. We are in the loop now. The SECOND time we hit a node in the
# visited cycle we can exit. Or just mark the start node and count.


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        longest_cycle_len = -1
        time_step = 1
        node_visited_at_time = [0] * len(edges)

        for current_node in range(len(edges)):
            if node_visited_at_time[current_node] > 0:
                continue
            start_time = time_step
            u = current_node
            while u != -1 and node_visited_at_time[u] == 0:
                node_visited_at_time[u] = time_step
                time_step += 1
                u = edges[u]
            if u != -1 and node_visited_at_time[u] >= start_time:
                longest_cycle_len = max(
                    longest_cycle_len, time_step - node_visited_at_time[u]
                )

        return longest_cycle_len

        # candidates = set()

        # for i in range(len(edges)):
        #     visited = {i}
        #     stack = [i]
        #     while edges[stack[-1]] != -1 and i not in candidates and edges[i] not in candidates:
        #         visited.add(edges[stack[-1]])
        #         stack.append(edges[stack[-1]])
        #         if edges[stack[-1]] in visited:
        #             candidates.add(edges[stack[-1]])
        #             stack.clear()
        #             break
        #     while stack:
        #         curr_node = stack.pop()
        #         edges[curr_node] = -1

        # longest_cycle = -1
        # for x in candidates:
        #     curr_cycle = 1
        #     next_node = edges[x]
        #     while next_node != x:
        #         curr_cycle += 1
        #         next_node = edges[next_node]
        #     longest_cycle = max(longest_cycle, curr_cycle)

        # return longest_cycle
