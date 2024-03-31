# 03-30-2024 Leetcode 2532. Time to Cross a Bridge
# https://leetcode.com/problems/time-to-cross-a-bridge/description/
# Time: like 45? Challenge: 5/10 but the answer DOESNT match the prompt

# First things first, lets compute priorities so we only have to do it once.
# Make a prioties_compute array of. Now for each worker i we will add a tuple
# to the array: (-(LtoR + RtoL), -workerIdx). 
# The rules on this are slightly convoluted: We are prioritizing LESS efficient workers.
# The HIGHEST combined crossing time is the LEAST efficient worker, and we want "least efficient"
# to be zero indexed, so negate the sum of the crossing time so it can be minsorted. Similarly, if
# two workers are tied for crossing times, the one with the HIGHER idx is LESS efficient. So we
# need to negate that too for the tie breaker... I think this is the same as just reverse sorting it

# Hey, instead of creating a whole new array for "efficiency of worker i", we could extend each entry
# of worker i to hold a 5th value. However, we can eliminate a bunch of nested referencing by realizing
# the following: We only need the idx of the ith worker to determine his efficiency, then never again. 
# We can just renumber all the workers BY there efficiency. The least efficient worker IS worker 0, the
# next LEAST efficient worker IS worker 1. So we just use the same values for worker i, a 4x len array,
# but assign it to efficiency of worker i: make a new eworkers array. 

# Ok, now given a simple worker idx instead of a whole tuple we can determine at any of the
# 4 points how long it takes worker[idx] to do whatever operation, and given a heap of
# waiting workers, we know which goes first. 

# The left and right of the bridge need to be minheaps. Do we need to keep warehouse heaps as well?
# Yes, it simplifies competing priorities (time_available, Worker_priority). It keeps the logic clean:
# We have 4 heaps. Yes 4. left_working, left_waiting, right_waiting, right_working. 

# 1) For the current time, release all workers that are done FROM right_working into right_waiting (if any)
# 2) If there are ANY workers in right_waiting, send him accross, FROM right_waiting TO left_working, where
# they will work til curr_time + worker[RTOL] + worker[DROP]. 
# 3) Update the time to our curr_time + crossing_worker[RTOL]

# REPEAT ABOVE TILL THERE ARE NO WORKERS IN right_waiting. The current time will then be less than the release
# time of any workers in right_working. ONLY at this point to we care about workers on the left side. They
# may have all completed their tasks and have been stewing in the factory, but we dont update that til now. 

# 4) Similar to the above, lets now release all releable workers FROM left_working that are done by curr_time
# into left_waiting. TIME DOES NOT ADVANCE HERE, so there isnt a possibility we gain a right crosser. We can
# move on to moving the highest priority left guy.
# 5) The highest priority person in left_waiting (if any) now crosses. FROM left_waiting TO right_working
# where their release time is (curr_time + crossing_worker[LTOR] + crossing_worker[LIFT])
# 6) Update curr_time += crossing_worker[LTOR]

# As time has advanced we MAY have gained some free workers from right_working that need to be added to 
# right_waiting, and thus then one needs to cross. So repeate after sending the left guy across. 

# Now we simply need to control the outer loop. Each time a person crosses FROM left_waiting we know this guy
# is eventually going to get a box, so decrement n now. We stop sending guys from left when n == 0, add that
# to the above conditions. We stop the whole process when n == 0 and left_working, right_witing, and right_working
# are all zero: all boxes are moved and all workers are done and waiting on the left bank. 

from heapq import heappop as hpop, heappush as hpush


class Solution:
    def findCrossingTime(self, n: int, k: int, workers: List[List[int]]) -> int:
        LTOR, LIFT, RTOL, DROP = 0, 1, 2, 3
        DONE_AT_TIME, WORKER = 0, 1
    

        efficiency_list = [[worker[LTOR] + worker[RTOL], idx] for idx, worker in enumerate(workers)]
        efficiency_list.sort(reverse = True)
        eworkers = []
        for curr in efficiency_list:
            eworkers.append(workers[curr[WORKER]])

        left_working, right_waiting, right_working = [], [], []
        left_waiting = [*range(k)]

        curr_time = 0
        while n  or right_waiting or right_working:
            # 0) Track if NO workers crossed:
            crossing_worker = None
            # 1) free finished right_workers
            while right_working and right_working[0][DONE_AT_TIME] <= curr_time:
                hpush(right_waiting, hpop(right_working)[WORKER]) 
            # 2) If right_waiting, send ONE guy left
            if right_waiting:
                crossing_worker = hpop(right_waiting)
                hpush(left_working, (curr_time + eworkers[crossing_worker][RTOL] + eworkers[crossing_worker][DROP], crossing_worker))
                # 3) update time after ONE cross
                curr_time += eworkers[crossing_worker][RTOL]
            # There were no waiting workers on right, now work on left; 
            elif n:
                # 4) release finished left_workers
                while left_working and left_working[0][DONE_AT_TIME] <= curr_time:
                    hpush(left_waiting, hpop(left_working)[WORKER]) 
                # 5) If left_waiting, AND boxes left to grab,  send ONE guy right
                if left_waiting:
                    crossing_worker = hpop(left_waiting)
                    hpush(right_working, (curr_time + eworkers[crossing_worker][LTOR] + eworkers[crossing_worker][LIFT], crossing_worker))
                    # 6) update time
                    curr_time += eworkers[crossing_worker][LTOR]
                    n -= 1
            if crossing_worker == None:
                # 7) Nobody crossed, nobody was ready (everyone is working). We need to advance time:
                # Ughh, edge case. We DONT advance time for the left workers trapped in the warehouse if there are no
                # more boxes to grab. They just play cards. Otherwise we get stuck in a loop if its the lower value. 
                l_time = left_working[0][DONE_AT_TIME] if left_working and n > 0 else math.inf  
                r_time = right_working[0][DONE_AT_TIME] if right_working else math.inf
                curr_time = min(l_time, r_time)
                    
        # Now all boxes have been moved to the left warehouse. Some people are still working, at a minimum the LAST
        # guy to cross literally just "entered" the warehouse. This is where the problem and examples diverge. The PROBLEM
        # states we return the time when all boxes have been moved AND dropped. The examplese stop as soon as the last box
        # crosses the bridge. The latter would be to just return curr_time. The former means we have to process all remaining
        # left_workers. As left_workers is ordered by release time, we just return the max release time in left_workers, we 
        # dont need to add them one at a time to a running total. 

        #EXAMPLES STYLE RETURN:
        return curr_time

        #PROBLEM STATEMENT RETURN:
        # return max(left_working, key=lambda x:x[DONE_AT_TIME])[DONE_AT_TIME]