# 03-08-2023 Leetcode 1055. Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/description/

# Well first things first, the source must contain at LEAST all the chars
# of the target. It can have extra, and we can discard them freely.
# Once we do this, make a set of source and target, they should be equal
# (since weve discarded extraneous letters in source), if not return -1 now.

# Now lets make a dict where we store letters in the source as the key and indexes
# the letter can be found at as a list for its value.

# We have to have a first char, so lets start there. We may as well use the first
# matching letter in our source for it, so start counting our first subsequence.
# This is subsequence one, and note what index the last matched letter came from.
# Lets say we are looking for a "q" and the lowest index to find a q in source is 4
# num_subsequences = 1, last_match_idx = 4
# Now we need the second leter in the target. If there is a match for that WITH an index
# greater than last_match (and by definition, smaller than len(source)), then selecting
# the lowest index for this second match is the best we can do. Update last_match_idx.
# If there is NO match with an idx smaller than last match then clearly we need to start
# a new subsequence. Add 1 to num_subsequence. The match is instead the first index of this
# char, disregarding the previous last_match_idx. Update and continue. Do this for all
# letters in target. Hey!

# Now that we are getting comfortable with using the built in bisect method, we can use that
# to efficiently find the lowest indexed match larger than last_match_idx

# We could just do this with two pointers: one for target, and one that loops on source. Each
# time it wraps source just add 1 to num_subsequences


class Solution:
    def shortestWay(self, source, target) -> int:
        letters_in_target = set(target)
        source_map = collections.defaultdict(list)
        for index, char in enumerate(source):
            if char in letters_in_target:
                source_map[char].append(index)

        num_subsequences = 1
        last_match = -1

        for char in target:
            if char not in source_map:
                return -1
            if source_map[char][-1] < last_match:
                num_subsequences += 1
                last_match = source_map[char][0]
                continue
            next_match = bisect.bisect_left(
                source_map[char], True, key=lambda mid: mid > last_match
            )
            if next_match == len(source_map[char]):
                num_subsequences += 1
                last_match = source_map[char][0]
            else:
                last_match = source_map[char][next_match]

        return num_subsequences
