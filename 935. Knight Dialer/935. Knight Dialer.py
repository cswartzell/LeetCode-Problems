# 04-18-2023 Leetcode 935. Knight Dialer
# https://leetcode.com/problems/knight-dialer/description/

# Step 1: Think about it: if the knight starts on a zero, we can tour the board
# ONLY missing 5. There are no valid jumps from 5 thus it can never be included

# So adjacency:
# 0: 4, 6
# 1: 8, 6
# 2: 7, 9
# 3: 8, 4
# 4: 3, 9, 0
# 5: XX
# 6: 7, 1, 0
# 7: 2, 6
# 8: 3, 1
# 9: 2, 4

# So we have at least two choices from any given digit, and possible 3 choices.
# Well shit. You can get the 3 choices by going to zero in between so, 3*2*3


class Solution:
    def knightDialer(self, n: int) -> int:
        # TRICK: We MUST include the single instance of 5 being a valid phone number of len(1)
        if n == 1:
            return 10

        dial_next = {
            0: [4, 6],
            1: [8, 6],
            2: [7, 9],
            3: [8, 4],
            4: [3, 9, 0],
            6: [7, 1, 0],
            7: [2, 6],
            8: [3, 1],
            9: [2, 4],
        }
        dp = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        next_dp = collections.defaultdict(int)
        for _ in range(n - 1):
            if _ == 23:
                pass
            for digit in dp:
                next_dp[digit] = sum(dp[jump] for jump in dial_next[digit]) % (
                    10**9 + 7
                )
            dp = next_dp
            next_dp = collections.defaultdict(int)

        return sum(dp.values()) % (10**9 + 7)
