# 05-31-2023 Leetcode 1091. Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

#Standard BFS, but prioritize diagonals first? Or rather specific order: 
# SE, S, E, SW, NE, W, N, NW. Does this work? Not sure as the distance of the steps
# is NOT equivalent. Really what we want to prioritize is the path that stays true to 
# to the center diagonal the most. 

#Down and right is ALWAYS better than just down or just right

#Wait, I think I am thinking about this all wrong. All I have to do is BFS spreading the num
#steps. Obnoxiously the walls are marked as 1 so lets count negative so we dont have to loop through
# and change them all.

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1
        if len(grid) == 1:
            return 1        
        
        orth = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (0, -1), (-1, 0), (-1, -1)]
        grid[0][0] = -1
        # currLen = -1
        currSteps = []
        nextSteps = [(0,0)]
        while nextSteps:
            currSteps = nextSteps
            nextSteps = []

            while currSteps:
                currRow, currCol = currSteps.pop()
                currLen = grid[currRow][currCol]
                for offsetRow, offsetCol in orth:
                    newRow = currRow + offsetRow
                    newCol = currCol + offsetCol
                    if newRow == newCol == len(grid) -1:
                        return -(currLen -1)
                    if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid):
                        continue

                    if grid[newRow][newCol] == 0: 
                        grid[newRow][newCol] = currLen -1
                        nextSteps.append((newRow,newCol))
            
        return -1