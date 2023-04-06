# 04-05-2023 Leetcode 1575. Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/description/

# Sounds like backtracking to me. BFS is FAR too large to store
# Wait, EVERY city is connected. So from a given point, you can go to
# ANY other point within fuel distance.

# I fucking hate when the answer is "lol, you though this was too big to recurse
# but just do it anyway"

# import cache from functools


class Solution:
    def countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        @cache
        def drive(trip):
            city, fuel_remaining = trip
            if fuel_remaining < 0:
                return 0
            here = 1 if city == finish else 0
            return here + sum(
                0
                if next_city == city
                else drive(
                    (
                        next_city,
                        fuel_remaining - abs(locations[next_city] - locations[city]),
                    )
                )
                for next_city in range(len(locations))
            ) % (10**9 + 7)

        return drive((start, fuel))
