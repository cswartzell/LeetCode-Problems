# 03-03-2023 Leetcode 1762. Buildings With an Ocean View
# https://leetcode.com/problems/buildings-with-an-ocean-view/description/
# Again, an absurdly simple "medium"


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # ans = collections.deque()
        ans = []
        tallest = 0
        for building_i in range(len(heights) - 1, -1, -1):
            if heights[building_i] > tallest:
                # ans.appendleft(building_i)
                ans.append(building_i)
            tallest = max(tallest, heights[building_i])
        # return list(ans)
        # return ans[::-1]
        return reversed(ans)
