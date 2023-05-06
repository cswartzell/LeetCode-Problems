# 12-28-2022 1962. Remove Stones to Minimize the Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

# So we are taking away half the stones in a pile, k times, and after k
# scoops, we want the fewest stones to remain. This is a maxheap problem.
# We simply take the biggest scoop we can each time. A maxheap makes this
# easy: pop the top, scoop from it, put it back. We can then simply count
# at the end how many are remaining, and this shouldnt be any slower than
# counting at the beginning, and may in fact be faster if some piles dissappear

# As always, python doesnt have a maxHeap. You can get the functionality by
# negating all values, but have to swap back and forth... obnoxiously. This is
# not clever, and seems to be antithetical to pythons stated design.

# Well fuck me! It seems like someone started to write all the max_heap
# functions and just... didnt? There is heapify, pop, replace, but not
# Push, so I guess its unusable as is. The underlying _shift() functions
# even are in place so they just skipped like 4 lines of code to implementing
# function max_heaps as standard. WTF. This is one of the first times I've
# been poking about in docs and am just... upset at how close they came


import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # #Ugh... if we're going to negate for maxHeap, we may as well
        # #do it in a loop and count the starting number of stones simultaneously
        # stones = 0
        # for i in range(len(piles)):
        #     stones += piles[i]
        #     piles[i] *= -1

        # # piles = [-x for x in piles]   #Negate for maxHeap
        # heapq.heapify(piles)

        # # for _ in range(k):
        # #     big_pile = -1 * heapq.heappop(piles)
        # #     halved = big_pile // 2      #so we dont have to divide twice. Faster?
        # #     stones -= halved
        # #     heapq.heappush(piles,- 1 * (big_pile - halved) )

        # #If we swap math.ceil for // we can leave the values negative.
        # #just remember to "add" the negative stones to remaining stones
        # #to remove them
        # for _ in range(k):
        #     big_pile =heapq.heappop(piles)
        #     halved = math.ceil(big_pile / 2)        #so we dont have to divide twice. Faster?
        #     stones += halved                        # "Adding" negative stones
        #     heapq.heappush(piles, big_pile - halved )   # Again, sign weirdness. We ARE removing the stones from the big_pile.
        #                                                 # Even though big_pile is negative, we remove halved by subtraction
        #                                                 # as halved is also negative. This reduces big_pile by removed (via additon)
        #                                                 # as we are maintaining the negative values for maxHeap reasons

        # return stones

        piles = [-x for x in piles]
        # piles = list(map(lambda x: -x, piles))

        # def negate(i):
        #     return -i

        heapq.heapify(piles)

        # ooh, VERY clever. We know piles[0] is the max of the heap, and heapreplace is FASTER than a pop then a Push
        # This allows to use the max val WITHOUT popping it first (by peeking), then POP (ignoring the return) THEN Push
        # the modified value.

        # Wait, I thought // for negative numbers was going to be wrong?
        # OH! fucking duh. piles[0] // 2 IS the ceiling for negative numbers, and what REMAINS is the ceiling. I was calculating
        # what we took away, which is the floor (as they are complimentary), then subtracting this. There isnt a need for that.
        # I was doing so in a dumb attempt to save on repeated addition, as I was then tracking how many stones we take away
        # instead of just summing stones remaining at the end. I only did THAT as i noted in the negating step we were already
        # running through all n stones, so I thought if we simply counted them then, we WOULDNT need another counting step at the end
        # This ends up being the same number of calculations though as I effectively added in an added operation within the n loop.
        # Simply summing at the end IS just as fast, if not faster by simply using the // op instead of an additional sum and subtract

        for _ in range(k):
            heapq.heapreplace(piles, piles[0] // 2)

        return -sum(piles)
