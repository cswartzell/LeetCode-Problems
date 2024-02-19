# 02-18-2024 LEETCODE DAILY 2402. Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/?envType=daily-question&envId=2024-02-18
# Time: 30m Challenge: weirdly 3/10
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:       
        M_START, M_END, R_END, ROOM = 0, 1, 0, 1
        open_rooms = [*range(n)]
        # heapq.heapify(open_rooms)
        # Tuple- (time when released, room number)
        in_use = []
        room_count = [0] * n
        remaining_meetings = sorted(meetings)
        curr_time = -1
        
        max_use = -1
        max_room = None

        # next_meeting = 0
        for meeting in remaining_meetings:
            # Time DEFINITILY moves to at least the start of the next meeting
            curr_time = max(curr_time, meeting[M_START])
            # If there are no free rooms now, and none released on moving time to 
            # the current meeting, move it to the next release time. 
            if open_rooms == [] and in_use[0][R_END] > curr_time:
                curr_time = in_use[0][R_END]
            while in_use != [] and in_use[0][R_END] <= curr_time:
                heapq.heappush(open_rooms, heapq.heappop(in_use)[ROOM])
            selected_room = heapq.heappop(open_rooms)
            room_count[selected_room] += 1
           
            delay = curr_time - meeting[M_START]
            heapq.heappush(in_use, (meeting[M_END] + delay, selected_room))

        for room, count in enumerate(room_count):
            if count > max_use:
                max_room = room
                max_use = count

        return max_room