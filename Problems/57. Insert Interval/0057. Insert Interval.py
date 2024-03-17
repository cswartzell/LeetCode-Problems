03-16-2024 Leetcode 57. Insert Interval
    # Yes, I could binary seasrch EITHER half of this problem. Perhaps we'll do that next. 



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]

        START, END = 0, 1
        new_intervals = []
        for idx, interval in enumerate(intervals):
            if interval[START] <= newInterval[START]:
                new_intervals.append(interval)
            else:
                break
        #Now new_inntervals[-1] is the very previous one to what we are adding. 
        # It may have started earlier or even at the same time as the new event.
        # It may run THROUGH the new event, such that we have to combine them,
        # (this includes ending AT exactly the start time of the new one), or it
        # may have ended prior to the start of the new one. In the later case, move on.
        # Otherwise, combine.

        if new_intervals[-1][END] >= newInterval[START]:
            new_intervals[-1][END] = max(new_intervals[-1][END], newInterval[END])
        else:
            new_intervals.append(newInterval)

        # Weve now dealt with the start time. Either we've combined the previous interval
        # and the new one to be a longer interval, or we've merely added the new interval. 
        # In either case, NOW new_intervals[-1] has the correcct start time, but its end time
        # may over run one OR MORE additional intervals. idx is still valid, so we can continue
        # to search the intervals array from there

        while idx < len(intervals):
            if new_intervals[-1][END] >= intervals[idx][START] and new_intervals[-1][END] <= intervals[idx][END]:
                new_intervals[-1][END] = intervals[idx][END]
                idx += 1
                break
            elif new_intervals[-1][END] < interval[START]:
                break
            idx += 1
        if idx <= len(intervals) - 1:
            new_intervals += intervals[idx:]
        return new_intervals









#lets begin by finding the start of our inserted interval. There are two possibilities:
# the start of our new interval occurs between existing intervals, or it occurs as part
# of a single existing interval. 

#We begin by iterating intervals. If the end of the current interval is SMALLER than the start
#of new_interval, we just add that whole interval to our new list, it is irrelevant as it occurs
#prior to the new list. 

#Eventually we will find either an existing interval that ends before our new one, or wwe have 
#discovered our new interval occurs after all existing, so just add it. 
# Assuming its NOT a new end, then we have 








#There is the moronic version, were we simply add all the numbers in all intervals, including our 
# new one, then iterate through them generating a new interval list. 

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         #Base Case: Our new interval is entirely before or after existing intervals
#         if newInterval[1] < intervals[0][0]:
#             return [newInterval] + intervals
#         if newInterval[0] < intervals[-1][1]:
#             return intervals + [newInterval]

#         new_intervals = []
        
#         starts_after_i = 0
#         for i in range(len(intervals)):
#             if newInterval[0] > intervals[i][1]:
#                 i += 1
#                 new_intervals.append(intervals[i])
#             else:
#                 break
