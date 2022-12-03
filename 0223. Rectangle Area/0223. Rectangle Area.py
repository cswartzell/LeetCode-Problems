# 11-17-2022 LeetCode 223. Rectangle Area
# https://leetcode.com/problems/rectangle-area/description/

# Pretty straighforward: sum the area of the two less the overlap
# Im not entirely sure I would have imediately recognized that the
# overlap would be an issue without the image, a VERY important
# lesson for interviews. DONT JUST CODE. Think about the problem,
# possible edge cases and, in particular in interviews where this
# is literally the goal, pitfalls and tricks intended to trap
# coders who dont bother to think it through.

# My first solution is a little cumbersome, but does guarentee a
# positive value for the overlap if one exists. I knew it was
# repetitive/symmetric and there was certainly a way to
# generate the overlaps of the two components simultaneously
# My solution checks if 1 is ahead of 2, of if 2 is ahead of 1
# before it gets the correct overlap math. The min/max solution
# is clever, but returns a negative value if there is no overlap
# so you need another max with 0 to account for this. Its far less
# readable, but executes MUCH faster.


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        # overlap_x = 0
        # overlap_y = 0
        # if bx1 >= ax1 and bx1 < ax2:
        #     overlap_x = min(ax2, bx2) - bx1
        # elif ax1 >= bx1 and ax1 < bx2:
        #     overlap_x = min(bx2, ax2) - ax1

        # if by1 >= ay1 and by1 < ay2:
        #     overlap_y = min(ay2, by2) - by1
        # elif ay1 >= by1 and ay1 < by2:
        #     overlap_y = min(by2, ay2) - ay1

        # overlap_x = max( (min(ax2,bx2) - max(ax1, bx1)), 0 )
        # overlap_y = max( (min(ay2,by2) - max(ay1, by1)), 0 )

        # One line, beats 99%
        return (
            (ax2 - ax1) * (ay2 - ay1)
            + (bx2 - bx1) * (by2 - by1)
            - (
                max((min(ax2, bx2) - max(ax1, bx1)), 0)
                * max((min(ay2, by2) - max(ay1, by1)), 0)
            )
        )
