# 05-02-2023 Leetcode 1870. Minimum Speed to Arrive on Time
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # First, each train other than the last effectively takes at least one hour, 
        # so if there are more trains than hours we are screwed
        if len(dist) > math.ceil(hour):
            return -1
        
        # Second, if there are exactly as many trains as the floor of hours
        # then each train needs to take at most one hour, meaning they travel
        # at their distance per hour and the last train must get there in the
        # fractional time, so dist[-1]/ hour-int(hour). Max of all these
        # finalTime = hour-int(hour)
        # maxSpeed = max(  dist[:-1] + [int(dist[-1]/finalTime)] if finalTime else dist  )
        # if len(dist) == math.ceil(hour):
        #     return maxSpeed

        #if there are spare hours... some trains can be slower. 
        #Specifically we want the fastest train to slow down and re-evlauate
        # speed = 1
        # while True:
        #     firstTrains = sum(math.ceil(train/speed) for train in dist[:-1])
        #     totalTime = firstTrains + dist[-1]/speed
        #     if totalTime > hour:
        #         speed += 1
        #     else: 
        #         return speed

        # speed = 1
        # while sum(math.ceil(train/speed) for train in dist[:-1]) + dist[-1]/speed > hour:
        #         speed += 1
        
        # Ok, so we know each time we want to slow down, we want to just got to the next slowest speed
        # try a set? Nope. Dumb. Try binary search?
    
        # while speeds:
        #     speed = speeds.pop()
        #     if sum(math.ceil(train/speed) for train in dist[:-1]) + dist[-1]/speed <= hour:
        #         lastSpeed = speed
        #     else:
        #         break

        L, R = 1,10000000
        ans = -1
        while L <= R:
            M = L + (R - L)//2
            if sum(math.ceil(train/M) for train in dist[:-1]) + dist[-1]/M <= hour:
                ans = M
                R = M - 1 
            else:
                L = M + 1 

        return ans