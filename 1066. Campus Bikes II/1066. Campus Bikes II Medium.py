#12-15-2022 Leetcode 1066. Campus Bikes II
#https://leetcode.com/problems/campus-bikes-ii/description/

#Can be done recursively, but that call stack... You DO need to calculate
#ongoing choices for every combination of every bike and worker. 
#There is NO WAY id be able to pull this off in an interview setting. 
#Particularly not Djikstras method, and properly implementing the masking
#situation. We use the number of set bits in the taken bikes mask to 
#be the index of the next worker to be assigned? Absolutely wild. 
#ABSURD that this is considered a medium difficulty problem




#I think this can be solved by iterating a 2d DP array like the Solution#
#for https://leetcode.com/problems/longest-common-subsequence/description/
#We will build a grid for distance from each bike to each worker. 

#If I were to do this on paper it would be like so: Create a 2d grid of
#bikes x workers, where the intersection is the manhattan distances.
#we know we need to make WORKER correct selections from these WORKER X bikes
#choices, meaning we can cross out (WORKER X BIKES) - WORKERS. We can cross them
#out by setting them to zero. The remaining numbers will sum to be our minimum
#How to cross them out? Cross out the largest number IN THE WHOLE GRID but only 
#if its not the last bike for a given worker?
 
import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def mh_dist ( worker, bike ) -> int:
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])


        def count_ones(mask) -> int:
            count = 0
            while mask != 0:
                mask &= (mask-1)
                count += 1
            return count

        num_bikes, num_workers = len(bikes), len(workers)
        
        priorityQueue = []
        visited = set()

        #PYTHON DOES NOT HAVE HEAP AS A TYPE: instead you use heap methods to maintain
        #a plain list AS a heap. 
        heapq.heappush(priorityQueue, (0,0))
        while priorityQueue:
            curr_dist_sum = priorityQueue[0][0]
            curr_mask = priorityQueue[0][1]
            heapq.heappop(priorityQueue)

            if curr_mask in visited:
                continue
            
            visited.add(curr_mask)
            
            worker_i = count_ones(curr_mask)

            if worker_i == num_workers:
                return curr_dist_sum

            for bike_i in range(num_bikes):
                if (curr_mask & (1 << bike_i) == 0):
                    next_dist_sum = curr_dist_sum + mh_dist(workers[worker_i], bikes[bike_i])

                    next_mask = curr_mask | (1 << bike_i)
                    heapq.heappush( priorityQueue, (next_dist_sum, next_mask))



                    

#     public int assignBikes(int[][] workers, int[][] bikes) {
#         int numOfBikes = bikes.length, numOfWorkers = workers.length;
        
#         PriorityQueue<int[]> priorityQueue = new PriorityQueue<>((a, b) -> a[0] - b[0]);
#         Set<Integer> visited = new HashSet<>();

#         // Initially both distance sum and mask is 0
#         priorityQueue.add(new int[]{0, 0});
#         while (!priorityQueue.isEmpty()) {
#             int currentDistanceSum = priorityQueue.peek()[0];
#             int currentMask = priorityQueue.peek()[1];
#             priorityQueue.remove();
            
#             // Continue if the mask is already traversed
#             if (visited.contains(currentMask))
#                 continue;
            
#             // Marking the mask as visited
#             visited.add(currentMask);
#             // Next Worker index would be equal to the number of 1's in currentMask
#             int workerIndex = countNumOfOnes(currentMask);
            
#             // Return the current distance sum if all workers are covered
#             if (workerIndex == numOfWorkers) {
#                 return currentDistanceSum;
#             }

#             for (int bikeIndex = 0; bikeIndex < numOfBikes; bikeIndex++) {
#                 // Checking if the bike at bikeIndex has been assigned or not
#                 if ((currentMask & (1 << bikeIndex)) == 0) {
#                     int nextStateDistanceSum = currentDistanceSum + 
#                         findDistance(workers[workerIndex], bikes[bikeIndex]);
                    
#                     // Put the next state pair into the priority queue
#                     int nextStateMask = currentMask | (1 << bikeIndex);
#                     priorityQueue.add(new int[]{nextStateDistanceSum, nextStateMask});
#                 }
#             }
#         }
        
#         // This statement will never be executed provided there is at least one bike per worker
#         return -1;
#     }
# }