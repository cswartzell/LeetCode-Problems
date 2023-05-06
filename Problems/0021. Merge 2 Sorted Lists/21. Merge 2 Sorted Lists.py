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
