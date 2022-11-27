# 11-26-2022 LeetCode 752. Open the Lock
# https://leetcode.com/problems/open-the-lock/description/

# is... is this a 4d BFS? It could be? Just note the deadlocks
# in 4d space, and starting at the first position start making
# our way toward the target?

# It should just be the 4d manhattan distance... but as the wheels
# go backwards not quite. There'd have to be a hell of a lot of
# deadlocks to make a significant difference: like "every number
# where the last wheel is a 3 except the target and when the second
# wheel is an 8"

# I guess we can compress it down to 2d? 100x100=10000. Just multiply
# the first and third wheels BY 10 and add them respectively to the
# second and forth wheels. Doesnt reduce the space but may be fewer
# counters and loops and such

# Well, we know some things, like a lower bound: The sum of the
# four dials is the minimum moves. No wait, we can go backwards...
# The lower bound is the sum of the 4 dials least moves...

# Spins to get X Digits (starting from 0)
# Digits: 0 1 2 3 4 5 6 7 8 9
# Spins:  0 1 2 3 4 5 4 3 2 1
# min(x, 10-x)

# Spins to go from x->y: min( max(x,y)-min(x,y), 10-max(x,y)-min(x,y) )
# so sum this for 0->target for each dial


# Ok, so lets think about this just like our standard 2d BFS, but 4d:
# Each cell has 8 neighbors instead of 4 (+1/-1 for each dimension): Easy
# Each step toward a neighbor adds one to curr_step, stored part of 5d tuple
# on the stack.
# Instead of checking bounds, we need to wrap: (cur_pos_d + offset + 10)%10
# Thus (9 + 1 + 10) % 10 = 0 and (0 - 1 + 10) % 10 = 9
# We only add to our stack if the neighborind cell is 2 or MORE than current cell
# We should set all cells other than deadlocks arbitrarily high to start with
# We simply dont add deadlocks to the stack ever
# This is flood fill from a SINGLE start location. We dont need to loop or check
# new locations. Everything possible to access will be accessible FROM the start
# locations (or is blocked off ancd can be ignored). Therefore, we only need to
# seed a stack and go from there. No need to loop through multiple seeds.
# Once the stack is empty... and it may be a while, we simply return the value
# (steps taken) to reach the target. If the target is still the preset value
# then there is no way to reach the target from START.

# Simple in its complexity? Insane? It seems like there is maybe a FAR
# simpler way of doing this right? Its in the BFS problem set though, so
# thats a pretty strong hint.


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 5d tuple, 4 neigbhbor dimensions. steps[4] is curr_steps to get to cell

        # Base Case- The lock is stuck to start.
        if "0000" in deadends:
            return -1

        # The OTHER base case: The target is the start.
        if target == "0000":
            return 0

        # Setup grid, even though there is aparently no need. As we are doing
        # BFS, we WILL be visiting all nodes in order, as fast as possible.
        # This is only necessary if there were multiple start points. I
        # chose to do it this way as I suspect I can reuse this code in the future

        # Instead, we can merely use the queue to store adjacent nodes to our
        # seed node and proceed from there. As long as we are popping left, we
        # will reach our target (if possible) eventually, and in as few steps
        # as is possible. We would need a "visied" hashmap, and really thats more
        # or less the same as an indexed 4d array right?

        # We may have to process the entire set of other nodes
        # that are the same steps away from START as TARGET, but no nodes that are
        # further
        # If the target isnt found by the time we run out of steps, return -1

        space = [
            [[[10000 for _ in range(10)] for _ in range(10)] for _ in range(10)]
            for _ in range(10)
        ]
        # Markout dead positions
        for dl0, dl1, dl2, dl3 in deadends:
            space[int(dl0)][int(dl1)][int(dl2)][int(dl3)] = -2
        # Notate the target
        space[int(target[0])][int(target[1])][int(target[2])][int(target[3])] = -1

        asteps = deque()
        asteps.append((0, 0, 0, 0, 0))
        while asteps:
            curr_pos = asteps.popleft()
            curr_steps = curr_pos[4]
            for d0, d1, d2, d3 in [
                (-1, 0, 0, 0),
                (1, 0, 0, 0),
                (0, -1, 0, 0),
                (0, 1, 0, 0),
                (0, 0, -1, 0),
                (0, 0, 1, 0),
                (0, 0, 0, -1),
                (0, 0, 0, 1),
            ]:
                cd0, cd1, cd2, cd3 = (
                    (curr_pos[0] + d0 + 10) % 10,
                    (curr_pos[1] + d1 + 10) % 10,
                    (curr_pos[2] + d2 + 10) % 10,
                    (curr_pos[3] + d3 + 10) % 10,
                )
                if space[cd0][cd1][cd2][cd3] == -1:
                    return curr_steps + 1
                if (
                    space[cd0][cd1][cd2][cd3] != -2
                    and space[cd0][cd1][cd2][cd3] > curr_steps + 1
                ):
                    space[cd0][cd1][cd2][cd3] = curr_steps + 1
                    asteps.append((cd0, cd1, cd2, cd3, curr_steps + 1))

        return space[int(target[0])][int(target[1])][int(target[2])][int(target[3])]
