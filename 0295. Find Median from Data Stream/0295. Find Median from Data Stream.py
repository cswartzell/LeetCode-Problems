# 11-12-2022 Leetcode 0295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/description/

# First instinct is just to use a minheap to keep it sorted
# and use DFS to return a sorted list each time
# we need to find the median. I dont think
# we can do much better than minheap for organizing...


# Hmm. Python docs even say for "large N" it is faster to just use
# sorted() to return the list of n largest or smallest elements. In
# our case we'll want all of them. Is that different?
# From stackoverflow: " it's impossible to print sorted sequence out of
# the heap faster than O(nlogn), because it'd mean it's possible to sort
# any sequence faster than O(nlogn)". As I expected.

# Ugh, we could go for a doubly linked list build and just traverse and
# insert. Insertions are much cheaper than reordering. For some reason I find
# myself always annoyed by linked lists. n insertions could be O(n^2) though right?

# ok... what about this. Two pointers, either spliting center or pointing
# to the center index of a deque. When we push a value we compare it to
# the two pointers. If smaller than both, appendleft. If smaller than left
# BUT NOT RIGHT, appendleft and sort just the left half. If larger than
# left BUT NOT RIGHT appendright and sort the right half. If larger than both
# arbitrarily append right. We only resort when we need to? No, it might go
# JUST left or right, and adding it shifts the window to include it. Bust.

# Ok. Heaps are out. They are great for inputting and mainting a min or
# max, but not an entire order. Its the same big o to sort them as if
# they werent mostly sorted in the first place. My brain next goes to
# "insertion sort? Thats a thing right? What was that thing". Beyond the
# name I barely remember. As a guess, its a DS that keeps a sorted list...
# Hey, thats what we want here. Off to research.

# https://www.geeksforgeeks.org/insertion-sort/
# Ok, inesertion sort is pretty basic. Just above bubble sort
# and the same principal, but as its sorting TO a sorted array
# it can stop once it finds the correct position, knowing its right
# without haveing to compare every element.

# Straioghtforward and easy to implement. Aaaaaand it doesnt work.
# TLE still. What the heck. Ok, we can improve this. We need to keep
# track of middle points anyway. Theres no reason to insert the new
# num at the FAR RIGHT and then insertionsort check all remaining vals
# Why not USE the known vals of the middle to speed up insertion?
# Is this a common technique? You could keep a couple of pointers
# and start insertion sort closer to its expected position. Three
# pointers would cut the list into quareters so youd only need to
# search 25% of the space to do an insertion, for the cost of a few
# extra ifs? Wait, I've just reinvented binary search.

# so the article is wrong? It says it uses insertion sort, then instead
# uses binary search to locate the intended potion, then shifts the right
# array over to insert the new num. Thats not insertion sort, thats just
# an insertion? I guess its *kind of* an insertion sort as its using the
# fact that the array is already sorted, but the way articles teach insertion
# sort is a linear scan through the unsorted portion...


# Follow up answers: If the numbers are strictly 1-100 we can just use a 2d
# list to store answers in buckets of their index. Or rather, the index could
# simply contain the number of times we've seen that value. We keep track of the
# number of elements pushed so far. When we call for median we just sequentially
# sum our buckets until we either exceed the median index mid-bucket, or need to
# split sum beteen two buckets for a pair of even numbered median indexes.

# For the follow up follow up, we do the same, but buckets [0] and [101] contain
# sorted lists of pushed values that exceed 1-100. We dont need to keep them sorted
# UNLESS the median is to be found within eitehr extreme bucket. At that point we will
# need to sort them and find the correct index within, summing two pairs if necessary.
# This may be ever so slightly complicated by a split median spanning [0]-[1] of [100]-[101]

# import heapq

# class MedianFinder:

#     def __init__(self):
#         self.num_list = []

#     def addNum(self, num: int) -> None:
#         #Idea 1: Heap? No good. O(nlogn) sorting
#         # heapq.heappush(self.heapy, num)

#         #Idea 2: Insertion sort? TLE still. Takes too long to search
#         #and shift entire space to add new nums once n is large
#         # self.num_list.append(num)
#         # j = len(self.num_list) - 2
#         # while j >= 0 and num < self.num_list[j] :
#         #         self.num_list[j + 1] = self.num_list[j]
#         #         j -= 1
#         # self.num_list[j + 1] = num

#         #idea 3: Binary search to find intended position, use concatentation
#         #of slices to reorder new list


