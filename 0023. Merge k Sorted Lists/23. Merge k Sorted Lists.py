# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

# Pretty naive solution, reusing the mergeTwoLists functions from before
# Could be done better using a heap, but Im not there yet in knowledge.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # catch empty lists
    if not len(lists):
        return None
    if len(lists) == 1:
        return lists[0]

    merged_head_prev = ListNode(-10000)  # I dont love it, but make a dummy node with a
    # default range that MUST be lower than any of the actual
    # node.vals, so it doesnt move and can be trimmed
    # Hey look, assign by address IS useful
    merged_list = merged_head_prev

    for next_list in lists:
        merged_list = self.mergeTwoLists(merged_list, next_list)

    return (
        merged_head_prev.next
    )  # Return the merged list, which starts AFTER the dummy node mergedHead

    # From LC #10, simply merge two ordered singly linked lists


def mergeTwoLists(self, list1, list2):
    mergedHead = ListNode(-1)  # start at -1 so curr.next starts at 0
    currNode = mergedHead
    while list1 and list2:
        if list1.val <= list2.val:
            currNode.next = list1
            list1 = list1.next
        else:
            currNode.next = list2
            list2 = list2.next
        currNode = currNode.next

    currNode.next = (
        list1 if list1 is not None else list2
    )  # As one list is empty, point the rest of the merged list to the remainder of the non empty list
    # Should work if both lists are empty simultaneously, as it the last node will then point ot None
    return mergedHead.next  # keep in mind our start node was a fake -1
