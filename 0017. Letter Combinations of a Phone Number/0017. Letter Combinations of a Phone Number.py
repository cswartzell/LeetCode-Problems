"""05-08-2022 Leetcode 17 Letter Combinations of a Phone Number"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        # Only up to 4 chars huh. Lets start with the naive way
        # and just having up to 4 deep for loops

        ntoc = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        ans = [
            x for x in ntoc[digits[0]]
        ]  # Think I need to seed it with the first chars. Test this?
        for i in range(1, len(digits)):
            newlist = []
            for j in ans:
                for k in ntoc[digits[i]]:
                    newlist.append(j + k)
            ans = copy.copy(newlist)

        return ans
