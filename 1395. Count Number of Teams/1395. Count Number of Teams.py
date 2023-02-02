# 02-01-2023 Leetcode 1395. Count Number of Teams
# https://leetcode.com/problems/count-number-of-teams/description/

# Is there a way other than to just do it?


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        num_teams = 0

        # Pretty clever O(n**2) solution, but I definitely needed a hint.
        # The key is to iterate considering the MIDDLE value, and look for
        # smaller/larger counts before, and after its position. That way we
        # are iterating just twice instead of 3 deep. LOTS of if statements here
        # which can be expensive. I tried to elif to reduce total executed
        for i in range(len(rating)):
            num_less_before, num_more_before, num_less_after, num_more_after = (
                0,
                0,
                0,
                0,
            )
            for j in range(len(rating)):
                if j < i:
                    if rating[j] < rating[i]:
                        num_less_before += 1
                    elif rating[j] > rating[i]:
                        num_more_before += 1
                elif j > i:
                    if rating[j] < rating[i]:
                        num_less_after += 1
                    elif rating[j] > rating[i]:
                        num_more_after += 1
            num_teams += (
                num_less_before * num_more_after + num_more_before * num_less_after
            )

        return num_teams

        # #TLE For sure right? O(n**3 practically)
        # for i in range(len(rating)-2):
        #     for j in range(i+1, len(rating)-1):
        #         for k in range(j+1, len(rating)):
        #             if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
        #                 num_teams += 1
        # return num_teams
