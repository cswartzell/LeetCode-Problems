# 11-26-2022 Leetcode 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

# So it may be easier on conditions if we literally
# sorround the given grid in one more row/col of water on each edge

# Ah, I can just BFS anywhere there is a one, replacing the 1s
# with another value, storing the input values so I can just check
# if we got all the 1 land masses. Sure would have been nice if land
# WASNT marked as 1, as I could use 1 to designate the areas of the
# first Island. Could just use negative number.

# How do we scan for land? I can think of 3 options.
# First, we linear scan the whole map, and save every coordinate pair
# that is a 1. If saved into a hash, we can delete these as we flood
# fill BFS adjacent land. Could be a hashmap of 300*300 chars, which
# while not a ton, isnt tiny either?
# We could instead keep a list of seen tiles, water or dealt with land,
# but this is the same as creating the hashmap, but in reverse. Actually
# its larger, as wed have to store the water tiles too. Well, larger on
# average. Worst case for storing land tiles is 'its all land'

# Or, we could start a linear scan each time we are done processing
# a land area? This seems kinda dumb. We could I guess have the whole
# algo part of the original linear scan, but interupt it to flood fill
# every time we encounter a 1. I think this is the way to go. We could
# technicaly jump the linear scan along a bit by adding some offset
# discovered in the BFS when filling, but it hardly seems worth it.
# Wont improve worst case, and it seems like storing some hasmap of
# visited nodes doesnt really help. How much faster to check if a node
# is visited, vs if its 0,1, or otherwise?

import string


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        self.num_isles = 0

        def flood(row, col):
            # For fun, pick a random printable single char to 'name' the island
            # NOTE: random char just cant be "1". Should be single space, "normalish" char
            # technically there could be M*N/2 islands, in this case 45,000, so a BIT
            # more than the ascii printable chars. Holy shit, should we move for unicode?
            island_char = random.choice(string.printable)
            if island_char == "1":
                island_char = "*"

            steps = [(row, col)]
            grid[row][col] = island_char

            self.num_isles += 1

            # I see we could MASIVELY improve on comparisons here by keeping a hashmap of visited nodes
            # Again, this wouldnt help the worst case, but on average... how big are these islands? Real
            # world data could be used to determine if a local hashmap for THIS island would be more
            # efficient than performing all the contraints checks.
            while steps:
                curr_pos = steps.pop()
                for row_d, col_d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (
                        0 <= curr_pos[0] + row_d < len(grid)
                        and 0 <= curr_pos[1] + col_d < len(grid[0])
                        and grid[curr_pos[0] + row_d][curr_pos[1] + col_d] == "1"
                    ):
                        grid[curr_pos[0] + row_d][curr_pos[1] + col_d] = island_char
                        steps.append((curr_pos[0] + row_d, curr_pos[1] + col_d))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    flood(row, col)

        return self.num_isles
