# 03-31-2024 Leetcode 2702. Minimum Operations to Make Numbers Non-positive
# https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/description/
# Time: 60 mins Challenge: 8/10

# If X is larger than Y then we want to apply x to the LARGEST
# current value, and Y to all the rest. Repeat. However is X is smaller
# than Y then we need to X to the current SMALLEST number and Y to the rest

# In either case we can actually imagine we are performing Y to all nums, and just
# adjusting the highest or lowest number by the difference in X-Y based on the above.
# This may mean we dont acutally have to to ANY of the Y adjustments. Just collect them
# as phantom delta we have done so far. 

# In the case where X is larger, we repeat this using a heap til the top of the 
# heap - delta < 0: clearly we have done enough ops such that the largest number
# is now zero or less, then all the rest must be. We just use a max heap.

# How do we do this for the other direction? I suspect negation. If we use a min heap
# we COULD pop off numbers once they hit < 0 and keep repeating til nums is empty. Its 
# not bad: we still use a phantom delta that means we dont have to do all the subtractions.
# but we do have to process the whole list unlike the above. I'm curious if htere is better solution:
# we need to do the X operation to the smallest num and collect DELTA_Y but we need to know if the 
# MAX element is <= DELATA_Y. A heap cant keep track of smallest and largest. 

# Oh god damnit, the constraints say X is explicitly larger than Y, but the problem doesnt. 

# Ok. it works but TLE. We are only adjusting the ONE element each time, but I guess we are just doing
# a simple addition FOR every operaion: if we start with [100, 1000000000] and X = 2 then thats a LOT of
# addition to do before we actualy start flip floping which we are reducing. Instead we can pop the 
# smallest and then compare it to the NEXT smallest (now at the top of the heap) and the number of 
# added ops is the ceiling of the difference of these two/x.  This eliminates what... like the 
# First an only big diff. Then the largest two are neck and neck just changing by one each time 
# maybe until they push down to the third; then these 3 take single op turns til we collect all?
# Is this actually better? Is there like a logn operation im missing?

# Maybe we dont need to start delta_y at 0? 
# I see one of the test cases has THOUSANDS of the same large number. If repeats are common maybe
# we could collect the values into a counter so we can do more ops at once: if the largest val in
# nums is 80, and there are 500 copies of 80, then the next 500 ops are clearly going to be reducing
# each of these 80's by x. We could do them ALL in one go? This at least seems more plausible as
# we are REDUCING the space, but retatining the same length so we are going to be adding more and
# more collisions as we go. If we have millions of values and an x of like 2, then when we get down 
# to where all the nums are in the 20s then they will all massively overlap. I like this better than
# the dumb "comapre the next". Now our heap is just the VALUES, not copies, and the heap itself actually
# shrinks as we go. 

class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        # ADDING EVERYTIME TOO SLOW:

        # if len(nums) == 1:
        #     return math.ceil(nums[0]/x)        

        # # DONT alter the input. Also, need a max heap
        # heap = [-num for num in nums]
        # heapq.heapify(heap)

        # delta_x = x - y
        # operations = 0
        # while heap[0] + operations * y < 0:
        #     heapq.heapreplace(heap, heap[0] + delta_x)
        #     operations += 1

        # return operations


        if len(nums) == 1:
            return math.ceil(nums[0]/x)        

        count = collections.Counter(nums)
        heap = [-num for num in count.keys()]
        heapq.heapify(heap)

        delta_x = x - y
        operations = 0
        while heap[0] + operations * y < 0:
            largest = heapq.heappop(heap)
            largest_count = count[largest] 
            operations += largest_count
            del count[largest]
            del_largest = largest + delta_x
            if del_largest not in count:
                heapq.heappush(heap, del_largest)
            count[del_largest] += largest_count

        return operations

