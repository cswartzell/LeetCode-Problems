"""05-16-2022 Leetcode 1091. Shortest Path in Binary Matrix"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # Build graph in dict and track all nodes.
        n = len(grid)
        if n == 1:
            return 1

        NE, NN, NW, WW, EE, SW, SS, SE = range(8)  # may not use
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Well... an insane iterative method of just building out chains of
        # nodes that are zero and can reach another zero node
        graph = dict()
        for x in range(n):
            for y in range(n):
                for ox, oy in offsets:
                    if x + ox >= 0 and x + ox < n and y + oy >= 0 and y + oy < n:
                        if grid[x][y] == 0 and grid[x + ox][y + oy] == 0:
                            if (x, y) not in graph:
                                graph[(x, y)] = [(x + ox, y + oy)]
                            else:
                                graph[(x, y)] += (x + ox, y + oy)

        stack = [(0, 0)]

        while stack:
            source = heappop(stack)  # POP MIN PRIORITY QUEUE
            for neighbor in graph[source]:
                x, y = neighbor
                sx, sy = source
                if grid[x][y] == 0 or grid[x][y] > grid[sx][sy] + 1:
                    grid[x][y] = grid[sx][sy] + 1
                    heappush(stack, neighbor)  # Push PRIORITY QUEUE VERSION

        return grid[n - 1][n - 1] if grid[n - 1][n - 1] != 0 else -1
