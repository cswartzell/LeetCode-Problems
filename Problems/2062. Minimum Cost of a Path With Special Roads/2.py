

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        idx = 0
        while idx < len(heights) - 1:
            # Drop: 
            if heights[idx + 1] <= heights[idx]:
                idx += 1
                continue
            d = heights[idx + 1] - heights[idx]
            # Out of ladders, get one using least bricks IF least bricks
            # is less than current d. Otherwise, just use bricks for d
            if ladders == 0 and heap and d > heap[0]:
                bricks -= heapq.heappop(heap)
                ladders += 1
            # Got a ladder without overspending bricks. Use it
            if ladders and bricks >= 0:
                ladders -= 1
                heapq.heappush(heap, d) 
            # No ladders, yet we have bricks leftover          
            elif bricks >= d:
                bricks -= d
            # No ladders or bricks enough
            else:
                return idx
            idx += 1
        return idx




# heap = []
#         idx = 0
#         while idx < len(heights) - 1:
#             # Drop: 
#             if heights[idx + 1] <= heights[idx]:
#                 idx += 1
#                 continue
#             d = heights[idx + 1] - heights[idx]
#             # Not Enough bricks
#             while d >= bricks and ladders and heap:
#                 bricks -= heapq.heappop(heap)
#                 ladders -= 1
#             if d <= bricks:
#                 bricks -= d
#                 heapq.heappush(heap, -d)
#             else:
#                 return idx

#             idx += 1
#         return idx




# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         brick_piers = []
       
#         for i in range(len(heights)-1):
#             if heights[i + 1] <= heights[i]:
#                 continue
            
#             bricks_needed = heights[i + 1] -  heights[i]
            
#             while bricks_needed > bricks and bricks_needed < -brick_piers[0] and brick_piers != [] and ladders:
#                 bricks -= heapq.heappop(brick_piers) #Stupid negated max_heaps...
#                 ladders -= 1
#             if bricks_needed <= bricks:
#                 heapq.heappush(brick_piers, -bricks_needed)
#                 bricks -= bricks_needed    
#             elif ladders:
#                 ladders -= 1
#             else: 
#                 return i
        
#         return len(heights)
