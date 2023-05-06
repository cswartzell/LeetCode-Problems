# 03-19-2023 Leetcode 1743. Restore the Array From Adjacent Pairs
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/


# So if EVERY adjacent pair is in the list, then every node will be in the list twice...
# EXCEPT for the start and end. Each of these will be in the list just once.
# There are therefore TWO equally valid sequences, as we have no way of knowing
# which singlet is the start and which is the end. Pick one at random and build out.


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for l, r in adjacentPairs:
            adj[l].append(r)
            adj[r].append(l)

        for x in adj:
            if len(adj[x]) == 1:
                break
        ans = [x]
        next_i = adj[x][0]

        while len(adj[next_i]) > 1:
            ans.append(next_i)
            for j in adj[next_i]:
                if j != ans[-2]:
                    next_i = j
                    break
        return ans + [next_i]
