    # 03-12-2023 Leetcode 2361. Minimum Costs Using the Train Line
    # https://leetcode.com/problems/minimum-costs-using-the-train-line/description/

    #Recursive DP. Need to pass what line we are on
    #Wait, we are going to blow the stack arent we?


    #So trivially, if the cost of the transfer saves more in ONE trip, we should
    # transfer to express. Conversely, if the cost difference of a slow trip is 
    # cheaper than the transfer fee we should switch to slow. We can always switch back.


    class Solution:
        def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
            n = len(regular)
            dpr, dpe, res = 0, expressCost, [0] * n
            
            for i in range(1, n + 1):
                dpr, dpe = min(dpr, dpe) + regular[i - 1],  min(dpr + expressCost, dpe) + express[i - 1]
                res[i - 1] = min(dpr, dpe)
            return res