#There are 6 cases per interval: 
# BEFORE: interval is entirely BEFORE removed section
# MID-START: START of removed section is somwhere in the middle, extends beyond end of curr interval
# CONTAINED: ENTIRE removed section is within interval
# SUBSUMED: Entire interval is within removed section
# MID-END: End of removed section is somewhere in the interval, terminates before end of curr interval
# AFTER: interval is entirely AFTER removed section

#All are relations on the start/end of the interval in question and the removed section
# BEFORE, MID-START, CONTAINED all have an interval start ahead of REMOVED
# MID-END, AFTER have interval ends beyond the end of REMOVED
# SUBSUMED is the only case with an interval start after REMOVED start AND interval end before REMOVED end

#BEFORE: Leave untouched

#MID-START: Change interval end to REMOVED start -1 [Interval start, REMOVED start -1]
#CONTAINED: Break into two intervals: [Interval start, REMOVED start -1]. [REOMVED end +1, INTERVAL end]
#After either of these operations, we can simply concat the remainder of the list without checking

#SUBSUMED: Ignore
#MID-EMD: Change INTERVAL start to REMOVED + 1
#AFTER: Add without altering: May be done by above operations. If not, add this and all following
#No need to continue to check following. 

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        #can hardcode these to micro-optimize memory
        start = 0
        end = 1
        
        
        #DOUBLE CHEKC ALL < vs <=: replace Intervals[curr][start]
        
        
        #intervals is a list, which is costly to remove elements from. We could instead build
        #a new answer list from scartch at the cost of additional memory of course. 
        for curr in len(intervals):
            if intervals[curr][start] < toBeRemoved[start]:
                #BEFORE: Ignore
                if intervals[curr][end] < toBeRemoved[start]:
                    continue
                #CONTAINED:
                if toBeRemoved[end] <= intervals[curr][end]:
                    pass
                    # return intervals[:curr] + [intervals[curr][start], toBeRemoved[start]] + [toBeRemoved[end] + 1, intervals[curr][end]] + intervals[curr + 1:]
                #MID-START: Remove the latter half of the curr interval
                if intervals[curr][end] >= toBeRemoved[start]:
                    intervals[curr][end] = toBeRemoved[start] - 1
            #SUBSUMED: Remove interval
            if intervals[curr][end] <= toBeRemoved[end]:
                intervals = intervals[:curr] + intervals[curr + 1:]
            #MID-END: 
            if toBeRemoved[end] > intervals[curr][end]:
                intervals[curr][start] = toBeRemoved[end + 1]
            #AFTER: 
            else:
                return intervals
