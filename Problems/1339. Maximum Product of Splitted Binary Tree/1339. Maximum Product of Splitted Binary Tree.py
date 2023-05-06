# 12-09-2022 Leetcode 1339. Maximum Product of Splitted Binary Tree
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

# ooh, a mathy one. I genuinely dont know how to approach this yet.
# ok, first things first would be a summation DFS traversal, so each
# node would directly have the sum of each branch decended from it.
# Perhaps each node should also know the sums of the branch above it?
# Thats multiple traversals to discover that.

# Intuitively I feel like we want the two sums to be as close to eachother
# as is possible. In geometry, the area of a square is the most efficient
# quadrilateral compared to its perimeter. Cam I prove it rigourously?
# Feel a little too rusty for that... But my point stands, I think we can
# use this and traverse the tree a SECOND time, once we have all the summation
# information. Pass DOWN the total of left and right and keep a max of this
# times one of each leg FROM that node.

# Am I going to have to extend the TreeNode class to do this? Could be a fun
# way to learn to do it. I think there is a way to do this in one go.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # def tree_sum(subroot):
        #     if subroot is None: return 0
        #     left_sum = tree_sum(subroot.left)
        #     right_sum = tree_sum(subroot.right)
        #     return left_sum + right_sum + subroot.val

        #   def maximum_product(subroot, total):
        #     best = 0
        #     def recursive_helper(subroot):
        #         nonlocal best
        #         if subroot is None: return 0
        #         left_sum = recursive_helper(subroot.left)
        #         right_sum = recursive_helper(subroot.right)
        #         total_sum = left_sum + right_sum + subroot.val
        #         product = total_sum * (tree_total_sum - total_sum)
        #         best = max(best, product)
        #         return total_sum
        #     recursive_helper(subroot)
        #     return best

        # tree_total_sum = tree_sum(root)
        # return maximum_product(root, tree_total_sum) % (10 ** 9 + 7)

        self.biggerest = 0
        self.total = 0

        def total_it(root):
            if not root:
                return
            self.total += root.val
            total_it(root.right)
            total_it(root.left)

        total_it(root)

        def sum_em(root):
            if not root:
                return 0
            left = sum_em(root.left)
            right = sum_em(root.right)
            self.biggerest = max(
                self.biggerest,
                (self.total - (left + right + root.val)) * (right + left + root.val),
            )
            return left + right + root.val

        sum_em(root)
        show_total = self.total
        show_biggerest = self.biggerest

        return self.biggerest
