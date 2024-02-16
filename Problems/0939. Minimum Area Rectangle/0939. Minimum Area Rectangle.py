# 02-15-2024 Leetcode 939. Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/
# Time: 25 mins Challenge: 5/10

# I cant think of anything better than this dict/set O(n**3)
# solution...

# and it worked perfectly fine and is in the top 3%?!


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        coords = collections.defaultdict(set)
        for x, y in points:
            coords[x].add(y)
        for x in list(coords.keys()):
            if len(coords[x]) < 2:
                del coords[x]
        
        min_area = 10**9 + 7

        x_sorted = sorted(coords.keys())
        for i in range(len(x_sorted) - 1):
            for j in range(i+1, len(x_sorted)):
                x_dif = x_sorted[j] - x_sorted[i]
                if x_dif >= min_area:
                    break
                y_set = coords[x_sorted[i]].intersection(coords[x_sorted[j]])
                if len(y_set) < 2: 
                    continue
                y_set = sorted(y_set)
                for k in range(1, len(y_set)):
                    y_dif = y_set[k] - y_set[k-1]
                    min_area = min(min_area, x_dif * y_dif)
        return min_area if min_area != 10**9 + 7 else 0
