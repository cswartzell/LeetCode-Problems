# 11-20-2022 Leetcode 1926. Nearest Exit from Entrance in Maze
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# And for the third day in a row, I've "solved" the problem, but in
# such an inefficient way that it exceeds the time limit.
# Its a little disheartening. I've gone with an iterative solution
# here, but I HATE the multiple and statements in the long ifs
# Id rather have the repeated but cleaner code of the
# N S E W movement statements.
# Hmm... I can just have it cease processing a route if the current
# step count on popping a square is greater than the current
# least steps? No sense in processing that further if we've found
# a faster route already. Pop it and be done. This doesnt preclude
# the same square eventually being part of an easier faster route,
# but coming a different way. Nope. Still not enough. TLE

# What am I doing wrong I wonder?
# AHA! I am NOT doing a Breadth First Search as I intended. Because
# I am adding to a STACK and popping from the same, I am effectively
# actually doing a DEPTH first search. I may be chasing a crazy path
# thatll lead nowhere, and doing that for each path. If we use a
# Queue, we are prceeding from the start and "blobbing out". As each
# batch of squares get added to the queue in order, we can
# actually return on THE FIRST INSTANCE we reach a wall. Thats the real
# trick: From start, we add all possible steps that are 1 away. We process
# these and add all steps that are 2 away next, but if we find an edge we
# are done. We are processing the steps in strict order from the entrance
# so there will never be a shorter route developed later.

from collections import deque


class Solution:
    # For the first time ever, I'm editing the input call
    # Ive removed the specification that maze is List[List[str]], which
    # allows me to assign ints directly into the maze to track steps
    # freeing the need to create a parallel 2d grid for storing steps
    def nearestExit(self, maze: List[List], entrance: List[int]) -> int:
        step_queue = deque([entrance])
        max_steps = len(maze) * len(maze[0])
        path = [[max_steps for _ in range(len(maze[0]))] for _ in range(len(maze))]

        # -1 for least steps to exit indicates no exit
        least_steps = max_steps + 1

        # I think once we step off the entrance we can consider it a wall.
        # there are no sensible routes that would lead back to it.
        # Instead I guess we can store zero steps here and we can only step
        # onto a square if it would be fewer steps to get there than any other
        # route. As no route can beat zero steps, we wont return

        path[entrance[0]][entrance[1]] = 0

        while step_queue:
            curr_pos = step_queue.popleft()
            curr_steps = path[curr_pos[0]][curr_pos[1]]
            if curr_steps >= least_steps:
                continue
            for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if (
                    0 <= curr_pos[0] + r <= len(maze) - 1
                    and 0 <= curr_pos[1] + c <= len(maze[0]) - 1
                    and maze[curr_pos[0] + r][curr_pos[1] + c] == "."
                    and curr_steps + 1 < path[curr_pos[0] + r][curr_pos[1] + c]
                ):
                    path[curr_pos[0] + r][curr_pos[1] + c] = curr_steps + 1
                    if (
                        curr_pos[0] + r == 0
                        or curr_pos[0] + r == len(maze) - 1
                        or curr_pos[1] + c == 0
                        or curr_pos[1] + c == len(maze[0]) - 1
                    ):
                        return curr_steps + 1
                    else:
                        step_queue.append([curr_pos[0] + r, curr_pos[1] + c])
        return -1

        # North
        # if curr_pos[0] > 0 and maze[curr_pos[0]-1][curr_pos[1]] == "." and curr_steps + 1 < path[curr_pos[0]-1][curr_pos[1]]:
        #     path[curr_pos[0]-1][curr_pos[1]] = curr_steps + 1
        #     if curr_pos[0]-1 == 0:
        #         least_steps = min(least_steps, curr_steps + 1)
        #     else:
        #         step_stack.append([curr_pos[0]-1, curr_pos[1]])
        # #South
        # if curr_pos[0] < len(maze) - 1 and maze[curr_pos[0]+1][curr_pos[1]] == "." and curr_steps + 1 < path[curr_pos[0]+1][curr_pos[1]]:
        #     step_stack.append([curr_pos[0]+1, curr_pos[1]])
        #     path[curr_pos[0]+1][curr_pos[1]] = curr_steps + 1
        #     if curr_pos[0]+1 == len(maze) - 1:
        #         least_steps = min(least_steps, curr_steps + 1)
        #     else:
        #         step_stack.append([curr_pos[0]+1, curr_pos[1]])
        # #West
        # if curr_pos[1] > 0 and maze[curr_pos[0]][curr_pos[1]-1] == "." and curr_steps + 1 < path[curr_pos[0]][curr_pos[1]-1]:
        #     path[curr_pos[0]][curr_pos[1]-1] = curr_steps + 1
        #     if curr_pos[1]-1 == 0:
        #         least_steps = min(least_steps, curr_steps + 1)
        #     else:
        #         step_stack.append([curr_pos[0], curr_pos[1]-1])
        # #East
        # if curr_pos[1] < len(maze[0])-1 and maze[curr_pos[0]][curr_pos[1]+1] == "." and curr_steps + 1 < path[curr_pos[0]][curr_pos[1]+1]:
        #     path[curr_pos[0]][curr_pos[1]+1] = curr_steps + 1
        #     if curr_pos[1]+1 == len(maze[0]) - 1:
        #         least_steps = min(least_steps, curr_steps + 1)
        #     else:
        #         step_stack.append([curr_pos[0], curr_pos[1]+1])
