class Solution:
    def findShortestCycle(self, n, edges):
        # Create an adjacency list to represent the graph.
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        # Initialize a variable to keep track of the minimum cycle length.
        min_cycle = n + 1

        # Iterate through each node in the graph.
        for i in range(n):
            # Initialize a list to store distances from the current node to other nodes.
            dist = [-1] * n
            dist[i] = 0

            # Initialize a queue for BFS traversal starting from the current node.
            q = [i]
            front = 0

            # Perform BFS traversal.
            while front < len(q):
                u = q[front]
                front += 1
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
                    elif dist[v] >= dist[u]:
                        # If a node is visited again and is not the parent, it forms a cycle.
                        # Calculate the cycle length and update min_cycle if needed.
                        min_cycle = min(min_cycle, dist[v] + dist[u] + 1)

        # If no cycle is found, return -1. Otherwise, return the minimum cycle length.
        return min_cycle if min_cycle <= n else -1