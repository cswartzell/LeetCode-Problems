# 11-25-2022 LeetCode 907. Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/

# Huh. Took a while to just think on this one and I have three
# ideas, but I'm not sure any are better than the others:

# 1 Brute force: Just generate the subbarays, call min() on each
# and pass that all into sum(). Should be doable in one line.
# The number of elements in the list of all subarrays
# (the "Power Array"?) of length n is the nth triangular number,
# good ole (n*(n+1))/2. In this case, n can be up to 3000. That
# could mean a subarray set of of 450,015,000 elements, each of
# which could be an int of up to 30,000. The sum could be as
# high as 13,500,450,000,000, significantly over our cap 10^9 + 7
# Calling min on 450 million sets seems... problematic.

# A min heap? We could generate the first subarray for each size,
# then sort of sliding window across the base array for that size:
# add the next element to the min heap, pop the element thats leaving
# and return the first element of the min heap. Certainly faster, but
# how much so? Adding a node to a minheap is O(1) somehow, awseome. Seems
# like it ought to be the height of the heap. Oh, it is. O(logn) to heapify
# Similarly, surely accessing the min element is also O(1). Lastly, its
# also O(log n) to delete an element. This seems like a pretty good option.

# But can we do better? We literally only care about the minimum value
# of a subarray, and can kind of ignore the rest. Can this be a plain
# sliding window solution? Again, we find the min value for the first
# subarray of size X for each X in N. Save this as curr_min.
# slide the window making only two comparisons: first, was the value
# that just left equal to or less than curr_min? If so, we may have just
# lost our min. We cant be certain though, as another copy of it may be
# within the window. We'll need to check. Call min() on the window to
# find the new curr_min. This is the only condition that will cause us
# to call min() on the set, and as min() is costly (O(n)), eliminating
# these checks significant. Note calling min() here will
# INCLUDE checking the new added number, so we are done with this window.
# If the leaving numbner is not equal to or less than min, we can instead
# only bother with the new number. If it is LESS than min(), update min.
# Lastly, add curr_min to our total.

# As subbarrays, we do have to process them
# in order. There doesnt seem to be a better way to generate the subarrays
# other than 2 for loops


# Well ok then. The solution MUST be done in O(n) time, but doesnt say it.
# The presented answer relies on a "Monotonic Stack", a concept that is
# Strictly foreign to me. Its pretty simple and clever, but I absolutely
# would not have been able to come up with it on my own.

# For each i in the array, sort of look forward and backward to find how
# long a slice the ith element WOULD be the smallest element for. This can
# be done using a very tricky stack operation. We need to be careful and
# EXCLUDE equal values to arr[i] on one side (the left here, but I think either?)
# and INCLUDE them on the other. We then can use another funky math trick
# to note how many subarrays there are of this slice (note, its NOT the nth
# triangular number, as that includes slices that DONT include the ith element)
# We can thus get the "contribution" of the ith element as smallest ele in
# its sorrounding subarrays.

# This is CLEARLY pretty tricky business.

# armed with this, Im going to try again coding it explicitly using the
# plain discription of the algorithm while not directly copying the code.


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sub_min_total = 0

        mono_stack = []
        for i in range(len(arr) + 1):
            while mono_stack and (i == len(arr) or arr[mono_stack[-1]] >= arr[i]):
                popped = mono_stack.pop()
                left = -1 if not mono_stack else mono_stack[-1]
                sub_min_total += (popped - left) * (i - popped) * arr[popped]
            mono_stack.append(i)
        return sub_min_total % (10**9 + 7)


# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         sub_min_total = 0

#         #Brute force dummy method
#         # # power_array = []
#         # for i in range(1,len(arr) + 1):
#         #     for j in range(len(arr) - i + 1):
#         #         sub_min_total += min(arr[j:j+i])
#         #         # power_array.append(min(arr[j:j+i]))

#         #brute force one line? Shocking, TLE. Still, fun to try. Incomprehensible as is
#         # return sum([min(arr[j:j+i]) for i in range(1,len(arr) + 1) for j in range(len(arr) - i + 1)])


#         #Oh, come on! I thought this was a good solution. Damnit. TLE, Really?!
#         for n in range(1,len(arr) + 1):
#             #min for sliding window of len n starting position
#             curr_min = min(arr[0:n])
#             sub_min_total += curr_min
#             for j in range(1, len(arr) - n + 1):
#                 #is the number leaving us old min? If so, finde new min in window
#                 if arr[j-1] <= curr_min:
#                     curr_min = min(arr[j:j + n])
#                 #Otherwise we've held on to old min. Is new num min?
#                 else:
#                     curr_min = min(curr_min, arr[n+j-1])
#                 sub_min_total += curr_min

#         #are we cheating by only modding here? Using unlimited ints
#         #above to cut down on operations. Dont know if thats actually
#         #faster, there may be a penalty for using very large ints

#         #The exponent operator is NOT ^ !!! Thats XOR
#         # return sub_min_total % (10^9 + 7)
#         return sub_min_total % (10**9 + 7)
