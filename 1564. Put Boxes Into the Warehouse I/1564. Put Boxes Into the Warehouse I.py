# 03-20-2023 Leetcode 1564. Put Boxes Into the Warehouse I
# https://leetcode.com/problems/put-boxes-into-the-warehouse-i/description/


# Since we cannot stack boxes, we want to maximize efficiency per room.
# We do NOT have to fit every box, but we want to fill as many rooms as possible
# We cannot reorder the rooms, but can reorder boxes. The rooms are monotonically
# decreasing in height from L to R.

# Step 1: Refigure the height of the rooms from L to R. Their current heights are lies
# The height of room[i] is min(room[i], min(rooms[0-i])).
# Once we have the correct height of the rooms, we want to put in boxes, and may as well
# go Tallest to Shortest, as our rooms go. Sort the boxes into a stack. Rooms go in a stack too

# Pop the LEFTMOST room (tallest) and keep popping boxes until one fits in said room. Once done,
# add to packed boxes. Move to next room and repeat until we are out of rooms or boxes.

# Oh SHIT is that a lot of input. 10**9. Well... we are mostly scanning linearly, but we
# DO want to do a sort...


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # last_min = 10**9 + 1
        # for i in range(len(warehouse)):
        #     warehouse[i] = min(warehouse[i], last_min)
        #     last_min = min(warehouse[i], last_min)

        # boxes.sort()

        # #Same answer, but better fits the prompt:
        # #Start with the last room. If it fits the current box (smallest), add and move one
        # #If NOT, no box will fit. KEEP this box, move to next room.
        # #Do til we run out of boxes or rooms
        # box_i, room_i = 0, len(warehouse) - 1
        # ans = 0
        # while box_i < len(boxes) and room_i >= 0:
        #     if boxes[box_i] <= warehouse[room_i]:
        #         ans += 1
        #         box_i += 1
        #     room_i -= 1

        # return ans

        # AHA! There is no need to reduce the room heights. By sorting the boxes
        # and starting at the largest size, we will have already processed the taller
        # boxes when switching between rooms, and all remaining boxes should be closer

        # last_min = 10**9 + 1
        # for i in range(len(warehouse)):
        #     warehouse[i] = min(warehouse[i], last_min)
        #     last_min = min(warehouse[i], last_min)

        boxes.sort(reverse=True)

        box_i, room_i = 0, 0
        ans = 0
        while box_i < len(boxes) and room_i < len(warehouse):
            if boxes[box_i] <= warehouse[room_i]:
                ans += 1
                room_i += 1
            box_i += 1

        return ans
