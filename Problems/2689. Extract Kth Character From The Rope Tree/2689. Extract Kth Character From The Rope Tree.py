# 05-01-2023 Leetcode 2689. Extract Kth Character From The Rope Tree
# https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/description/

#We dont know how many chars there are in a leaf so we are going to left DFS it. 
# Really should remember which that is. Prefix?
# We dont need to generate the whole string, just enough letters

#Ah, im an idiot and misread it. We go down


# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        # """

        seenLetters = 0
        stack = [root]
        while stack:
            currNode = stack.pop()
            #Are there enough letters below this node to contain the kth letter?
            #If not, count them all as seen and move on
            if currNode.len and k >  seenLetters + currNode.len:
                seenLetters += currNode.len
                continue

            if not currNode.left and not currNode.right:
                if len(currNode.val) + seenLetters >= k:
                    return currNode.val[k - seenLetters -1]
                else:
                    seenLetters += len(currNode.val)
            else:
                if currNode.right:
                    stack.append(currNode.right)
                if currNode.left:
                    stack.append(currNode.left)    