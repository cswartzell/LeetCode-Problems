"""03-15-2022 LeetCode 1057. Campus Bikes"""
from collections import defaultdict
import heapq


workers = [[0, 0], [2, 1]]
bikes = [[1, 2], [3, 3]]


#The following is the optimal solution given, using a heap and some clever ordering:
# Still generates every worker/bike combination, but storing these in a heap makes
# picking them out in order faster


worker_to_bike_list = []
pq = []

for w, wl in enumerate(workers):
    curr_worker_pairs = []
    for b, bl in enumerate(bikes):
        curr_worker_pairs.append(((abs(wl[0] - bl[0]) + abs(wl[1] - bl[1])), w, b))

    # Sort the worker_to_bike_list for the current worker in reverse order
    curr_worker_pairs.sort(reverse=True)
    # Add the closest bike for this worker to the priority queue
    heapq.heappush(pq, curr_worker_pairs.pop())
    # Store the remaining options for the current worker in worker_to_bike_list
    worker_to_bike_list.append(curr_worker_pairs)

# Initialize all values to false, to signify no bikes have been taken
bike_status = [False] * len(bikes)
# Initialize all values to -1, to signify no worker has a bike
worker_status = [-1] * len(workers)

while pq:
    # Pop the worker-bike pair with smallest distance
    distance, worker, bike = heapq.heappop(pq)

    if not bike_status[bike]:
        # If the bike is free, assign the bike to the worker
        bike_status[bike] = True
        worker_status[worker] = bike
    else:
        # Otherwise, add the next closest bike for the current worker to the priority queue
        next_closest_bike = worker_to_bike_list[worker].pop()
        heapq.heappush(pq, next_closest_bike)

print("return worker_status")


# Damn! I was like 80% of the way there to using defaultdict to store w/b pairs by m_dist keys,
# it seemed complicated and I didnt get the benefit at the time. The reason its better is that
# you DONT need to sort: We are adding w/b pairs ALREADY in ascending order, only the m_dist changes
# but by storing these in a dict, then iterating over the keys in the dict, we dont need to resort:
# The m_dist is sorted naturally by iterating from min_m_dist through the rest of the dict, and each
# val per key was added in already sorted. I did try saving m_dists to their own list and iterating
# over just this, that way you dont bother checking w/b pairs for m_dists with no values. This served
# to slow things down rather than speed things up: Presumably the w/b pairs are in a pretty small
# tight order, and since m_dist is just an in dict check its very fast already. Seemed like making this
# added set took more time than it saved. If m_dists were siginificantly more dispersed this may be a beter
# choice overal. 
# Got the following to work

# taken_workers = set()
# taken_bikes = set()
# d_w_b = defaultdict(list)
# min_m_dist = 1998  # we know x, y <= 1000, 1000 so the largest distance is corner to corner 999 + 999
# wonb = [False]*len(workers)

# for w in range(len(workers)):
#     for b in range(len(bikes)):
#         m_dist = abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
#         min_m_dist = min(m_dist, min_m_dist)
#         d_w_b[m_dist].append((w, b))

# for i in range(min_m_dist, 1998):
#     for w, b in d_w_b[i]:
#         if w not in taken_workers and b not in taken_bikes:
#             wonb[w] = b
#             taken_workers.add(w)
#             taken_bikes.add(b)
#         if len(taken_workers) == len(workers):
#             break  # return wonb
#     i += 1

# print(str(wonb))


# WOW! I can't believe I did this one. I had more intermediate steps that I thought needed to
# be sorted each time, but it turns out .sort() automatically sorts multidimensional lists/tuples
# correctly, including column by column

# taken_workers = set()
# taken_bikes = set()
# d_w_b = []
# wonb = [False] * len(workers)

# for i in range(len(workers)):
#     for j in range(len(bikes)):
#         d_w_b.append([abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]),i, j])
# d_w_b.sort()

# for d,w,b in d_w_b:
#     if w not in taken_workers and b not in taken_bikes:
#         wonb[w] = b
#         taken_workers.add(w)
#         taken_bikes.add(b)
#     if len(taken_workers) == len(workers):
#         break

# print(str(wonb))
