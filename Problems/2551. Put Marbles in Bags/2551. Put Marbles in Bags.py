# 07-09-2023 Leetcode 2551. Put Marbles in Bags=
# https://leetcode.com/problems/put-marbles-in-bags/description/

# Pretty obvious packing problem, which typically DO NOT have a greedy
# solution. We must either aproximate with some hueristic or check
# every combination. Often there is a shortcut to early exit
# so backtracking is often the go to. 

# This one is a little weird in that we may be able to ignore some stuff?
# We are only looking for the max and min of the solution, and that may
# be able to be greedyish? 

# We are guarenteed to have at least enough marbles such that we can put
# one in every bag, no need to check for failure. If there are the SAME
# number of marbles as bags, then we can just return 0: Each bag gets one
# marble and the max and min are the same.

# After this case, every other case obviously has at least 1 bag with multiple
# marbles, possibly all of them.

# Min: We must fill k bags, 1 or more requiring multiple marbles. We want to use the
# k smallest digits for "one side of the bag", and up to the next k smallest digits for
# "the other side of the bag". As we are summing the two marbles for a bag cost, then 
# simply summing the bags, order doesnt matter. BUT as we are grabbing indexes from a list
# order DOES matter.

# Aha, now I understand the problem, if not the solution:
# We need to divide the array into k subbarrays such that the sum of each subarrays
# left and right indecies are A) minimal, and B) maximal. We then simply compute this
# difference.

# This can be done somewhat trivially with k nested for loops via recursion:
# use the last k-1 indexes as solo marbles, and all the remainder go in the first bag,
# update min and max. Shrink first bag by one and add it to the second bag. Continue
# until the FIRST k-1 indecies are in bags and k-1 marbles are in the last bag. 
# This is seemingly VERY costly.

# How to do some precomputation? So we could do a 2d array and for each index, compute the cost
# to each other index so at least we arent doing the addition over and over. 

# New insight: Obviously we must include the ends of the existing array in bag ends. These Left
# and Right bags may then expand to take up more space, but wherever they stop they leave a smaller
# array with k-2 bags to distribute, who must also use their new ends for the left and right, til
# the final bag (if odd) which must use the whole array. Does this make it DP?

#We may also be able to do something with monotonically increasing sequences. 

# There must be a trick but I am not seeing it. K  and weights being of order 10**5 is QUITE
# large and I dont think we can reasonably compute every combination. 


# Ok, imagine a row of marbles and we have to stick k-2 playing cards between them. Each playing
# card has a value. Those cards are just the left and right index of two DIFFERENT bags but since 
# they are just additive, we can flip this so they are the sum of one meta-bag.
# In this sense, we are flipping the idea of bag edges. Physically imagine we sew all the bags together,
# each seam has a value. As we must use the outside ends of the array, that counts for the left and
# right edges of our bag strip. Thats 2 edges, so effecitvely "one bag". We then need k-1 pairs internally
# and the order DOESNT MATTER. We precompute every internal space where a card/seam could go and since they
# are mutually exclusive, just take the min/max k-1. Dead simple. I was so close

# We can IGNORE the left and right edges as they are both added to the min and max, then are getting
# the difference between those two so they are supressed back out. Its literally the difference between
# the max k-1 pairs and the min k-1 pairs 

# class Solution:
#     def putMarbles(self, weights: List[int], k: int) -> int:
#         return sum((seams := sorted([weights[i]+weights[i+1] for i in range(len(weights) - 1)]))[-(k-1):]) - sum(seams[:k-1]) if (k != len(weights) and k != 1) else 0

        # if k == len(weights) or k == 1:
        #     return 0

        # seams = sorted([weights[i]+weights[i+1] for i in range(len(weights) - 1)])
        # return sum(seams[-(k-1):]) - sum(seams[:k-1])

class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        return sum((s:=sorted([w[i]+w[i+1] for i in range(len(w)-1)]))[-(k-1):])-sum(s[:k-1]) if (k!=1) else 0
