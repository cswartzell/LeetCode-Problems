# 03-07-2023 Leetcode 2187. Minimum Time to Complete Trips
# https://leetcode.com/problems/minimum-time-to-complete-trips/

#So we have a fundamental time unit: the shortest time a bus can take is 1
#so PER unit of time, each bus completes 1/time[i] of a trip. 

#So we can sum(time_spent//x for x in time[i]) to get the total number of trips
#in time_spent. We could maybe binary search our way toward time spent?

#As the number of trips can be HUGE it may be good to note that after the
# Least Common Multiple of all times, the buses will be synched again as they
# were at the top of the problem. There will be a whole number of trips. We can
# use this divide the number of trips by this MEGA clock cycles to get close
# to the remainder of individual trips. If the number of trips is less than this
# megacylce, we know they wont ever sync prior



class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        # if totalTrips is fucking gigantic and we think the LCM is easy to calculate
        # lcm = math.lcm(*time)
        # megacycle = sum(lcm//trip_time for trip_time in time)
        # time_spent = (totalTrips // megacycle) * lcm
        # totalTrips %= megacycle


        #Binary search? Im not even sure its terribly logical, but hey:
        #Holy shit, its among the FASTEST solutions?!
       
        
        slowest_route, fastest_route = max(time), min(time)
        lower_bound = fastest_route * math.ceil( totalTrips/len(time) )
        # upper_bound = min((slowest_route * math.ceil( totalTrips/len(time) )), fastest_route * totalTrips) 
        upper_bound = slowest_route * math.ceil( totalTrips/len(time) ) 

        while lower_bound < upper_bound:
            mid = lower_bound + (upper_bound - lower_bound) // 2
            curr_trips = sum(mid//trip for trip in time)
            if curr_trips >= totalTrips: #because we are summing ceil operations, we actually need to keep lowering mid
                                         # until it DOESNT meet our total number of trips
                upper_bound = mid
            elif curr_trips <  totalTrips:
                lower_bound = mid + 1
            else:
                return mid
        
        return upper_bound