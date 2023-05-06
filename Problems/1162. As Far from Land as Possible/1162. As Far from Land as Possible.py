
#n can be up to 100, so this can be quite large. Efficiency is key

#jeez, I dont konow. Flood fill comes to mind, but like... from EVERY
#land point? That seems like a disaster. 

#okay.. what if we BFS Flood fill using a dequeue. That way we prune as early
#as possible? I Kinda wish land wasnt marked as 1, but rather a different char
#We COULD edit that as we do the first pass to find all the land sections: shore
#water IS 1 step away from land... which is marked as one. We could just used
#negative numbers for water distance I guess



class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        floodsea = collections.deque()
        point_nemo = 0

        for row in range(len(grid)):
            for col in range(len(row)):
                if grid[row][col] == 1:
                    floodsea.append([row,grid])
                    grid[row][grid] = 100

        while floodsea:
            curr = floodsea.popleft()
            for direction in ()