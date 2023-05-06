# 11-26-2022 LeetCode 286. Walls and Gates
# https://leetcode.com/problems/walls-and-gates/description/

#I guess start with a linear scan and note the positions of the gates.
#BFS from each, adding steps so long as 0 < curr_step_count < grid_pos 

#Yep, standard grid based ortho BFS search pattern.

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #find the gates:
        gates = []
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    gates.append((row,col,0))
        
        while gates:
            steps = [gates.pop()]
            while steps:
                curr_pos = steps.pop()
                for row_d, col_d in [(-1,0), (1,0),(0,-1),(0,1)]:
                    if 0 <= curr_pos[0] + row_d < len(rooms) and 0 <= curr_pos[1] + col_d < len(rooms[0]) and 0 < rooms[curr_pos[0] + row_d][curr_pos[1] + col_d] > curr_pos[2] + 1:
                        rooms[curr_pos[0] + row_d][curr_pos[1] + col_d] = curr_pos[2] + 1
                        steps.append((curr_pos[0] + row_d, curr_pos[1] + col_d, curr_pos[2] + 1))

        pass
