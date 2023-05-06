class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid) -> Node:
        def quad_it(grid) -> Node:
            if len(grid) == 1:
                return Node(grid[0][0] == 1, True, None, None, None, None)
            else:
                tl = quad_it([row[: len(grid) // 2] for row in grid[: len(grid) // 2]])
                tr = quad_it([row[len(grid) // 2 :] for row in grid[: len(grid) // 2]])
                bl = quad_it([row[: len(grid) // 2] for row in grid[len(grid) // 2 :]])
                br = quad_it([row[len(grid) // 2 :] for row in grid[len(grid) // 2 :]])
                all_leaves = all([tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf])
                all_TorF = tl.val == tl.val == bl.val == br.val
                if all_leaves and all_TorF:
                    return Node(tr.val, True, None, None, None, None)
                return Node(False, False, tl, tr, bl, br)

        return quad_it(grid)


sol = Solution()
ans = sol.construct(
    [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ]
)
pass
