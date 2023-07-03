# 07-02-2023 Leetcode 2522. Partition String Into Substrings With Values at Most K
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/description/

# I THINK this is backtracking. We are going to have to try each partitioning.

# Ugh. As a crazy minor optimization we could check if k is under 9, and if so
# check if any digit in str is over k.

#No! It can be greedy. We want to always add the next digit to the smallest partition
# Also, once added, we can resort the partition to minimize it. We can do it with heaps

#And once again I've failed to read the problem. We arent just partitioning digits 
# willy nilly, its substrings... meaning order matters. Meaning this problem is trivial:
# Start a total at 0. Multiply total by 10 and add the new digit. If less than k, contnue.
# If greater than k, add 1 to ans as that last partition is full, and start over with a new
# total that equals this new digit

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if k <= 9:
            if max(set(s))>str(k):
                return -1
        
        s_ints = list(int(x) for x in s)
        
        ans = 1
        total = s_ints[0]
        for digit in s_ints[1:]:
            if (update := total*10 + digit) <= k:
                total = update
            else:
                total = digit
                ans += 1
        return ans







        #Unecessary Heap Answer
        # if k <= 9:
        #     if int(max(set(s)))>k:
        #         return -1
        
        # s_ints = list(int(x) for x in s)
        
        # def list_to_int(part: list) -> int:
        #     part.sort()
        #     total = 0
        #     for digit in part:
        #         total = total*10 + digit
        #         if total > k:
        #             return k + 1
        #     return total

        # heap = [[s_ints[0]]]
        # ans = 1
        
        # for digit in s_ints[1:]:
        #     if list_to_int(heap[0] + [digit]) < k:
        #         heapq.heappush(heap, heapq.heappop(heap) + [digit])
        #     else:
        #         heapq.heappush(heap, [digit])
        #         ans += 1
        
        # return ans



    # Unecessary backtracking answer: Pretty close and decent

    # def minimumPartition(self, s: str, k: int) -> int:
    #     if k <= 9:
    #         if int(max(set(s)))>k:
    #             return -1
    #     s_ints = list(int(x) for x in s)
        
    #     self.min_parts = math.inf
    #     self.partitions = []
    #     def partition(i):
    #         see_partitions = self.partitions
    #         see_ans = self.min_parts
    #         #If we have partitioned the last number potentially update the number of partitions
    #         # All partitions OUGHT to be valid, as they would not have been added to the list
    #         # if they were invalid to begin with
    #         if len(self.partitions) >= self.min_parts:
    #             return

    #         if i == len(s_ints):
    #             self.min_parts = min(self.min_parts, len(self.partitions))
    #             return

    #         for j in range(len(self.partitions)):
    #             if 10*self.partitions[j] + s_ints[i] <= k:
    #                 # self.partitions[j] = updated 
    #                 self.partitions[j] = 10*self.partitions[j] + s_ints[i]
    #                 partition(i+1)
    #                 self.partitions[j] //= 10

    #         self.partitions.append(s_ints[i])
    #         partition(i+1)
    #         self.partitions.pop()

    #     partition(0)
    #     return self.min_parts
f