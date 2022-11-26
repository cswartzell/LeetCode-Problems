# 11-25-2022 LeetCode 622. Design Circular Queue
#https://leetcode.com/problems/design-circular-queue/description/

#I like it when the classes are a little more in-depth rarther than implementing
#like a single spaghetti block function. Feels more real... but what do I know

#pretty straightforward implementation of a ring buffer. Gets a little fiddly
#with the indexing and making sure you arent off by one. I also go hung up for
#a bit as I was trying to use the index positions themselves to note if a 
#queue was full or empty, but if done as I have here, the head and tail
#will both be at the same index in EITHER case, full or empty, with no simple
#way to discern which. Now if you clear out the values or use a sentinel value
#for emptied spaces I suppose youc could check this to distinguish the two states.
#In the end I just opted to track the number of elements IN the buffer instead. 
#In a real implementation, this could allow a quick and easy O(1) len() function
#as well, at the cost of one measly int. Why not ALWAYS have this be the case?

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [-1] * k
        self.head = 0
        self.tail = 0
        self.lenq = 0
        self.qk = k

    def enQueue(self, value: int) -> bool:
        # INSPECTION BLOCK I NEED TO KNOW HOW TO DO THIS
        loc_q, loc_head, loc_tail, loc_k, loc_lenq = (
            self.q,
            self.head,
            self.tail,
            self.qk,
            self.lenq,
        )
        if not self.isFull():
            self.q[self.tail] = value
            self.tail = (self.tail + self.qk + 1) % self.qk
            self.lenq += 1
            return True
        return False

    def deQueue(self) -> bool:
        # INSPECTION BLOCK I NEED TO KNOW HOW TO DO THIS
        loc_q, loc_head, loc_tail, loc_k, loc_lenq = (
            self.q,
            self.head,
            self.tail,
            self.qk,
            self.lenq,
        )
        if not self.isEmpty():
            # clear the space out?
            self.q[self.head] = -1
            self.head = (self.head + 1) % self.qk
            self.lenq -= 1
            return True
        return False

    def Front(self) -> int:
        # INSPECTION BLOCK I NEED TO KNOW HOW TO DO THIS
        loc_q, loc_head, loc_tail, loc_k, loc_lenq = (
            self.q,
            self.head,
            self.tail,
            self.qk,
            self.lenq,
        )
        if not self.isEmpty():
            return self.q[self.head]
        return -1

    def Rear(self) -> int:
        # INSPECTION BLOCK I NEED TO KNOW HOW TO DO THIS
        loc_q, loc_head, loc_tail, loc_k, loc_lenq = (
            self.q,
            self.head,
            self.tail,
            self.qk,
            self.lenq,
        )
        if not self.isEmpty():
            return self.q[(self.tail - 1 + self.qk) % self.qk]
        return -1

    def isEmpty(self) -> bool:
        # INSPECTION BLOCK I NEED TO KNOW HOW TO DO THIS
        loc_q, loc_head, loc_tail, loc_k, loc_lenq = (
            self.q,
            self.head,
            self.tail,
            self.qk,
            self.lenq,
        )
        return self.lenq == 0

    def isFull(self) -> bool:
        # INSPECTION BLOCK I NEED TO KNOW HOW TO DO THIS
        loc_q, loc_head, loc_tail, loc_k, loc_lenq = (
            self.q,
            self.head,
            self.tail,
            self.qk,
            self.lenq,
        )
        return self.lenq == self.qk


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
