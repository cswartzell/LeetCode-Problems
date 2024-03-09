# 03-08-2024 Leetcode 0851. Loud and Rich
# https://leetcode.com/problems/loud-and-rich/
# Time: 20 Challenge 5/10


# Well thats a hell of a tricky wording.I think this is a disjoint union thing.
# Specifically we DONT want to quick join, we need to iterate through the full list
# in a chain. The trick wording is "the loudest y that definitely has more than x"
# If we have disjoint sets, we have zero information about their relative levels: 
# therefore this clause means "only search within a union"

# Call our set richer_than, start with index == itself, every person is the richest they know.
# For each x,y pair in richer where x is richer than y, assign only x to y: Its the only relation
# we can surmise BETWEEN y and x. There could be a z that is between the two and thus righer than y
# but we have no way of knowing. Furthermore in usual cases we would assign the ROOT of x to y, to
# get to the richest person. In this case we want to PRESERVE that chain for later collection.

# We will chache chains so we dont waste time searching them repeatedly: the function get_loudest(x)
# will iterate through all parents of x, noting which is the loudest recursively. If we have
# x < y < z < a and a is the loudest, we can save that for each as we backtrack. SPECFICALLY
# only when backtracking: get to the root, then pass BACK max(root.volume, this.volume)
# and store that in a dict.

# Thinking about it, we need richer_than[x] to be a set. There could be multiple y richer than x
# given and again at first we dont know who is who. So really its more of just a simple BFS. 
# Ok, set to x:{x}, but on first ammending we need to delete that first x. 

# Ok... this is starting to look like union find again...


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_than = {x:{x} for x in range(len(quiet))}
        for x, y in richer:
            richer_than[y].discard(y)
            richer_than[y].add(x)

        def search(x):
            # already found: return loudest
            if ans[x] != -1:
                pass
            # X is the richest and therefore loudest
            elif richer_than[x] == {x}:
                ans[x] = x                
            else:
                ans[x] = x
                for y in richer_than[x]:
                    if quiet[search(y)] < quiet[ans[x]]:
                        ans[x] = y                
            return ans[x]
        
        ans = [-1 for _ in range(len(quiet))]
        for x in range(len(quiet)):
            search(x)
        
        return ans