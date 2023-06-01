# 05-31-2023 Leetcode 1396. Design Underground System
# https://leetcode.com/problems/design-underground-system/description/

class UndergroundSystem:

    def __init__(self):
        # Key: Id. Val: (startStation, TimeIn)
        self.checkedIn = collections.defaultdict(tuple)
        # Key: startStation Val: key:endStation->Val:(total times of rides, num rides) 
        self.avgTravel = collections.defaultdict(lambda: collections.defaultdict(lambda: [0,0]))   

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # If not already in, check in
        if id not in self.checkedIn:
            self.checkedIn[id] = (stationName, t)            

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #If checked in, get from where and when and remove from checked in
        if id in self.checkedIn:
            startStation = self.checkedIn[id][0]
            timeElapsed = t - self.checkedIn[id][1]
            del self.checkedIn[id]
            #If this is the first entry for the starting station or THIS end from the start station,  
            # set its only exit as the current endStation, and the time it took is the average

                    # REMEMBER: Declaring the type for a dict must be a callable, but we can use a lambda to set a called default val
                    # In this case we use lambda to call a new default dict as the first dicts value. Furthermore, we use a lambda
                    # to initialize a zeroed list of len 2 for the default val of the second dict

                    # if startStation not in self.avgTravel or stationName not in self.avgTravel[startStation]:
                    #     self.avgTravel[startStation][stationName] = [timeElapsed, 1]
                    # else:
            
            self.avgTravel[startStation][stationName][0] += timeElapsed # May overflow RAPIDLY if we are using Millis
            self.avgTravel[startStation][stationName][1] += 1
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avgTravel[startStation][endStation][0] / self.avgTravel[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)