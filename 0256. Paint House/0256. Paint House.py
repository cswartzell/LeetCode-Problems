# First thing that comes to mind is a classic binary tree.
# Also, maybe an intro DP problem and I just dont know enough
# about DP to work through it. Anyhow, if you make an arbitrary
# choice for the first house on one end (the root), the next house
# will be left with just two choices, which can each be child nodes.
# Each of those have only 2 choices.... repeat til you get to the last
# house. Each node contains info on the color of that house, and total
# costs accumulated so far. Repeat this process for all 3 initial choices.
# It will work, but seems pretty redundant... Ill start with it and see
# if it passes.

# Wait, I'm an idiot. There are up to 100 houses, which means this would be
# a b-tree with a height of 100. 2^100 entries is going to be... well "a bit"
# I dont think this method is going to work at all. We are adding the same
# values over and over. This is what memoization is for. I really need to
# wrap my head around DP and memoization, its brilliant, relatively easy,
# and super critical to problems like this.


# Ok, reading my way through the brilliant solution document it gives a
# psuedocode block for its 3rd solution, recursion with memoization.
# This is an attempt to code that without lookin at the actual code

# Nice! It works and is just utterly straightforward. Simple obvious recursion
# but store the results in memo dict. Ive commented out the manual memo
# to try the LRU cache for automatic memoization. It works. Sweet
# class Solution:
#    def minCost(self, costs: List[List[int]]) -> int:
#         self.last_house = len(costs) - 1
#         # self.memo = {}           #manual memo, a dict

#         @lru_cache(maxsize=None)
#         def paint(n,color):
#             # if (n, color) in self.memo:
#             #     return self.memo[(n,color)]      #tuples can be keys as they are immutable
#             total_cost = costs[n][color]
#             if n == self.last_house:
#                 pass                        #exits the if block
#             elif color == 0:
#                 total_cost += min(paint(n+1,1),paint(n+1,2))
#             elif color == 1:
#                 total_cost += min(paint(n+1,2),paint(n+1,0))
#             elif color == 2:
#                 total_cost += min(paint(n+1,0),paint(n+1,1))
#             # self.memo[(n,color)] = total_cost
#             return total_cost

#         return min(paint(0,0), paint(0,1), paint(0,2))

# And so lastly we try to follow the DP solution. DP here is iterative, so beats memo recursion
# by a long shot. We start a DP by identifying a subproblem: Calculate the cost for a particular
# house (position/number) given a color. The key here is actually writing in the cacluclated costs
# directly into our input matrix, so we use that result for input in the future.

# My goodness... thats absurdly simple. The last row is the cost of painting the last house... so
# for each input in the row above it, simply pick the min of the remaining choices in the row below,
# and literally add it to the element in this row. Repeat. The choice propogates up. Its amazing once
# youve seen the directed graph diagram overlayed onto the input matrix.


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cycle = [0, 1, 2]

        for row in range(len(costs) - 2, -1, -1):
            for color in range(len(costs[row])):
                costs[row][color] += min(
                    costs[row + 1][cycle[color - 1]], costs[row + 1][cycle[color - 2]]
                )

        return min(costs[0])


# SCRAP THIS DUMMY HIGH TREE IDEA

# class TreeNode:
#     def __init__(self, color, cost):
#         self.color = color
#         self.running_total = cost
#         self.next_one = None
#         self.right_two = None

# class Solution:
#    def minCost(self, costs: List[List[int]]) -> int:
#     cycle = [0,1,2]
#     for x in cycle:
#         root = TreeNode(x, costs[0][x])         #start a b-tree with each of the colors for house 0

#         curr_node = root
#         for i in len(costs):
#             curr_node.next_one = TreeNode(cycle[curr_node.color-1], curr_node.running_total + )
