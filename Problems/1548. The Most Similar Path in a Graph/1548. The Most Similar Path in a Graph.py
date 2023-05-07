# 04-03-2023 Leetcode 1548. The Most Similar Path in a Graph
# https://leetcode.com/problems/the-most-similar-path-in-a-graph/description/

# Dijkstra?
# Use a heap. Test minimum routes, stop on first success?

# ok! So my first attempt WORKS, but is far too slow. Fails only the 12th case
# I think we are missing that this is a DP solution. Can we add that in or is this too much
# of a mess to do so?

# OK! Instead of using a heap and pushing, which isnt cheap, we can just deque. No edit distance change?
# Add to front. Edit distance? Add to back. We can ONLY ever have 2 edit distances in the queue at a time:
# we start with all the ones that are 0, then have all the single cities with a distance of 1 after this.
# we process ALL the zeros first, and if they get dist added, they become a 1. Now ALL the nodes are one
# and we process those, turning them into twos. We actually only EVER have two values at once.

# Ok, so furthering THAT, we want to process LONGER vals first. Can we? We'd have to sort by lenth. We
# could have 2 dequues and push values that are longer to the front of the NEXT stack, but we are working
# in longest to shortest order... We could REVERSE the stack when swaping curr = next?

# class Solution:
#     def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
#         cities_named_i  = collections.defaultdict(list)
#         for i, name in enumerate(names):
#             cities_named_i[name].append(i)

#         adj_map = collections.defaultdict(list)
#         for a,b in roads:
#             adj_map[a].append(b)
#             adj_map[b].append(a)

#         # heap = [ (0, 1, [city]) for city in cities_named_i[targetPath[0]]] + [ (1, 1, [city]) for city in adj_map if city not in cities_named_i[targetPath[0]] ]
#         heap = collections.deque()
#         heap.extend( [(0,[city]) for city in cities_named_i[targetPath[0]]] + [(1, [city]) for city in adj_map if city not in cities_named_i[targetPath[0]]])
#         dp = []

#         curr_edit, curr_route = -1, []
#         while len(curr_route) < len(targetPath) and heap:
#             curr_edit, curr_route = heap.popleft()
#             if curr_route[-1] in arrived_earlier:
#                 continue
#             for neighbor in adj_map[curr_route[-1]]:
#                 arrived_earlier.add(neighbor)
#                 if names[neighbor] == targetPath[len(curr_route)]:
#                     heap.appendleft((curr_edit, curr_route + [neighbor]))
#                 else:
#                     heap.append((curr_edit + 1, curr_route + [neighbor]))

#         return curr_route
class Solution:
    def mostSimilar(
        self, n: int, roads: List[List[int]], names: List[str], tp: List[str]
    ) -> List[int]:
        # construct graph
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        # init variables
        m = len(tp)
        dp = [[m] * n for _ in range(m)]
        prev = [[0] * n for _ in range(m)]

        # populate dp
        for v in range(n):
            dp[0][v] = names[v] != tp[0]
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i - 1][u] < dp[i][v]:
                        dp[i][v] = dp[i - 1][u]
                        prev[i][v] = u
                dp[i][v] += names[v] != tp[i]

        # re-construct path
        path, min_dist = [0], m
        for v in range(n):
            if dp[-1][v] < min_dist:
                min_dist = dp[-1][v]
                path[0] = v
        for i in range(m - 1, 0, -1):
            u = prev[i][path[-1]]
            path.append(u)

        return path[::-1]
