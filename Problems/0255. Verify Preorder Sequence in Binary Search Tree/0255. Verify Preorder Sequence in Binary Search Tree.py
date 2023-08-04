# 08-03 Leetccode 255. Verify Preorder Sequence in Binary Search Tree
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/


# Construct the B Tree
# preorder search it.
# compare?

#Wait... how do I make a B Tree? Damnit.
#Stack? Push number. if next number is SMALLER, push number. Repeat
# if next number is larger, POP until larger (discard number)
# see if set empty?
# I think I need to push a min/max?

# #STANDARD NODE CLASS
# class node:
#     def __init__(self, val = None, children = None):
#         self.val = val
#         children = None

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:       
        stack = [preorder[0]]
        min_val = 0
        for num in preorder[1:]:
            if num < min_val:
                return False
            if stack[-1] > num:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    temp = stack.pop()
                    min_val = max(min_val, temp)
                    if stack and stack[-1] > num:
                        stack.append(temp)
                        break
                stack.append(num)
        return True




        # stack = [(preorder[0], preorder[0])]
        # for num in preorder[1:]:
        #     #smaller than minimum
        #     if num < stack[-1][0]:
        #         stack.append((num, stack[-1][1]))
        #     # greater than last-----------------------------------
        #     elif num > stack[-1][0] and