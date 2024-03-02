# 03-01-2024 Leetcode 3062. Winner of the Linked List Game
# https://leetcode.com/problems/winner-of-the-linked-list-game/?envType=weekly-question&envId=2024-03-01
# Time: 15 Challenge: 2/10

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        evens_score = 0
        while head and head.next:
            evens_score += 1 if head.val > head.next.val else -1
            head = head.next.next
        
        if evens_score > 0:
            return "Even"
        elif evens_score == 0:
            return "Tie"
        else:
            return "Odd"