#         #IDEA 4 AFTER THE FACT! TWO HEAPS!
#         #A min heap AND a max heap.
#         #The median would ALWAYS be the tops of the heap!
#         #If its larger than the top of the minHeap (right),
#         #heapPush to the right. If smaller than the top of
#         #the maxHeap (left) HeapPush Left. We can simply keep
#         #a seperate tracker, or sum the lengths of either to know
#         #if there are an odd or even number of elements. If even, its
#         #the mean of the top two heaps. If Odd we have two choices:
#         #Either push a copy of each new num to BOTH heaps (thus both
#         #tops would have the same number) and always just use the mean,
#         #making sure to pop off the duplicate when adding the NEXT number
#         #to the same heap. OR we could track seperately how many nums are
#         #in each pile and just grab the top of the larger pile. Oh wait...
#         #this requires the piles to always have the same size. We need to rebalance
#         #as we go.

#         #ok, lets just have an overflow "middle" variable, that holds the odd man out
#         #when we have an odd number of elements in our combined heaps. This way the
#         #heaps are always even numbered. IFF there is a middle value, and we are adding
#         #a new number to one heap, push the middle value to the other, emptying the middle
#         #value. If there ISNT a middle value, first pop the first element of the heap we are
#         #GOING to put the new value into, and store the popped value in the middle.


#         # local_inspect = self.num_list
#         l, r = 0, len(self.num_list)
#         while l < r:
#             m = (l + r) // 2
#             if self.num_list[m] < num:
#                 l = m + 1
#             else:
#                 r = m

#         #G'damn the time limit must be tight. Concatenating slices like this takes too long
#         #Where the insert fuction squeaks by. Interesting to note insert is faster
#         # self.num_list = self.num_list[:l] + [num] + self.num_list[l:]
#         self.num_list.insert(l, num)

#     def findMedian(self) -> float:
#         #As expected, simple converting to list doesnt sort. Is there a point in storing as a heap then?
#         # local_inspect = self.num_list
#         left = self.num_list[(len(self.num_list)-1)//2]/2
#         right = self.num_list[math.ceil((len(self.num_list)-1)/2)]/2
#         sumlr = left + right
#         return sumlr

# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()


######################### ATTEMPT 2: 2 Heaps #################################################
# HECK YEAH!
import heapq


class MedianFinder:
    def __init__(self):
        self.minHeap = []
        # NOTE: THERE IS NO MAXHEAP! This is just a minheap, but you negate all the values first.
        # AND LATER when pulling them back out. Simple, but obnoxious. Would love if theyd just
        # duplicate it, but I guess "tHaTS nOT pYthOnIC!"
        self.maxHeap = []
        self.middle = None

    def addNum(self, num: int) -> None:
        left, right, mid = self.maxHeap, self.minHeap, self.middle

        # initial two pushes
        if not self.maxHeap and not self.minHeap:
            # first push will be middle
            if self.middle == None:
                self.middle = num
            # seocnd push is going somewhere
            else:
                if num >= self.middle:
                    heapq.heappush(self.minHeap, num)
                    heapq.heappush(self.maxHeap, -self.middle)
                else:
                    heapq.heappush(self.maxHeap, -num)
                    heapq.heappush(self.minHeap, self.middle)
                self.middle = None
            return

        # SPECIAL CASE: If there is a middle, and the num num is the same as the middle, this
        # moves the middle into one pile, and the new num into the other. Doesnt matter
        # which goes where as they are the same number.
        # Otherwise, move the middle into the appropriate heap and the new num to the other
        if self.middle != None:
            if num >= self.middle:
                heapq.heappush(self.maxHeap, -self.middle)
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.minHeap, self.middle)
                heapq.heappush(self.maxHeap, -num)
            self.middle = None
            return

        # if there is no middle, and this new num should be it, do so
        if self.middle == None and num >= -self.maxHeap[0] and num <= self.minHeap[0]:
            self.middle = num

        # num is equal or larger than the min on the right, dump in right, popping a new middle
        elif self.minHeap and num >= self.minHeap[0]:
            self.middle = heapq.heapreplace(self.minHeap, num)

        # num is equal or smaller than the max on the left, dump in left, popping a new middle
        else:
            self.middle = -heapq.heapreplace(self.maxHeap, -num)

    def findMedian(self) -> float:
        return (
            self.middle
            if self.middle != None
            else (self.minHeap[0] - self.maxHeap[0]) / 2
        )
