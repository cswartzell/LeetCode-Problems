# 11-25-2022 LeetCode 346. Moving Average from Data Stream
# https://leetcode.com/problems/moving-average-from-data-stream/description/

# Extremely straightforward implementation of a sum of a queue

import queue


class MovingAverage:
    def __init__(self, size: int):
        # Python Queue DOES take a max size, but throws and exception if exceeded)
        # Also, an obnoxious format to call
        self.winder = queue.Queue()
        self.eles = 0
        self.size = size
        self.curr_sum = 0

    def next(self, val: int) -> float:
        if self.eles == self.size:
            self.curr_sum -= self.winder.get()
            self.eles -= 1
        self.winder.put(val)
        self.curr_sum += val
        self.eles += 1
        return self.curr_sum / self.eles


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
