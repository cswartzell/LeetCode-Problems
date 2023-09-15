#11-13-2023 Neetcode 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Time: 14 mins


# binary search to find row, binary search row

from bisect import bisect_left as bl, bisect_right as br


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         row = bisect.bisect_right([matrix[x][0] for x in range(len(matrix))], target) - 1
#         (idx := bisect.bisect_left(matrix[row], target))
#         return matrix[row][idx] == target if idx < len(matrix[row]) else False 
        





# # import bisect

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         row = max(bisect.bisect_right([r[0] for r in matrix], target) - 1, 0)
#         col = min(bisect.bisect_left(matrix[row], target), len(matrix[0])-1)
#         return matrix[row][col] == target

# from bisect import bisect_left as bl, bisect_right as br

class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:       
        return m[(R:=br([r[0]for r in m],t)-1)][min(bl(m[R],t),len(m[0])-1)]==t
