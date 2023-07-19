# 07-19-2023 Leetcode 826. Most Profit Assigning Work
# https://leetcode.com/problems/most-profit-assigning-work/description/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        workers = sorted(worker[::])
        jobs = sorted(zip(profit, difficulty))
        total = 0

        while jobs and workers:
            curr_worker = workers.pop()
            
            while jobs and jobs[-1][1] > curr_worker:
                jobs.pop()

            if jobs:
                total += jobs[-1][0]
        
        return total
