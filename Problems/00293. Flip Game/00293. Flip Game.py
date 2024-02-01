# 02-01-2024 Leetcode Weekly 0293. Flip Game
# https://leetcode.com/problems/flip-game/?envType=weekly-question&envId=2024-02-01
# Time: Challenge: 

# Weird. We are given instructios for how a game ends, but are only asked to return all
# possibilites for the first turn. Maybe three are a few of these challenges.
# LOTS of ways to skin this cat. Two pointer. RE. string searches etc.

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        str_arr = list(currentState)
        i = 0
        ans = []
        while i < len(currentState) - 1:
            if currentState[i] == currentState[i+1] == "+":
                # ans.append(currentState[:i] + "--" + currentState[i+2:])

                # A more "appropriate" string builder method. But not really since
                # we need to join which is O(n) anyhow
                str_arr[i], str_arr[i+1] = "-", "-"
                ans.append("".join(str_arr))
                str_arr[i], str_arr[i+1] = "+", "+"
            i += 1
        return ans
