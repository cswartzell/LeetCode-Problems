# 12-09-2022 Leetcode 0108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

#acutaly stumped me for a sec. BSTs are NOT unique, so any solution will do.
#had a little trouble ensuring the slices would hit all nodes


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BST_it(left, right):
            if left > right:
                return
            middle = (right + left) // 2
            node = TreeNode(nums[middle])
            node.left = BST_it(left, middle - 1)
            node.right = BST_it(middle + 1, right)
            return node

        return BST_it(0,len(nums)-1)