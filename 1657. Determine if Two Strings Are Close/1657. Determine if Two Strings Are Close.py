# 12-1-2022 LeetCode 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

# Swapping "any two" means absolute free
# rearangement. You can always shuffle enough times
# to allow any ordering. We can actually literally ignore
# the ordering requirement.

# I believe the swapping letters thing is also similarly odd:
# if there are the same number of each letters, this is no differnt
# than merely shuffling the letters around more. However, this IS a
# useful operation for disimilar numbers of letters.

# Obviously the strings must be of the same length to start with.

# So we are only interested in swapping letters. If we have too high of
# count of one letter set, and too low on another we would just swap
# those counts... But its complicated. I guess we need the differences
# between them to align. How do we go about finding that?

# A Counter is ideal to start with: count of each letter, destroys the
# ordering which we dont care about anyway.

# Wait... it doesnt actually matter what the letters are either, just their
# number groupings. We cant actually change the numbers within groupings,
# just literally what letter that grouping is assigned. If there are 6 "B"s
# these can all beome "A"s but its still 6 of them. So we dont care
# about the letters or how the swaps are done: if they dont have the
# same grouping then there is nothing we can do

# So this enitre problem is a trick! Operation 1 is useless and we can
# check if enough operations 2s would be useful in one go without
# having to actually do any of the swaps

# Oh wait, we can only swap existing letters. That means the two words
# need to have the same keys in the Counter, then check group numbers
# Still a trick. Still an extremely easy answer. I kind of love it.

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1c = Counter(word1)
        w2c = Counter(word2)
        return sorted(w1c.values()) == sorted(w2c.values()) and sorted(w1c.keys()) == sorted(w2c.keys())

        # Note: This is a dumb "one liner" as Im creating each counter twice. Maybe its holding on to them?
        return set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(
            Counter(word2).values()
        )
