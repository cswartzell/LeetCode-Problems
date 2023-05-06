from collections import defaultdict
from functools import cache

nums = [2, 2, 3, 3, 3, 4, 7]

points = defaultdict(int)
max_num = 0
for num in nums:
    points[num] += num
    max_num = max(max_num, num)


max_points = [0]*(max_num+1)
# max_points[0] = 0   #unnecessary as its taken care of BY the array declaration
max_points[1] = points[1]
for num in range (2, max_num+1):
    max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])    
print(max_points[max_num])


#FULLY FUNCTIONAL top down DP ripped directly out of the solutions page
#its hard to conceptualize whats going on with the recursive call and 
#you cant easily inspect the cache to watch it build. Try bottom up

# points = defaultdict(int)
# max_num = 0
# for num in nums:
#     points[num] += num
#     max_num = max(max_num, num)


# @cache  # this is a decorator, full of magic. stats a cache for a following function
# def max_points(num):
#     if num == 0:
#         return 0  # Zero base case, always worth zero points, can ignore result usually
#     if num == 1:
#         return points[1]  # Base case. If we get to 1, it has to be max
#     else:
#         return max(max_points(num - 1), max_points(num - 2) + points[num])

# print(max_points(max_num))












#Neat. This one is complicated as heck, and this very clever Greedy solution FAILS
# to choose optimal selections. It takes the biggest single point gain, not realizing
# the deletion consequences means it may lose out on better choices

# while nums_counter:
#     for x in nums_counter:
#         if x * nums_counter[x] >= (
#             (x - 1) * (nums_counter[x - 1]) + (x + 1) * (nums_counter[x + 1])
#         ):
#             points += x * nums_counter[x]
#             del nums_counter[x - 1]
#             del nums_counter[x + 1]
#             del nums_counter[x]
#             break
