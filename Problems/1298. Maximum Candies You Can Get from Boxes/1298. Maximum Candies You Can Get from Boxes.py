# 03-02-23 Leetcode 1298. Maximum Candies You Can Get from Boxes
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/

# Interesting. I guess its just a matter of doing it effeciently? It seems straightforward
# There are only 1000 possible boxes, and keys. Im just going to make sets to track
# keys+unlocked boxes in one hand, and boxes available on the other. For each pass through
# a while loop, we process the boxes we have on hand that CAN be opened, adding them to their
# respective sets. This way we are only using sets for checking what we can do and not
# at all iterating over lists


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        # Openable tracks both boxes we dont need keys for (unlocked), and keys we've acquired
        # Boxes remaining are boxes we have discovered
        openable = set()
        boxes_remaining = set()
        candy = 0

        # No keys to start with, so the only thing to add to Openable are boxes with status == 1
        # Add ALL initial boxes to boxes_remaining
        for box in initialBoxes:
            if status[box] == 1:
                openable.add(box)
            boxes_remaining.add(box)

        # Heck yeah walrus operator!
        # Get the Interestion of boxes we have and boxes that can be opened
        # and, if there is no intersection, we are done
        while to_open := openable.intersection(boxes_remaining):
            for box in to_open:  # For each openable box
                candy += candies[box]  # Get the Candy
                openable.remove(box)  # Remove the box from our lists
                boxes_remaining.remove(
                    box
                )  # Remove the box from our lists (TLE if not from both, even though technically not necessary)
                openable.update(keys[box])  # Add all new keys to openable
                for new_box in containedBoxes[box]:
                    boxes_remaining.add(
                        new_box
                    )  # Add all new boxes discovered to boxes_remaining
                    if status[new_box] == 1:
                        openable.add(
                            new_box
                        )  # and add them to openable as well if they are unlocked

        return candy
