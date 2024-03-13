# 03-12-2024 Leetcode 1171. Remove Zero Sum Consecutive Nodes from Linked List
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12
# Time: 30 mins Challenge 5/10


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_at_sum = collections.defaultdict(ListNode)
        dummy = ListNode(0, head)
        node_at_sum[0] = dummy

        node = head
        curr_sum = 0
        while node:
            curr_sum += node.val
            if curr_sum in node_at_sum:
                temp = node_at_sum[curr_sum].next
                node_at_sum[curr_sum].next = node.next

                #delete intermediate nodes from dict
                temp_sum = curr_sum
                while temp != node:
                    temp_sum +=  temp.val
                    del node_at_sum[temp_sum]
                    temp = temp.next

                node = node_at_sum[curr_sum]
            else:
                node_at_sum[curr_sum] = node
            node = node.next
        
        return dummy.next
