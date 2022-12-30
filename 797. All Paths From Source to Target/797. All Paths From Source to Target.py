# 12-30-2022 Leetcode 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/description/

# Its acyclical so we dont need to worry about loops
# We need EVERY path, so we dont need to keep a "visited" set
# So... its just BFS? Stack based iteration rather than recursion?

# Once again, leetcodes enext_nodeamples only show the most basic cases.
# Presumably there are paths that terminate and DO NOT end at the target
# Once found, we could delete those. We can also delete any nodes that dont
# have an edge leading out, unless they ARE the target.

# Wait, if we do the above recursively, dont we end up with a graph where all ]
# routes DO go to the target eventually? Is this somehow less work than just BFS
# in the first place? I think its the same amount of searching, if not more, just
# with a different goal in mind.

# Hmm... up to 15 nodes. That could be the 14th triangular number of edges right?
# First node points to 14 others, nenext_nodet node can point to 13 as it cannot point to first...
# Thats only 105 edges. That could be some deep paths...
# The first path would have 14 paths of length one, the second pass would have
# Well... 14*13 paths? Then presumably that times 12 paths... so 14! possible
# routes which is... unnacceptable? I should HAVE to do pruning right?

import functools


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        # apply the memoization
        @lru_cache(maxsize=None)
        def all_paths_to_target(curr_node):
            if curr_node == target:
                return [[target]]

            results = []
            for next_node in graph[curr_node]:
                for path in all_paths_to_target(next_node):
                    results.append([curr_node] + path)

            return results

        return all_paths_to_target(0)

        # Duh. Dict not needed. Dicts key is literally just the list idx... so we can just
        # use the list in the fist place. Still, neat if needed
        # #A DICTIONARY CONSTRUCTOR WORKS LIKE A LIST CONSTRUCTOR ONLY IF USED IN BRACKETS
        # # DICT( THE SAME CONSTRUCTOR DOES NOT SEEM TO ALWAYS WORK !!!!   )
        # # dict_graph = { i : e for i, e in enumerate(graph)}

        # target_node = len(graph) - 1

        # curr_paths_stack = collections.deque([[0]])
        # final_paths = []

        # while curr_paths_stack:
        #     next_node = len(curr_paths_stack)
        #     for _ in range(next_node):
        #         curr_path = curr_paths_stack.popleft()
        #         for next_node in graph[curr_path[-1]]:
        #             if next_node == target_node:
        #                 final_paths.append(curr_path + [next_node])
        #             else:
        #                 curr_paths_stack.append(curr_path + [next_node])

        # return final_paths


# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         target_node = len(graph) - 1

#         next_paths_stack = [[0]]
#         curr_paths_stack = []
#         final_paths = []

#         while next_paths_stack:
#             curr_paths_stack = next_paths_stack
#             next_paths_stack = []
#             while curr_paths_stack:
#                 curr_path = curr_paths_stack.pop()
#                 for next_node in graph[curr_path[-1]]:
#                     if next_node == target_node:
#                         final_paths.append(curr_path + [next_node])
#                     else:
#                         next_paths_stack.append(curr_path + [next_node])

#         return final_paths
