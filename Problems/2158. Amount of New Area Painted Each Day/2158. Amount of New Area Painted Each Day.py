# 04-11-2023 Leetcode 2158. Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/description/

# So obviously there is a trivial ansawer where we just store an array of 10**5 bools
# of "already painted". Bisect left AND right in the days range to quickly find the
# new area to paint, fill in our array. Honestly, Its not a bad solution and
# 10**5 bools is kinda nothing. In an interview I might present this as a backup plan.

# No, wait. Doesnt work, requires linear scan or repeated binary searches:
# Take [2,3], [5,7], [1,10]
# The last day of paint is adding some to the left, center, and right. Its not a simple
# stop and start.

# Oh! Its just union find of course. Just list the STOP location for a painted section to
# be the root. That way we skip ahead through done sections when doing a linear scan

# basic Union Find class. Will need to add returns


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        root = list(range(50001))

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union_to(x, y):
            i = x
            count = 0
            while i < y:
                i_root = find(i)
                if i_root == i:
                    root[i] = y
                    count += 1
                elif i_root < y:
                    i = i_root - 1
                else:
                    break
                i += 1
            return count

        work_log = []
        for start, stop in paint:
            work_log.append(union_to(start, stop))

        return work_log
