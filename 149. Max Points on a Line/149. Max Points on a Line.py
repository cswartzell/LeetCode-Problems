# 01-08-2023 Leetcode 149. Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/description/

# Wow... ok. How do we do this in better than O(n**2)?
# Obviously we could just compare every point to every other point...
# There ARE only 300 points, so maybe an O(n**2) IS allowable?
# as the points range from -10,000 to 10,000 there are 20,001 possible buckets
# Obviously we could just use a dict for the lines we have but... what, with
# floats as the key? That seems rife for error. Wed have to have a tuple of
# the slope and the y intercept, BOTH floats, as the key. Should we use the
# DECIMAL data type for "precison". It would consistently round, but that
# of course produces its own sort of errors and may incorrectly lump two
# very near but identical lines

# Bucket sort using the slope to start? That finds buckets of
# PARALLEL lines, but not even same lines. We then need to solve
# the zeros. Jesus, I must be missing something.

# General equation for a line is y = m * x + b
# and for two points thats (y2 - y1)/(x2 - x1) + b
# to solve for b, plug in one of the points and subtract:
# y2 - (y2 - y1)/(x2 - x1)*x2 = b
#


# Well... This works for small input at least. It seems like a toddler solution.
# I dont like that we are using TWO floats in a tuple as a dict key. We are then
# Adding the same point to a buckets set posible MANY times. As its a set, it just
# rejects this but still.. way too much added work

# We could slightly reverse this logic and use the points tuple as the dict key
# and add (m,b) tuples to each point to note lines they fall on, then do a counter
# and return max, but I dont think this actually solves any of my concerns

# WOW! It worked, and wasnt bad in terms of timing. Maybe there isnt much of a better trick?
# I still think there must be a way to simply tally points rather than adding them to a set


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Base cases. If one point I GUESS a max of one point can be on any given line
        # and for two points there is only one such line that includes both by definition
        if len(points) < 3:
            return len(points)

        # lines are stored as (slope, y-intercept) tuples for keys, and a SET of points on said line
        # That way we dont end up miscounting copies of the same point as we compare.
        # Seems kinda dumb, should be a simple way to tally somehow, but I started with this and hey, it worked
        line_bucket = collections.defaultdict(set)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                # Must test for division by zero. Set slope as inf if so
                m = (
                    (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    if (points[j][0] - points[i][0]) != 0
                    else math.inf
                )
                # IFF slope IS inf, then the line is vertical and does not have a y intercept
                # In this case, we merely use its x intercept for b, which serves equally well to
                # denote seperate, parallel, vertical lines
                b = points[j][1] - (m * points[j][0]) if m != math.inf else points[j][0]
                # Add both points to said line. Possibly over and over and over...
                line_bucket[(m, b)].add((points[i][0], points[i][1]))
                line_bucket[(m, b)].add((points[j][0], points[j][1]))

        max__points = 0
        for x in line_bucket:
            max__points = max(max__points, len(line_bucket[x]))

        return max__points
