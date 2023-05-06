# 04-13-2023 Leetcode 1936. Add Minimum Number of Rungs
# https://leetcode.com/problems/add-minimum-number-of-rungs/description/


class Solution:
    # def addRungs(self, r: List[int], d: int) -> int:
    # return r[0]//d-int(r[0]%d==0)+sum((r[i]-r[i-1])//d-int((r[i]-r[i-1])%d==0) for i in range(1,len(r)) if r[i-1]+d<r[i])

    # class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:

        # added = 0
        # curr_height = 0
        # next_rung = 1
        # while curr_height < rungs[-1]:
        #     if rungs[next_rung] - curr_height > dist:
        #         new_rungs =  (rungs[next_rung] - curr_height) // dist
        #         added += new_rungs
        #     curr_height = rungs[next_rung]
        #     next_rung += 1
        # return added
        return sum(
            (nxt - prv) // dist - ((nxt - prv) % dist == 0)
            for prv, nxt in zip([0] + rungs, rungs)
        )
