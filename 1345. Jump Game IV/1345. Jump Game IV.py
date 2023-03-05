# 03-04-2023 Leeetcode 1345. Jump Game IV
# https://leetcode.com/problems/jump-game-iv/

# These were just simple DP problems before
# So I can take one step forward, one back, or
# jump to ANY other node that has this same value
# Obviously we'll need to create a dictionary for that.

# The brute force method of solving this is BFS. Its possible that
# is the best I can do and it will alost sertainly time out.

# Wait... first instinct, this doesnt seem that hard:
# Start from the end, it can only be reached in 1 way-
# either from the index immediately before it, or by any other
# index that shares the same value. Mark each of those as being
# one step away in our dp array. Add all of these to our Queue
# and BFS. On reaching an empty space, or one with a higher reachabiliity
# score, update it and include it in the queue. If its current score is lower
# than terminate this branch. This does mean we are working backwards, so we
# need to use deque to add to the right and pop from the left so we know
# we have the min value on first reaching index 0


# So instead of checking if the next reachable index in dp is currently
# less than whats there, we could store all the visited indexes in a set
# and just seee if its been visited. As we are doing BFS, if its been
# visited previously we know it was already as soon as possible, and this
# new visit cant possibly be faster. Checking if its in a set is probably
# SO minorly quicker than checking value > than it hardly matters. We have
# to store the value in the DP array (I think? someo of these are tricksy
# and you can like, only store the last two vals). Having to add it to a set
# may negate the speed gained by checking set inclusion. Can test.

# Ah, skipped a step. I was only updating nodes if they were LESS than the
# current predicted path, but I need to include them in the queue if they
# are EQUAL to current predicted path value for them, as now they are a valid
# step in that sequence. Without performing an additional check, I am now
# sloppily updating their value to themsleves, leaving it unchanged. Not
# sure it warrants the extra check to reduce one assignment. I doubt
# on op is particularly quicker than the other.


from ast import List
import collections


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        last_i = len(arr) - 1
        if last_i == 0:
            return 0

        jump_map = collections.defaultdict(list)
        for index, value in enumerate(arr):
            jump_map[value].append(index)

        arrdp = list(range(last_i, -1, -1))
        bfsq = collections.deque()
        bfsq.append(last_i)

        while bfsq:
            curr_idx = bfsq.popleft()
            # As we are BFSing, first time we reach index 0 we are done
            if curr_idx - 1 == 0:
                return arrdp[curr_idx] + 1
            if curr_idx + 1 < last_i and arrdp[curr_idx + 1] >= arrdp[curr_idx] + 1:
                arrdp[curr_idx + 1] = arrdp[curr_idx] + 1
                bfsq.append(curr_idx + 1)
            # This is one step down from curr_idx, but we already checked its inbound above
            # using the "is one step down idx 0? check"
            if arrdp[curr_idx - 1] >= arrdp[curr_idx] + 1:
                arrdp[curr_idx - 1] = arrdp[curr_idx] + 1
                bfsq.append(curr_idx - 1)
            for jump_idx in jump_map[arr[curr_idx]]:
                if jump_idx == 0:
                    return arrdp[curr_idx] + 1
                if jump_idx != curr_idx and arrdp[jump_idx] > arrdp[curr_idx] + 1:
                    arrdp[jump_idx] = arrdp[curr_idx] + 1
                    bfsq.append(jump_idx)

        # We can safely default to this as we set it as len(arr) single steps from the end
        return arrdp[0]
