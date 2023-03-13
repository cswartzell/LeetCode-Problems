# 03-11-2023 Leetcode 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # An attempt to add a less than comparison function, defined by "dunder"
    # that would allow heapq to work with listnodes and compare them directly
    # Sadly this failed, as I guess its not overriding the existing ListNode clase

    # def __lt__(self, comparison: ListNode ):
    #     return self.val < comparison.val


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         merged_list = ListNode(-1000001)
#         merged_list_head = merged_list

#         while lists:
#             smallest_val = 100001
#             smallest_list = None
#             for k_list in lists:
#                 if k_list.val < smallest_val:
#                     smallest_val = k_list.val
#                     smallest_list = k_list
#                 merged_list.next = k_list
#                 k_list = k_list.next

# 03-11-2023 Improvement
# The above cycles every list, len(list) times and so is akin to an O(n**2)
# Solution. The GOOD thing about linked lists is the nodes are single entiities
# and merely use pointers to get their next element. What I can do is heapify the above
# Start by pushing the head of every list onto a heap (based on their value), then
# pushpop the min valm pushing the next node in that list onto the heap. This brings
# things way down to O(nlogn) time. Now the question is, how do I use heapq with
# a user defined DS like Listnode?
# from typing import Optional
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         merged = ListNode(0)
#         node_heap = []

#         for list_i, list_head in enumerate(lists):
#             if list_head:
#                 heapq.heappush(node_heap, (list_head.val, list_i))

#         if not node_heap:
#             return None
#         merged_curr = merged

#         while node_heap:
#             curr_val, list_i = heapq.heappop(node_heap)
#             merged_curr.next = lists[list_i]
#             merged_curr = merged_curr.next
#             lists[list_i] = lists[list_i].next
#             if lists[list_i]:
#                 heapq.heappush(node_heap, (lists[list_i].val, list_i))

#         return merged.next

from typing import Optional
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def lt(self: ListNode, other: ListNode):
            return self.val < other.val

        ListNode.__lt__ = lt

        merged = ListNode(0)
        merged_curr = merged

        heapq.heapify(lists)
        while lists:
            merged_curr.next = heapq.heappop(lists)
            merged_curr = merged_curr.next
            if merged_curr.next:
                heapq.heappush(lists, merged_curr.next)
        return merged.next
