# 11-23-2022 LeetCode 79. Word Search
# https://leetcode.com/problems/word-search/

# We could start by creating some sort of map. Maybe
# a dict where the keys are the 26 letters, and the values
# are a list of tuple coordinates? Is then using this any
# faster than a direct BFS starting with each starting letter?

# Lets just try the BFS version first. Remember, that means deques

# Well shoot. Theres a lesson in reading the prompt.
# Each letter may NOT be used more than once. I thought it COULD
# and actually liked the clever variance that caused. So now I have
# to keep some kind of visited list. This maybe should have been
# done via recursion, since I cannot have a global visited list
# as part of a BFS solution. I could switch it to a DFS solution...
# I note the grids are TINY, no bigger than 6x6, so we can just
# append a list of visited cells to each element in our deque.
# Really, this is how a recursive function would work and so its
# like its actually more memory intensive anyhow.

# aaaaaaaand TLE. At least this time I preceisely predicted
# the worst case: the grid is all the same letter and the word
# is as well.
# Also, my solution TECHNICALLY works. Its just not fast enough.
# In an interview environment I'd be able to make my case that
# at least I have a solution, though it can be improved on.
# Every starting postion is valid, and every step
# is valid. O((m*n)**2) at least.

# Is working backwards any better? Doesnt seem like it ought to be
# We could aslo eliminate every letter not in the grid/mark out
# every cell with a non used letter in a restricted list, but again
# I dont think thats any faster than the checks we are doing here.
# Somewhat interestingly, if you X out an entire row or column
# you can actually remove it from the search space, thus significantly
# cutting down on the processing. Seems like a crapshoot for
# anything but a very heterogenuous grid. NONE OF THESE
# ideas affect the "All As" grid failure, so cant really be
# part of the solution.

# now we could do a little check in the beginning scan, adding
# letters to a set and checking that the set at least HAS all
# the letters in the word. Might speed things up for large cases
# but doesnt actually affect the worsrt case scenario listed above.
# We could go a step further and create a nebulous graph, tracking
# which letters lead to other letters, but NOT their positions?
# You could quickly check if there is the potential for a solution
# but frankly that seems pretty dumb right?


# Ok, in the real world is the recursive solution beter as we can
# take advantage of multithreading? Doesnt improve the worst case,
# but does actually process it faster? I think we ignore this question
# for these testing scenarios however.

# I guess lets change it to DFS and sere if that improves things.
# I dont see how, in the case of a grid made of all "A" and a word
# of all "A", followed by one "B" we will process the same nodes...


# Oh wait... What if we mark squares out that we know fail?
# This has got to be the key. It IS a backtracking problem.
# if we follow a chain and it ultimately fails, we dont want
# to waste time falling into any part of that same chain again.

# Can we use what we have here? IFF we cannot take any further
# steps from a curr cell, what does that tell us? Not much: it means
# for this position in the word only, it doesnt lead to the next
# letter. Any letter in the current chain could be part of a different
# path, or in a different position in the word and still be a valid
# square. I dont think we can mark ANYTHING as being invalid...


# HORSESHIT. I dicked with this for an hour and a half, read a number
# of other frustrated users who couldnt get it to be under TLE,
# considered a number of tweaks that improve average, but not worst
# case time (thus doing nothing to pass TLE). In the end I just reverted
# all my changes and submitted the most minor tweak on my first attemp:
# Passed immediately, (albeit bottom 30%). Thats NONSENSE. The official
# answer is recursive, but for no additional benefit. Literally nothing
# is gained by it.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find starting locations
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs = deque()
                if board[row][col] == word[0]:
                    dfs.append((row, col, 0, {(row, col)}))

                # base case for single letter word, alleviates index errors in loop
                if len(word) == 1 and dfs:
                    return True

                while dfs:
                    curr_row, curr_col, word_i, visited = dfs.pop()
                    for xd, yd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if (
                            0 <= curr_row + xd < len(board)
                            and 0 <= curr_col + yd < len(board[0])
                            and (curr_row + xd, curr_col + yd) not in visited
                        ):
                            if board[curr_row + xd][curr_col + yd] == word[word_i + 1]:
                                if word_i + 1 == len(word) - 1:
                                    return True
                                dfs.append(
                                    (
                                        curr_row + xd,
                                        curr_col + yd,
                                        word_i + 1,
                                        visited | {(curr_row + xd, curr_col + yd)},
                                    )
                                )
        return False
