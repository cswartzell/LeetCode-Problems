# 01-08-2023 Leetcode 134. Gas Station
# https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_i = 0
        min_gas = math.inf

        for i in range(len(gas)):
            gas[i] -= cost[i]
            cost[i] = (
                (gas[i] + cost[i - 1]) if i != 0 else gas[i] + (gas[-1] - cost[-1])
            )
            if cost[i] < min_gas:
                min_gas = cost[i]
                min_i = i

        start = (min_i + 1) % len(cost)
        curr_pos = start
        tank = gas[curr_pos]
        curr_pos = (curr_pos + 1) % len(cost)
        while tank >= 0:
            if curr_pos == start:
                return curr_pos
            tank += gas[curr_pos]
            curr_pos = (curr_pos + 1) % len(cost)

        return -1
