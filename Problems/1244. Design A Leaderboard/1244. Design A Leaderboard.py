# 07-07-2023 Leetcode 1244. Design A Leaderboard
# https://leetcode.com/problems/design-a-leaderboard/description/

# Hmm... I guess I could keep a separate heap for the scoreboard?
# But then updating it is hard. Just heapify the values when called?


class Leaderboard:

    def __init__(self):
        self.leaderboard = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.leaderboard[playerId] += score    

    def top(self, K: int) -> int:
        if self.leaderboard:
            top_k = sorted(list(self.leaderboard.values()), reverse=True)
            return sum(top_k[:min(K, len(top_k))])
        else:
            return 0

    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)