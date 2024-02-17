# 02-16-2024 Leetcode Daily 2662. Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
# Time: Like... 90 minutes Challenge: 7/10 Pretty quickly assumed it was a Dijkstra
# thing, but it was a lot to figure out and I psyched myself out on parts. 


# Interetsing. Obviously the first step is to get the straight manhattan distance.
# We can then look at what happens if we take special roads but... how?
# Consider a situations where the straight distance is a million steps to the right.
# Maybe there is a series of special roads that lead left with the following property:
# their start and ends have a single space between them, and they are all 10 spaces long, and cost 1.
# There are like 400,000 of these. The last road in the chain however travels directly to
# our target for a cost of 1. We take 400,000 steps THE WRONG WAY and end up 10x further from
# our starting point. We then get to the target instantly. Its a legitimate route, 
# we can't discount it.

# Without negative weights there can never be a benefit
# to taking the same route twice (these are ONE WAY right? The wording pretty much ensures this)
# We can start by deleting special roads that are more expensive than the straight distance they 
# cover. After this it seems like a straightforward graph problem right? Special roads are explicit
# edges, but EVERY special road start is a node. Every special road end is a node. There are implicit
# edges between every node and every other node, just the straight distance. 
# The end nodes are a little weird. We never really want to travel directly to them. We only happen to
# arrive at them if we took a special road.

# So its just a Dijkstras method problem right? Stack for shortest traveled so far. First one to the end wins?
# For each starting node we DO have to push the distance to ALL the other nodes though... That seems off. We also
# need to mark what roads have been taken. There are up to 200 roads. This could be a bit mask but 200 bit
# bitmasks seems a little much. 

# Im a little worried I'm missing the obvious. The above seems straightforward, but like memory is going to be
# a huge problem.

# Ugh, we cant even eliminate spcial roads that start out crazy far from the target. What if a DIFFERENT 
# special road takes us right to this start? Oh man, multiple special roads could all start from the same
# grid location too. Nothing is unique about them. Hell, there could be special roads that start AND end at
# the same spots with differing costs... or even the same. We COULD check and eliminate these, but thats getting
# into the ectreme weeds

# Ill try the dijkstra stack and see if it crashes and burns...

# AHA! I was just mixed up. You dont need a bitmask nor to track th history of each route. I'm conflating a 
# DFS/backtracking solution WITH dijkstras. BECAUSE we never want to revisit a start point for a special node,
# We will never want to revisit the ENDPOINT of that node, they are one in the same. If some early route gets
# us to endpoint [5,6], any later rout that ALSO ends here will necisarily have taken more steps. As such it will
# be permanantly behind in the count and forever able to catch up. We dont even push it. Also, as stated we never want
# to travel TO end points directly. It buys us nothing. Therefore the only way to get to a given endpoint is via a 
# start point, and by never visiting a start point twice, we can keep just a simple seen list. The SHORTEST path
# that is near a given special road will take it. No longer path benefits more from doing so later. Each path is
# used at most once. 

# Rather than keep a seen list, we can literally DELETE paths from our dicts, so we dont have to bother checking 
# if they are in seen. NOPE! This is wrong. We are checking ALL nodes from every curr_pos.
# Instead we can keep a dict of the cost to get to a particular start node. If it costs more get to a given start
# node from here, then someone else has taken that path earlier and we can ignore it. No deleting, no seen. We have
# to be able to check the availability of every node to every node. But now we can quickly discard useless paths.
# WHEW... Finally feel like I am getting somewhere

from heapq import heappush as hpush, heappop as hpop
from functools import cache

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        _start = tuple(start)
        _target = tuple(target)
        
        sp_roads = collections.defaultdict(list)
        
        # @cache
        def dist(a:tuple, b:tuple) -> int:
            return abs(a[0] - b[0]) + abs(a[1]-b[1])

        for sx, sy, ex, ey, cost in specialRoads:
            if dist((sx, sy), (ex, ey)) > cost:
                sp_roads[(sx, sy)].append([cost, (ex, ey)])

        cost_to_reach = {sp_start: 10**7 for sp_start in sp_roads}

        heap = [[0, _start]]
        while heap:
            curr_cost, curr_pos = hpop(heap)

            if curr_pos == _target:
                return curr_cost
        
            hpush(heap, [curr_cost + dist(curr_pos, _target), _target])

            for sp_start in sp_roads:
                dist_to_sp = dist(curr_pos, sp_start)
                if curr_cost + dist_to_sp < cost_to_reach[sp_start]:
                    cost_to_reach[sp_start] = curr_cost + dist_to_sp 
                    for sp_road in sp_roads[sp_start]:
                        sp_cost, sp_end = sp_road
                        hpush(heap, [curr_cost + dist_to_sp + sp_cost, sp_end])
        
        return -1
