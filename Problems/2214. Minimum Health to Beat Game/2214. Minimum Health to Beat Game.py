# 01-08-2023 Leetcode 2214. Minimum Health to Beat Game
# https://leetcode.com/problems/minimum-health-to-beat-game/description/

# Isnt this just the sum of the damage, + 1 to survive, minus
# the min(armor, max(damage))? Yep. Wow. A medium?


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) + 1 - min(armor, max(damage))
