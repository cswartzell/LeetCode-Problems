# if you can move diagonally, (curr_pos, next are not orthogonal) do so
# otherwise its just the remaining manhattan dist

# we can use absolute value and ignore relative up/down/left/right

# class Solution:
#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         ans = 0
#         for i in range(1, len(points)):
#             x1, y1 = points[i-1]
#             x2, y2 = points[i]

#             x_dist = abs(x1 -x2)
#             y_dist = abs(y1 - y2)

#             # ans += x_dist + y_dist - min(x_dist, y_dist)
#             # ans += (x_dist := abs(x1 -x2)) + (y_dist := abs(y1 - y2)) - min(x_dist, y_dist)
#             ans += (x_dist := abs(x1 -x2)) + (y_dist := abs(y1 - y2)) - min(x_dist, y_dist)
#         return ans


class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        return sum(
            (x := abs(p[i - 1][0] - p[i][0]))
            + (y := abs(p[i - 1][1] - p[i][1]))
            - min(x, y)
            for i in range(1, len(p))
        )
