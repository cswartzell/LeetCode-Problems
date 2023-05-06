# I mean, my intuition says we know nothing about
# what each row contains, only that its increasing, so we
# must check each row from its first index until we find a
# val higher then our target, then start the next row from
# its beginning.

# Well thats not quite true. We know that for target n, it
# must be within the first n rows, and that assumes a vertical
# matrix. It doesnt explicitly state the values are unique, but
# if it is strictly increasing in both directions than it must be
# by consequence. The same logic applies within a row, and since
# the two searches are ordered, we can use fancy techniques like
# binary search to speed things along. Wait... I'm not sure thats
# true. We can certainly use a b search to speed along checking
# within a row, but noting about the sorted nature of the rows
# might indicate which row the target might be in within its limits
# it could be anywhere with nearly equal probibilty... What/how
# do we bsearch what row to check?


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i, j = 0, 0
        # while i < len(matrix) and matrix[i][0] <= target:
        #     while j < len(matrix[0])-1 and matrix[i][j] < target:
        #         j += 1
        #     if matrix[i][j] == target:
        #         return True
        #     i += 1
        #     j = 0
        # return False

        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False
