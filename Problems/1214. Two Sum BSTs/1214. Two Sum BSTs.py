# 06-21-2023 Leetcode 1214. Two Sum BSTs
# https://leetcode.com/problems/two-sum-bsts/description/

# It seems absurd to do anything but traverse one tree and save it as a set
# I mean... its only 5000 entries. With possible duplicates our set is pretty small
# We can then just naively traverse the second tree looking for the additive compliment
# to target in our set. Whats the trick here?

# There is a pretty minor optimization: We could store a min and max and stop searching legs of
# our SECOND BST if know that all the nodes below that cannot be found as they are all either too
# large or too small.



# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        first_set = set()
        fs_min, fs_max = root1.val, root1.val

        # Store first BST in set, note its max and min (may be faster to do later? Do sets keep track automatically?)
        curr_lvl, next_lvl = [], [root1]
        while next_lvl:
            curr_lvl = next_lvl
            next_lvl = []
            while curr_lvl:
                curr_node = curr_lvl.pop()
                first_set.add(curr_node.val)
                fs_min = min(fs_min, curr_node.val)
                fs_max = max(fs_max, curr_node.val)
                if curr_node.left:
                    next_lvl.append(curr_node.left)
                if curr_node.right:
                    next_lvl.append(curr_node.right)
        
        #search second BST. Toss legs that are too small/large. Terminate early on match
        curr_lvl, next_lvl = [], [root2]
        while next_lvl:
            curr_lvl = next_lvl
            next_lvl = []
            while curr_lvl:
                curr_node = curr_lvl.pop()
                if target - curr_node.val in first_set:
                    return True
                if target - curr_node.val < fs_max and curr_node.left:
                    next_lvl.append(curr_node.left)
                if target - curr_node.val > fs_min and curr_node.right:
                    next_lvl.append(curr_node.right)
                    
        return False

