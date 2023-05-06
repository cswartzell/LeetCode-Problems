# 11-25-2022 LeetCode 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/description/

# Other than the barage of self. another easy implementation of a standard


class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [-1] * k
        self.head = 0
        self.tail = 0
        self.lenq = 0
        self.qk = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q[self.tail] = value
            self.tail = (self.tail + self.qk + 1) % self.qk
            self.lenq += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            # clear the space out?
            self.q[self.head] = -1
            self.head = (self.head + 1) % self.qk
            self.lenq -= 1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.q[self.head]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.q[(self.tail - 1 + self.qk) % self.qk]
        return -1

    def isEmpty(self) -> bool:
        return self.lenq == 0

    def isFull(self) -> bool:
        return self.lenq == self.qk


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
