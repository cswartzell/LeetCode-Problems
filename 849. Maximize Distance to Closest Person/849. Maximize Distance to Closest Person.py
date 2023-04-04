# 04-02-2023 Leetcode 849. Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/

# AHA! I caught the tricky edge case BEFORE jumping in to programming for once!
# So the obvious solution is a linear scan with two pointers: the last filled seat
# and the next one. Preferred seat is max(next_filled-last_filled // 2) for a O(n) O(1)
# solution. BUT! this algorthim only counts BETWEEN people. What about prior to the first
# or after the last person? Find those manually first I guess?

# There may be a cleaner way to do it, but I'll start with manual for the two end positions
# Weird that the problem doesnt mention

from itertools import groupby


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # guarenteed there is one filled seat, so no messy index errors
        first_filled, last_filled = seats.index(1), seats[::-1].index(1)
        max_dist = max(first_filled, last_filled)

        last_i = first_filled
        for i in range(first_filled + 1, len(seats) - last_filled):
            if seats[i]:
                max_dist = max(max_dist, (i - last_i) // 2)
                last_i = i

        return max_dist
