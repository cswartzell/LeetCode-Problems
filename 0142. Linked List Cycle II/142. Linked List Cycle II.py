# 03-09-2023 Leetcode 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description/

# "Do you know floyds method", the challenge.
# Answer? kind of. I can explain the gist.
# But I forget exactly how you do it. Once they meet,
# You reset the fast pointer? To root maybe?
# The second time they meet, THATS the start of the cycle.
# Its something VERY akin to this

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tort, hare = head, head

        while hare and tort:
            tort = tort.next
            hare = hare.next.next if hare.next else None
            if not hare:
                break
            if hare == tort:
                tort2ga = head
                while tort != tort2ga:
                    tort, tort2ga = tort.next, tort2ga.next
                return tort2ga

        return None

        # #why do they put in stupid cases like "lol, there are no nodes to check"
        # if not head:
        #     return None

        # turtle = head.next
        # hare = None
        # if head.next:
        #     hare = head.next.next

        # if not turtle or not hare:
        #     return None

        # while turtle != hare:
        #     turtle = turtle.next
        #     if hare.next:
        #         hare = hare.next.next
        #     if hare == None or turtle == None:
        #         return None

        # #reset the hare, we know there is a cycle
        # #Oh wait. Maybe you reset the turtle?
        # #No, its turtle2. Turtles all the way
        # # turtle = head.next
        # # while turtle != hare:
        # #     turtle = turtle.next

        # turtle2 = head
        # while turtle != turtle2:
        #     turtle, turtle2 = turtle.next, turtle2.next

        # return turtle
