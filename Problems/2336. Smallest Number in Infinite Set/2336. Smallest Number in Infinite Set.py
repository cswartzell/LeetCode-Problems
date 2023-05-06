# 04-18-2023 Leetcode 2336. Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/description/


class SmallestInfiniteSet:
    def __init__(self):
        self.inf_counter = 0
        self.back_heap = []
        self.missing_nos = set()

    def popSmallest(self) -> int:
        if not self.back_heap:
            self.inf_counter += 1
            smallest = self.inf_counter
        else:
            smallest = heapq.heappop(self.back_heap)

        self.missing_nos.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.missing_nos:
            self.missing_nos.remove(num)
            if not self.missing_nos:
                self.inf_counter = 0
            else:
                heapq.heappush(self.back_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
