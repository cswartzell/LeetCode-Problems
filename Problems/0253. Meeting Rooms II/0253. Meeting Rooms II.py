# 07-19-2023 Leetcode 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/description/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int: 
        # intervals.sort()
        # heap = []
        # ans = 0
        # for interval in intervals:
        #     while heap and heap[0] <= interval[0]:
        #         heapq.heappop(heap)
        #     heapq.heappush(heap, interval[1])
        #     ans = max(ans, len(heap))

        # return ans
        intervals.sort()
        heap = []
        ans = 0
        for interval in intervals:
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            ans = max(ans, len(heap))

        return ans
 