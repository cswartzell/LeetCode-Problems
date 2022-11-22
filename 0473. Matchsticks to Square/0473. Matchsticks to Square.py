"""07-11-2022 Leetcode 473. Matchsticks to Square"""

# ok, there are 4 choices for each match, and 15 matches
# The combinations is (close to) 4^15, or 2^30 rather.
# Its not quite full, since we must have at least one match per
# side, so that eliminates a small percentage of choices.
# It maybe is 4*3*2*1*4^11. So maybe 400Mb assuming 4 bytes
# but still far too many to enumerate them all...

# Im stumped, time to look at the answer: MOTHERFUCKER
# It IS one of those times were we recurse and simply
# try every combination. Horseshit. And I knew it was bin
# packing, which is NP-Complete: ie there is no nonexponential
# solution. You "have" to brute force it (for a clever value of brute)


from collections import OrderedDict


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        num_matches = len(matchsticks)
        # Hey look, I invented the OrderedCounter
        # match_dict = dict()
        # for match in matchsticks:
        #     total += match
        #     if match in match_dict:
        #         match_dict[match] = match_dict[match] + 1
        #     else:
        #         match_dict[match] = 1

        if perimeter % 4 != 0 or perimeter < 4:
            return False
        side_length = perimeter // 4
        side_total = [0 for _ in range(4)]
        matchsticks.sort(reverse=True)

        # ok, DFS recursion times out, onto DP. Straight up going to have
        # to follow along the solution as this is not something I know:

        @cache
        def dp(placed_matches, sides_done):
            total = 0
            for i in range(num_matches - 1, -1, -1):
                if not placed_matches & (1 << i):
                    total += matchsticks[num_matches - 1 - i]

            if (
                total > 0 and total % side_length == 0
            ):  # why not just if total == side_length? Ah, we are literally just
                sides_done += 1  # using one summation, and it needs to hit the target 3 times exactly

            if sides_done == 3:
                return True

            result = False

            # Holy shit... the following is to compute the remaining space in the current side
            # but since we just have a single sum, we have to remove multiples of already filled sides
            # rem stores available space in the current side (incomplete).
            blown_sides = int(total / side_length)
            rem = side_length * (blown_sides + 1) - total

            for i in range(num_matches - 1, -1, -1):
                if matchsticks[num_matches - 1 - i] <= rem and placed_matches & (
                    1 << i
                ):
                    if dp(placed_matches ^ (1 << i), sides_done):
                        result = True
                        break
            return result

        return dp(
            (1 << num_matches) - 1, 0
        )  # clever quick way to 1-fill a bitmask. Shift 1 N times, then subtract 1

        # Well my intuition was right... take the next longest match, and
        # place it in the first bin that has room for it. Then, recurse
        # through all matches until you find a match that doesnt fit or
        # you manage to fill all four sides

        # too bad this times out. O(4**n), absurd


#         def recurse(match_idx):
#             #test if three sides are done (4th side is a gimme then)
#             if match_idx == len(matchsticks):
#                 return side_total[0] == side_total[1] == side_total[2] == side_length

#             for side in range(len(side_total)):    #for each side...
#                 if matchsticks[match_idx] + side_total[side] <= side_length: #if match fits
#                     side_total[side] += matchsticks[match_idx]
#                     if recurse(match_idx+1):
#                         return True
#                     side_total[side] -= matchsticks[match_idx]
#             return False

#         return recurse(0)
