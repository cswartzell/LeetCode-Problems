import bisect
import collections
import math


s1 = "abcdebdde"
s2 = "bde"

letter_indexes = collections.defaultdict(list)
for index, letter in enumerate(s1):
    letter_indexes[letter].append(index)

# Could run through and make sure there is one copy of every letter in this dict,
# but it wouldnt give us order info so may not be worth the time to check
# Maybe better to check here once rather than repeatedly in the loop
if any(letter not in letter_indexes for letter in s2):
    # return ""
    print("oops")

# We COULD check if there is a letter in s2 that only has ONE position in S1.
# If so, we squeeze toward it. There can multiple letter where that is true.

min_L, min_R = 1001, -1
min_len = math.inf

# For each starting letter in s2
while letter_indexes[s2[0]]:
    L = letter_indexes[s2[0]].pop()
    curr_i = L
    unfound = False
    # While the curr_len might be smaller, and we have letters to find
    for s2_next in s2[1:]:
        if curr_i + 1 - L > min_len:
            break
        # get minimum index of next letter, or bail if there isnt one after curr_idx
        next_i = bisect.bisect_left(letter_indexes[s2_next], curr_i)
        if next_i == len(letter_indexes[s2_next]):
            unfound = True
            break
        curr_i = letter_indexes[s2_next][next_i]
    if not unfound:
        if curr_i - L <= min_len:
            min_L, min_R, min_len = L, curr_i + 1, curr_i + 1 - L

    # return s1[min_L:min_R] if min_len != inf else ""
    print(s1[min_L:min_R] if min_len != math.inf else "double oops")
