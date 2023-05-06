# 04-28-2023 Leetcode 1080. Insufficient Nodes in Root to Leaf Paths
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/description/

# What could be meant by "delete all nodes simultaneously"?
# As far as I am aware, this is not really an option


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def DFS(node, downsum) -> int:
            if not node.left and not node.right:
                return downsum + node.val

            lsum, rsum = -math.inf, -math.inf
            if node.left:
                lsum = DFS(node.left, downsum + node.val)
                if lsum < limit:
                    node.left = None
            if node.right:
                rsum = DFS(node.right, downsum + node.val)
                if rsum < limit:
                    node.right = None

            return max(rsum, lsum)

        dummy_root = TreeNode(0, root, None)
        DFS(dummy_root, 0)

        return dummy_root.left
