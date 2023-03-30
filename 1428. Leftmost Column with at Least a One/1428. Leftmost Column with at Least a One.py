# 03-29-2023 Leetcode 1428. Leftmost Column with at Least a One
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/description/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


# Wait, what? The ros and cols can be up to 100x100, so 10,000 cells, but
# we have to guarentee an answer by querying no more then 1000 cells?

# So we can sort of 3d binary search. Start with the middle column (what a dick move)
# And start at the top of that column and I guess linearly search down. Stop when
# you get to the FIRST one. As the columns are in sorted order, all cols to the left
# are less than this number, so we can start future searches at this row only searching
# down. If we DONT find any ones, we've eliminated all cols to the left. If we do, we can
# elimnate all cols to the right. Repeat.

# No to prove that this searches the space in less than 1000 queries:
# ¯\_(ツ)_/¯

# No, wait, the problem is entirely fucking dumb. The rows have nothing to do with one another.
# EACH row is sorted... as in, all zeros followed by all ones. So, we need to go row by row and
# find the left most 1. We can binary search each row, and the Right pointer gets updated on each#
# search.


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        # rows, cols =  binaryMatrix.dimensions()

        # L, R = 0, cols - 1
        # while L <= R:
        #     M = L  + (R-L)//2
        #     # any() shortcuts too
        #     # Once a row DOESNT have a 1 in the searched for place (and weve)
        #     # found at least one) we can stop searching this row for it ever again.
        #     # We could keep the row index in a "dont need to check list"
        #     # But I think not bothering still solves this in at most 800 queries
        #     if any(binaryMatrix.get(row, M) for row in range(rows)):
        #         R = M - 1
        #     else:
        #         L = M + 1
        # return R + 1 if L < cols else -1

        rows, cols = binaryMatrix.dimensions()
        L, R = 0, cols - 1

        for row in range(rows):
            L = 0
            while L <= R:
                M = L + (R - L) // 2
                if binaryMatrix.get(row, M):
                    R = M - 1
                else:
                    L = M + 1
        return R + 1 if R != cols - 1 else -1
