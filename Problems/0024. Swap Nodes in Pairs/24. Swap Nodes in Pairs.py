# """02-15-2022 LeetCode 24. Swap Nodes in Pairs- Annoyingly not easy to test here as I'd need to generate a linked list and am lazy"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, cur, ans = None, head, head.next
        while cur and cur.next:
            adj = cur.next
            if prev:
                prev.next = adj

            cur.next, adj.next = adj.next, cur
            prev, cur = cur, cur.next

        return ans or head
