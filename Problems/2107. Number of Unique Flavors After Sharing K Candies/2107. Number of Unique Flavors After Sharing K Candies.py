# 02-01-2023 2107. Number of Unique Flavors After Sharing K Candies
# https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/description/

# Sliding window right?
# Yep, but real tricky


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        flavors = collections.Counter(candies)
        # flavors -= collections.Counter(candies[:k]) #This actually does remove them
        for x in candies[:k]:
            flavors[x] -= 1
        max_flaves = len(+flavors)

        curr_flaves = max_flaves
        for i in range(1, len(candies) - k + 1):
            if flavors[candies[i - 1]] == 0:
                curr_flaves += 1
            flavors[candies[i - 1]] += 1

            if flavors[candies[i + k - 1]] == 1:
                curr_flaves -= 1
            flavors[candies[i + k - 1]] -= 1

            max_flaves = max(max_flaves, curr_flaves)

        return max_flaves

        # I FEEL LIKE THIS SHOULD HAVE WORKED BUT TLE

        # flavors = collections.Counter(candies)
        # max_flaves = 0

        # for i in range(0, len(candies)-k+1):
        #     max_flaves = max(max_flaves, len(flavors - collections.Counter(candies[i:i+k])))

        # return max_flaves

        # flavors = collections.Counter(candies)
        # # given = collections.Counter(candies[:k])
        # max_flaves = 0

        # # for i in range(0, len(candies)-k+1):
        # #     # max_flaves = max(max_flaves, len(+(flavors-collections.Counter(candies[i:i+k]))))

        # # return max_flaves

        # window_count = collections.Counter(candies[0:k])
        # min_given = len(window_count)
        # for i in range(1, len(candies)-k+1):
        #     if window_count[candies[i-1]] == 1:
        #         del window_count[candies[i-1]]
        #     else:
        #         window_count[candies[i-1]] -= 1

        #     if candies[i+k-1] in window_count:
        #         window_count[candies[i+k-1]] += 1
        #     else:
        #         window_count[candies[i+k-1]] = 1

        #     min_given = min(min_given, len(window_count))

        # return max_flavors - min_given
