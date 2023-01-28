# 01-28-2023 Leetcode 352. Data Stream as Disjoint Intervals
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/

# Ok, forget all that junk. I think we are going to have to recreate the intervals
# each time anyhow, simply because its too cumbersome to extend, merge, and delete
# intervals. Creating them from scratch each time is pretty trivial.
# Round 1: we'll simply create a bool list for seen numbers. When we want to
# generate the intervals, we just scan through THE ENTIRE list.
# A SUPER minor improvement could be to keep a "first num seen" and "last num seen"
# and only look at that range, expanding it as more nums are seen but that will
# probably make almost no difference.

# Round 2 would be to keep an ordereed set: pop left to get the head of the next interval
# then keep popping to either extend the interval, or find the head of the next. keep
# track of the current tail. This would be MUCH less iteration through the whole list,
# but at the expense of keeping and ordered set. Oh wait! We only need to sort it When
# looking for intervals. We can sloppily add to it when pushing new vals. Presumably this
# is less expensive than keeping it ordered as we go? Complex analysis would actually be
# needed to tell if that was true

# class SummaryRanges:

#     def __init__(self):
#         self.seen = [False] * 10001

#     def addNum(self, value: int) -> None:
#         self.seen[value] = True

#     def getIntervals(self) -> List[List[int]]:
#         peek_seen = self.seen
#         intervals = []
#         i = 0
#         while i < 10001:
#             curr_start, curr_end = None, None
#             while i < 10001 and self.seen[i] == False:
#                 i += 1
#             if i < 10001:
#                 curr_start = i
#             while  i < 10001 and self.seen[i] == True:
#                 i += 1
#             if i < 10001:
#                 curr_end = i - 1

#             if curr_start != None and curr_end != None:
#                 intervals.append([curr_start,curr_end])
#             i += 1

#         return intervals


# Bah! Still pretty bad in execution time. Whatever. It FEELS clever, and thats
# what is really important right? Honestly, it looks clever and includes Complex
# "advanced methods tm" which might help in an interview setting.

# BUT I GOD DAMNED DID A HARD ON MY OWN, AND ITS NOT COMPLETELY AWFUL


class SummaryRanges:
    def __init__(self):
        self.seen = set()
        self.seen_heap = []

    def addNum(self, value: int) -> None:
        if value not in self.seen:
            # keep as set to remove dupes, AND keep seen_list as a heap to reduce sorting cost
            self.seen.add(value)
            heapq.heappush(self.seen_heap, value)

    def getIntervals(self) -> List[List[int]]:
        # Ok... heap version, so no manual sorting each time
        new_seen_heap = copy.copy(self.seen_heap)
        intervals = []
        while new_seen_heap:
            curr_head = heapq.heappop(new_seen_heap)
            curr_tail = curr_head
            while new_seen_heap and new_seen_heap[0] == curr_tail + 1:
                curr_tail += 1
                heapq.heappop(new_seen_heap)
            intervals.append([curr_head, curr_tail])
        return intervals


# class SummaryRanges:

#     def __init__(self):
#         self.seen = set()
#         self.seen_list = []

#     def addNum(self, value: int) -> None:
#         if value not in self.seen:
#             self.seen.add(value)
#             self.seen_list.append(value)

#     def getIntervals(self) -> List[List[int]]:
#         #bit of a pain: We want to keep seen as a set to reduce duplicates
#         #but then we sort from scratch each time. IF seen was a list, then sorting
#         #it (using default timsort) WOULD be faster each time as it wouldnt need
#         #to start over. It uses merge sort so should be quick?
#         #I could also manually heapsort it
#         #This doubles the space required, but its a fixed 10001 max, so O(1)
#         self.seen_list.sort(reverse = True)
#         new_seen_list = copy.copy(self.seen_list)
#         intervals = []
#         while new_seen_list:
#             curr_head = new_seen_list.pop()
#             curr_tail = curr_head
#             while new_seen_list and new_seen_list[-1] == curr_tail + 1:
#                 curr_tail += 1
#                 new_seen_list.pop()
#             intervals.append([curr_head, curr_tail])
#         return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()


# Ok.... what about 2 DP arrays that function like disjoint union maps?
# There are only 1000 possible values, pretty small actually. We can easily
# store an INTERVAL_START dp array, and an INTERVAL_END dp array.
# As we add a new int i, we check INTERVAL_START[i-1], and set INTERVAL_START[i]
# to ITS head if it exists. Like a representetive member of a disjoint set.
# we do the same for INTERVAL_END.

# Ugh, that feels OK at best, but now to list the sets we havew to create the list
# from scratch each time... its better to somehow save this as actual INTERVAL_START
# We can keep a set of SEEN numbers to facilitate iterative lookups as we modify
# intervals I guess. new_int_start = seen[i-1]. while new_int_start, new_int_start -= 1
# Do the same for end? Wait... and still delete members of our array. Really, the array
# generation is the hard part.

# Here are the possiblities for a new int:
# Stands alone as part of a new intervals: add to list in order
# falls into a current interval and disappears: ignore
# extends an interval right or left WITHOUT touching a second interval: modify interval
# bridges two existing intervals, thus colapsing them into one. Delete 2 intervals, add new

# Im going to try the first method first. Yes, I have to generate the intervals from scratch
# on each call, but it seems like that will be quick

# class SummaryRanges:

#     def __init__(self):
#         self.interval_start = [-1]*10001
#         self.interval_end = [-1]*10001

#     def addNum(self, value: int) -> None:
#         def get_start(value):
#             prior_start = self.interval_start[min(0, value - 1)
#             #value before exists but is not the start of an interval
#             if prior_start != -1 and prior_start != value - 1:
#                 curr_head = get_start(value - 1)
#             elif prior_start == -1:
#                 return value:
#             elif prior_start == value - 1
#                 return prior_start
#             self.interval_start[value] = curr_head
#         get_start(value)

#         def get_end(value):
#             next_end = self.interval_end[max(10000, value + 1)
#             #value before exists but is not the start of an interval
#             if next_end != -1 and next_end != value + 1:
#                 curr_tail = get_start(value + 1)
#             elif next_end == -1:
#                 return value:
#             elif next_end == value + 1
#                 return next_end
#             self.interval_end[value] = curr_tail
#         get_end(value)

#     def getIntervals(self) -> List[List[int]]:
#         return [9,9]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
