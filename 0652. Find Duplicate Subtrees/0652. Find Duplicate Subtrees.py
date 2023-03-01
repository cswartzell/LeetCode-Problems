# 02-28-2023 Leetcode 0652. Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        string_trees = collections.defaultdict(int)
        ans = []

        def dfs(curr_node) -> str:
            if not curr_node:
                return ""
            curr_str = (
                str(curr_node.val)
                + ":"
                + dfs(curr_node.left)
                + ":"
                + dfs(curr_node.right)
            )
            string_trees[curr_str] += 1
            if string_trees[curr_str] == 2:
                ans.append(curr_node)
            return curr_str

        dfs(root)
        return ans

        # string_trees = collections.defaultdict(int)
        # ans = []

        # def dfs (curr_node) -> str:
        #     if not curr_node:
        #         return "!"

        #     left_str = ":" + dfs(curr_node.left)
        #     string_trees[left_str] += 1
        #     if string_trees[left_str] == 2 and left_str != ":!":
        #         ans.append(curr_node.left)

        #     right_str = ":" + dfs(curr_node.right)
        #     string_trees[right_str] += 1
        #     if string_trees[right_str] == 2 and right_str != ":!":
        #         ans.append(curr_node.right)

        #     return str(curr_node.val) + left_str + right_str

        # dfs(root)
        # return ans
