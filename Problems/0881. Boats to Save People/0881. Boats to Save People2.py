# 04-08-2023 Leetcode  881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/description/

# Solvable when its only two people. Always need to send the heaviest
# May as well send the lightest if possible.
# Just use two pointers


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        lightest, heaviest = 0, len(people) - 1

        # at least one person, so should account for base case
        while lightest <= heaviest:
            boats += 1
            if people[lightest] + people[heaviest] <= limit:
                lightest += 1
            heaviest -= 1
        return boats
