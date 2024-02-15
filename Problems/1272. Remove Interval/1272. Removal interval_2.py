# 02-14-2024 Leetcode weekly 1272. Removal interval
# https://leetcode.com/problems/remove-interval/?envType=weekly-question&envId=2024-02-15
# Time: 25 Challenge: 4/10


# Sort intervals FIRST by starting of the interval.
# If need be, we might binary search to find the spot where we 
# first need to start editing. That seems like a step too far for now.
# Can add it in if neccessary. For now, an O(n) pass seems fine

# Cases:
# End of curr_int < removed_start: Interval is too early, skip
# Start of curr_int > removed end: Interval too late, we are done. Return

# SOME OVERLAP
# End of curr_int > removed_start: 
    # if Start of curr_int < removed_start: curr_int starts BEFORE the removal, but runs into it:
    #     curr_int_start = removed_start. Technically there can only be one of these Cases
    #     as the intervals are disjoint. No need to check though

    # if Start curr_int > removed_start and End curr_int < removed_end: 
    # This interval is entirely in the removed selection. Delete it.breakpoint

    # if Start curr_int < removed_end and End curr_int > removed_end: 
    # This interval starts in the middle of the removed section, but overruns it.
    # curr_interval_start = removed_end. RETURN here 

    # if curr_int_start < removed_start AND curr_int_end > removed_end:
    # curr_int more than spans the entire removed section. We need to break it 
    # into two sections. We can return here as we are beyond the end of removed. 

    # NOTE: carefully mind when we use < or <= 
    # NOTE: My first attempt modified the len of the arry LIVE. This may be dumb.
    # As we are using a while loop, and just checking indexing does this break as the
    # len changes as we go? Or does the while recheck the condition at the top each time? 
    # DONT EDIT THE INPUT. just build an ans array dummy

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        START = 0
        END = 1

        ans = []
        for idx in range(len(intervals)):
            if intervals[idx][END] <= toBeRemoved[START]:
                ans.append(intervals[idx])
                continue
            elif intervals[idx][START] >= toBeRemoved[END]:
                ans += intervals[idx:]
                break
            elif intervals[idx][START] < toBeRemoved[START]:
                ans.append([intervals[idx][START], toBeRemoved[START]])
                if intervals[idx][END] > toBeRemoved[END]:
                    ans.append([toBeRemoved[END], intervals[idx][END]])
            elif intervals[idx][END] > toBeRemoved[END]:
                    ans.append([toBeRemoved[END], intervals[idx][END]])
            # implicit SKIP if interval[idx][START] >= removed[START] and interval[idx][END] <= removed[END]
            # These intervals are small and lie entirely in removed. Ignore them 

        return ans
