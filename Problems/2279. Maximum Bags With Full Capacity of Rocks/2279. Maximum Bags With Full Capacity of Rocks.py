# 12-26-2022 Leetcode 2279. Maximum Bags With Full Capacity of Rocks
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/


# Just order the bags by how many rocks it will take to fill them,
# then do so?


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:

        # Store Remaining Capacity OVER existing Capacity
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]

        capacity.sort()

        count = 0
        i = 0
        for i in range(len(capacity)):
            additionalRocks -= capacity[i]
            if additionalRocks >= 0:
                count += 1
            else:
                break

        return count
