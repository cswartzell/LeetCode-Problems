# 04-15-2023 Leetcode 1639. Number of Ways to Form a Target String Given a Dictionary
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/
# Jesus FUCK this week is nonsense

# Ok, so first make an array or counters such that "there are 35 A's in all words 0th index.
# There are XX B's in the words 0 positions..." So each index covers how many of each letter
# We then just multiply these as we go... but we can skip indexes of course so now its
# a fucking backtracking thing "If we take Letter 0, which is an A, from words index 0. there
# are 35 choices. For letter 1, we can take that from words[1] OR skip it..."


# WITH NO FUCKING HINTS OH FUCK YES.
# This may be among the most difficult problems I've solved. Its so easy but so hard to grasp


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        FUNDICT = [
            collections.Counter(zipt) for zipt in zip(*[[*word] for word in words])
        ]

        dp = [[0 for _ in range(len(words[0]))] for _ in range(len(target))]

        def spell_it(letter_i, k):
            # If we are done spelling target
            if letter_i == len(target):
                return 1
            # If we have more letters to spell than idxs to spell with
            if len(target) - letter_i > len(FUNDICT) - k:
                return 0

            # If we've solved this so far
            if dp[letter_i][k]:
                return dp[letter_i][k]

            taken, skipt = 0, 0
            # If we can use the kth idx, do so
            if target[letter_i] in FUNDICT[k]:
                taken = spell_it(letter_i + 1, k + 1) * FUNDICT[k][target[letter_i]]

            # Also, try skipping using the kth idx
            skipt = spell_it(letter_i, k + 1)

            # store in DP
            dp[letter_i][k] = (skipt + taken) % (10**9 + 7)
            return dp[letter_i][k]

        return spell_it(0, 0)

        # FUNDICT = [collections.Counter(zipt) for zipt in zip(*[[*word] for word in words])]

        # @functools.cache
        # def spell_it(letter_i, k ):
        #     #If we are done
        #     if letter_i == len (target):
        #         return 1
        #     #If we have reached the last possible spelling idx and cant match the
        #     # next letter, or have more letters to spell than idxs to spell with
        #     if len(target) - letter_i > len(FUNDICT) - k or k == len(FUNDICT)-1 and target[letter_i] not in FUNDICT[k]:
        #         return 0

        #     taken, skipt = 0, 0
        #     #If we can use the kth idx, do so
        #     if target[letter_i] in FUNDICT[k]:
        #         taken = spell_it(letter_i + 1, k+1) * FUNDICT[k][target[letter_i]]

        #     skipt = spell_it(letter_i, k+1)

        #     return (skipt + taken) % (10**9 + 7)

        # return spell_it(0,0)
