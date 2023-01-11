# 01-10-2023 Leetcode 533. Lonely Pixel II
# https://leetcode.com/problems/lonely-pixel-ii/description/


# literally the worst problem yet


# I dont think there is an O(1) solution that doesnt involve recalculating
# whole rows/cols. We either have to store at least the count totals for
# one or the other, or recalculate rows/cols EACH time we get to them.
# We COULD store only the shorter of the two to reduce space to
# O(min(m,n)) but that would require two copies of the solution I think,
# flipping the iteration. Not sure there is a supoer clever way around it


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        row_target, col_target = [], []

        for row_i in range(len(picture)):
            row_target += [target == sum(1 for char in picture[row_i] if char == "B")]
        for col_i in range(len(picture[0])):
            col_target += [target == sum(1 for row in picture if row[col_i] == "B")]
            # col_target += [target == sum(1 for char in zip(*picture) if char == 'B')]

        lonely_ps = 0

        for col_i in range(len(picture[0])):
            seen_row = None
            count = 0
            for row_i in range(len(picture)):
                if (
                    row_target[row_i]
                    and col_target[col_i]
                    and picture[row_i][col_i] == "B"
                ):
                    if not seen_row:
                        seen_row = picture[row_i]
                    elif picture[row_i] != seen_row:
                        count = 0
                        break
                    count += 1
            lonely_ps += target if count == target else 0
            lonely_ps += count

        return lonely_ps


# class Solution:
#     def findBlackPixel(self, picture, N):
#         """
#         :type picture: List[List[str]]
#         :type N: int
#         :rtype: int
#         """
#         count = 0
#         for c in zip(*picture):
#             if c.count('B') != N: continue
#             first_row = picture[c.index('B')]
#             if first_row.count('B') != N: continue
#             if picture.count(first_row) != N: continue
#             count += 1
#         return count*N


# row_target, col_target = 0, 0

# for row_i in range(len(picture)):
#     row_target += 1 if target == sum(1 for char in picture[row_i] if char == 'B') else 0
# for col_i in range(len(picture[0])):
#     col_target += 1 if target == sum(1 for row in picture if row[col_i] == 'B') else 0

# return row_target * col_target
