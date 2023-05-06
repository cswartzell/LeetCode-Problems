class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # We can skip the 0 index stair, effectively we are on "cost[-1]"
        # Similarly, the top is beyond the end of the list, so "cost[len(cost)]"
        # where normally that would be out of bounds. Its free to start, and take
        # the last step, or "cost = 0". If we add 0 to either side, we can then simply
        # run the update loop without having to check for OOB errors as the list will be
        # 3 long. I guess we have to check an empty list...

        if len(cost) == 0:  # prevents index errors
            return 0

        cost = [0] + cost + [0]

        # if len(cost) == 1:    #prevents index errors
        #     return cost[0]
        # cost[-2] += cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1 : i + 3])

        return cost[0]
