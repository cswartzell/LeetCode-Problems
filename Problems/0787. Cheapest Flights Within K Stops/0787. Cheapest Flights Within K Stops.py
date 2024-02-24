# 02-23-2024 Leetcode Daily 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=daily-question&envId=2024-02-23
# Time: 28 mins Challenge 5/10



#If done iteratively instead of recursively we can stop searching when any
#flightpath exceeds the current minimum, as there are no negative cost flights
#Given that we are limited by a number of stops, it seems like BFS is a better
#strategy here. So, Itertive BFS it is

# Its just dijkstras

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        TOTAL, STOPS, CITY = 0, 1, 2
        adj_cities = collections.defaultdict(list)
        for frm, to, price in flights:
            adj_cities[frm].append((to, price))
        
        cheapest = [[10**9 + 7 for _ in range(k + 1)] for _ in range(n)]
        min_cost = 10**9 +7

        heap = [(0, 0, src)]
        while heap and heap[0][TOTAL] < min_cost:
            curr_total, curr_stops, curr_city = heapq.heappop(heap)
            for neighbor, price in adj_cities[curr_city]:
                if curr_total + price < cheapest[neighbor][curr_stops]:
                    cheapest[neighbor][curr_stops] = curr_total + price
                    if neighbor == dst:
                        min_cost = min(min_cost, curr_total + price)
                    elif curr_stops < k:                
                        heapq.heappush(heap, (curr_total + price, curr_stops + 1, neighbor))
                
        return min_cost if min_cost != 10**9 + 7 else -1

