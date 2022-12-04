# 12-3-2022 2256. Minimum Average Difference
# https://leetcode.com/problems/minimum-average-difference/

# Ooh, whats that Data Structure that does this? Its a tree Structure
# that also keeps information like a running sum? Fenwick Tree!
# Actually LESS effecient than just summing it ourselves once here
# as we are given a fixed arrany and do not need the ability to update it
# dynamically. O(log n) to get sum where we can just do it O(n) to start
# (both) have this requirement, then just O(1) for lookup

# Still, shall we give it a go for practice? It is a
# slightly more complicated DS and I've seen it come up before


class ftree:
    # Constructs and returns a Binary Indexed Tree for given
    # array of size n.
    def __init__(self, arr, n):
        # Create and initialize BITree[] as 0
        self.BITTree = [0] * (n + 1)
        # Store the actual values in BITree[] using update()
        for i in range(n):
            self.updatebit(n, i, arr[i])
        # return BITTree

    def getsum(self, i):
        s = 0  # initialize result
        # index in BITree[] is 1 more than the index in arr[]
        i = i + 1
        # Traverse ancestors of BITree[index]
        while i > 0:
            # Add current element of BITree to sum
            s += self.BITTree[i]
            # Move index to parent node in getSum View
            i -= i & (-i)
        return s

    # Updates a node in Binary Index Tree (BITree) at given index
    # in BITree. The given value 'val' is added to BITree[i] and
    # all of its ancestors in tree.
    def updatebit(self, n, i, v):
        # index in BITree[] is 1 more than the index in arr[]
        i += 1
        # Traverse all ancestors and add 'val'
        while i <= n:
            # Add 'val' to current node of BI Tree
            self.BITTree[i] += v
            # Update index to that of parent in update View
            i += i & (-i)


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        nums_ftree = ftree(nums, len(nums))

        max_sum = nums_ftree.getsum(len(nums) - 1)
        min_avg = max_sum
        mindex = 0

        for i in range(len(nums)):
            i_sum = nums_ftree.getsum(i)
            new_avg = abs(
                (i_sum // (i + 1)) - ((max_sum - i_sum) // max((len(nums) - i - 1), 1))
            )
            if new_avg < min_avg:
                min_avg = new_avg
                mindex = i
        return mindex


# class Solution:
#     def minimumAverageDifference(self, nums: List[int]) -> int:
#         def getsum(BITTree,i):
#             s = 0 #initialize result
#             # index in BITree[] is 1 more than the index in arr[]
#             i = i+1
#             # Traverse ancestors of BITree[index]
#             while i > 0:
#                 # Add current element of BITree to sum
#                 s += BITTree[i]
#                 # Move index to parent node in getSum View
#                 i -= i & (-i)
#             return s

#         # Updates a node in Binary Index Tree (BITree) at given index
#         # in BITree. The given value 'val' is added to BITree[i] and
#         # all of its ancestors in tree.
#         def updatebit(BITTree , n , i ,v):
#             # index in BITree[] is 1 more than the index in arr[]
#             i += 1
#             # Traverse all ancestors and add 'val'
#             while i <= n:
#                 # Add 'val' to current node of BI Tree
#                 BITTree[i] += v
#                 # Update index to that of parent in update View
#                 i += i & (-i)

#         # Constructs and returns a Binary Indexed Tree for given
#         # array of size n.
#         def construct(arr, n):
#             # Create and initialize BITree[] as 0
#             BITTree = [0]*(n+1)
#             # Store the actual values in BITree[] using update()
#             for i in range(n):
#                 updatebit(BITTree, n, i, arr[i])
#             return BITTree

#         ftree = construct(nums, len(nums))

#         max_sum = getsum(ftree, len(nums)-1)
#         min_avg = max_sum
#         mindex = 0

#         for i in range(len(nums)):
#             i_sum = getsum(ftree, i)
#             # left = (i_sum//(i+1))
#             # right = (max_sum - i_sum)//(len(nums)-i-1)
#             # new_i_avg = abs(    (i_sum//(i+1)) - (  (max_sum - i_sum)//(len(nums)-i-1)  )    )
#             new_avg = abs(    (i_sum//(i+1)) - (  (max_sum - i_sum)//max((len(nums)-i-1),1)  )    )
#             if new_avg < min_avg:
#                 min_avg = new_avg
#                 mindex = i
#         return mindex
