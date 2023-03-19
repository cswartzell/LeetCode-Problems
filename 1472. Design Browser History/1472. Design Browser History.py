# 03-18-2023 Leetcode 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/description/


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_pos = 0

    def visit(self, url: str) -> None:

        if self.curr_pos == len(self.history) - 1:
            self.history.append(url)
            self.curr_pos += 1
        else:
            self.history = self.history[: self.curr_pos + 1] + [url]
            self.curr_pos += 1

    def back(self, steps: int) -> str:
        self.curr_pos = max(0, self.curr_pos - steps)
        return self.history[self.curr_pos]

    def forward(self, steps: int) -> str:
        self.curr_pos = min(self.curr_pos + steps, len(self.history) - 1)
        return self.history[self.curr_pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
