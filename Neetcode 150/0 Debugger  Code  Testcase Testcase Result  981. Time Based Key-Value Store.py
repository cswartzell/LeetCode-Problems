# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/description/
# Time: 20 mins

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.d_time = defaultdict(list)
        self.d_vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d_time[key].append(timestamp)
        self.d_vals[key].append(value)

    def get(self, key: str, timestamp: int):
        # if len(self.d_vals[key]) == 0:
        #     return ""
        # idx = min(bisect.bisect_left(self.d_time[key], timestamp), len(self.d_time[key]) - 1)
        # if self.d_time[key][idx] > timestamp:
        #     idx = max(idx-1, 0)
        # if idx == 0 and timestamp < self.d_time[key][0]:
        #     return ""
        # return self.d_vals[key][idx] 
        # if len(self.d_vals[key]) == 0:
        #     return ""
        idx = bisect.bisect_right(self.d_time[key], timestamp)
        if idx == 0 :
            return ""
        return self.d_vals[key][idx - 1] 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)