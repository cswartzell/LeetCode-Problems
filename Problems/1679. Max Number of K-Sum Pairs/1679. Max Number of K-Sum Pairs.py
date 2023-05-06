"""05-04-2022 Leetcode 1679. Max Number of K-Sum Pairs"""
from collections import Counter
import random

# I guess I can just rely on Python's magic "in" for this one
# Seems... trivial. Complications? It doesnt say there isnt
# duplicate values. Ok, lets assume this is part of the trick.
# Using a Counter container basically solves that one.
# How to select from our counter keys? At random seems fun.
# Probably random is going to time out.


# trial = random.choice(  list( cnums.keys() )  )
# As expected, recreating a list of keys each time is quite slow. I guess we can save
# this as a seperate set and pop from that set of keys since Counter() does not have a
# pop or quick random or sequential access.


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnums = Counter(nums)
        numset = set(
            cnums.keys()
        )  # obnoxious duplicate of key list for fast pop and remove
        ops = 0
        while numset:
            trial = numset.pop()
            if trial == k / 2:
                ops += cnums[trial] // 2
            elif (k - trial) in numset:
                ops += min(cnums[trial], cnums[k - trial])
                numset.remove(k - trial)
        return ops
