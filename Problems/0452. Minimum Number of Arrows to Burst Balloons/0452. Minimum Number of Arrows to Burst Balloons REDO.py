# 03-13-2023 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

# 1) Sort them.
# 2) We need to hit the first at least, so somewhere in the first range. Arrow + 1
# 3) While the starttof next balloons is BEFORE the end of the first ballon,
# we can hit it while hitting the first. Repeat this logic: We are now hititng the
# second balloon, and must do so with SOME arrow prior to getting to THIS balloon's end.
# May as well be the arrow from before. Now check the NEXT balloon.
# keep moving arrow start right and end range left as we add balloons
# And by add balloons I mean pop them from a list. Or deque to move L to R.
# We could use a regular list but then wed have to do something tricky like reverse
# the tuples, or make them negative or whatever. Easier to just think of it forwards for me


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        BALLOON_START, NEXT_BALLOON = 0, 0
        q_points = collections.deque(sorted(points))
        arrows = 0
        while q_points:
            arrows += 1
            curr_left, curr_right = q_points.popleft()
            while q_points and q_points[NEXT_BALLOON][BALLOON_START] <= curr_right:
                next_left, next_right = q_points.popleft()
                curr_left = next_left
                curr_right = min(curr_right, next_right)
        return arrows
