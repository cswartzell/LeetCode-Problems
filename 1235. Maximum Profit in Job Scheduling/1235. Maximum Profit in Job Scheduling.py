# 11-25-2022 Leetcode 1235. Maximum Profit in Job Scheduling
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

# First off, note there can be up to 50,000 entries in the jobs/profit
# lists. This automatically precludes brute force solutions like "generate
# all valid orders and compare profits", not that this is ever what
# leetcode solutions are looking for. If done recursively wed hit the stack

# Ok, well we have to start the day somehow. There will always be
# some job/s that start first. Oh wait! Does this kind of look like that
# monotonic stack problem? 907. Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/

# We could include the idea of rates: For each hour we can earn
# a rate, which is the jobs total/hours. This isnt enough to give
# a solution, but may be a component.


# Ok, didnt really know how to start and once again had to read
# through the answer. I rather like the last option, and it seems
# so simple that I should have been able to come up with it.
# keep a list of "chains" of current jobs. For each new job, add
# it to the chain that would be most profitable. We only need to compare
# chains that dont conflict: chains that are "ongoing" cannot include this
# new job so we can ignore them. All the chains that are "done" at this point
# can thus be considered precursors. We dont need to store them all again, they
# have been evaluated to this point: All future jobs can be added to each of them,
# so we only need to store the most profitable one. We want to effeciently compare
# chains, so we can store them in a heap (sorted by END time), pop all non-conflicting
# chains (those that end before the current jobs start) into a list, add the current job
# to the most profitable of the list and push only that onto the heap. The rest of the
# heap are the jobs that are "still cooking".
# NOTE: If there are NO chains that we can add to (the popped list is empty)
# Then we start a new chain using this job as the first link

# For the heap what do we need to store? Ending time and curr_profit for that chain
# I think right? Stored as a list with ending time first, that makes heapifying it
# simple

import heapq


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(
            [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        )
        # there is not "heap", DS. Rather, you use heap ops to maintain a list AS a heap
        # Instantiate first job
        job_chains = []
        # heapq.heappush(job_chains, (jobs[0][1],jobs[0][2]))

        # retains the "best" previous profit chain so we can add new jobs to it
        # without having to restore all previous chains to the heap. Its sort of a DP
        # type algorithm: We've already calculated the best profit for all job combinations
        # prior to this new one we are looking at.
        max_profit = 0
        for i in range(len(jobs)):
            extendable_chains = []
            while job_chains and job_chains[0][0] <= jobs[i][0]:
                popped_chain = heapq.heappop(job_chains)
                max_profit = max(max_profit, popped_chain[1])
                extendable_chains.append(popped_chain)
            if not extendable_chains:
                # not so sure about adding max_profit here, but shouold work?
                heapq.heappush(job_chains, (jobs[i][1], jobs[i][2] + max_profit))
            else:
                # heapq.heappush(job_chains, (jobs[i][1],max(extendable_chains, key=lambda x:x[1])[1] + jobs[i][2]))
                heapq.heappush(job_chains, (jobs[i][1], max_profit + jobs[i][2]))
        return max([x[1] for x in job_chains])

        # I think Im getting good at least at coding, if not generating the algorithms in
        # the first place, if "clever, compact,  yet incomprehensible" is a measure of "good"
