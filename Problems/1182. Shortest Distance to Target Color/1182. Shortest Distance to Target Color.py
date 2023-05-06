# the brute force approach seems obviously trivial...
# the len of the array is long, but not insane at 5000
# but we could have 5000 queries

# Ok, lets just build 3 parallel arrays, dist_to_color_x
# I think we can start by scanning the array and tossing
# indexes per color into three different stacks
# We can then use differences between these stacks to build
# up our color offset array
from math import ceil


class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        num_colors = 3
        # buckets for the indexes each element of colors array
        dist_clr_stk = [[] for _ in range(num_colors)]  # may as well generalize it.
        # distance to the next element  of this color from the given index
        # (as in, if this index IS the color, dist == 0, if there is one spot of that color
        # one index away, then dist = 1...)
        dist_clr = [
            [-1 for _ in range(len(colors))] for _ in range(num_colors)
        ]  # Default value (could use dicts?)

        # start by sorting indexes of listed colors into buckets,
        # fill in spots on our color trackers with 0 when found
        for i in range(len(colors)):
            dist_clr_stk[colors[i] - 1].append(i)
            dist_clr[colors[i] - 1][i] = 0
        # set the dist to the first instance manually
        for color in range(num_colors):
            if dist_clr_stk[color]:
                first_idx = dist_clr_stk[color][0]
                for i in range(first_idx + 1):
                    dist_clr[color][i] = first_idx - i
                # set the dist to the last instance manually
                last_idx = dist_clr_stk[color][-1]
                for i in range(last_idx, len(colors)):
                    dist_clr[color][i] = i - last_idx

        # fill in remaining pair-sets of color distances
        for color in range(num_colors):
            if len(dist_clr_stk[color]) > 1:  # Done if theres only one instance
                # for each distance between pairs of elements
                for i in range(len(dist_clr_stk[color]) - 1):
                    curr_idx = dist_clr_stk[color][i]
                    next_idx = dist_clr_stk[color][i + 1]
                    between = next_idx - curr_idx - 1
                    # No space between indecies of same color
                    if between == 0:
                        continue
                    # count up from one end, down from the other, filling between
                    else:
                        for j in range(1, ceil(between / 2) + 1):
                            dist_clr[color][curr_idx + j] = j
                            dist_clr[color][next_idx - j] = j
                            # accounts for even and odd in one go, just double assigns
                            # the center dist count when the between is odd

        return [dist_clr[c - 1][i] for i, c in queries]
