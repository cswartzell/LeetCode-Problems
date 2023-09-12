# 09-12-2023 Neetcode 155. Min Stack
# https://leetcode.com/problems/min-stack/description/
# Time: 25mins


# What? How do we maintain a minimum in O(1) time?! I could do
# O(log n) by pushing to heap on push, and popping on pop... but
# how to do better?!

class MinStack:
    def __init__( self ):
        self.stack_len = 0
        self.stack = []
    
    def push( self, val: int ):
        if self.stack_len == 0 or self.stack[self.stack_len - 1][1] > val:
            _min = val
        else:
            _min = self.stack[self.stack_len - 1][1]
        self.stack.append((val, _min))
        self.stack_len += 1
   
    def pop( self ) -> int:
        # How to remove a val in O(1) WITHOUT just using pop to invent pop?
        # is del an O(1) operation? Slicing ISNT. It looks like del is
        temp = self.stack[self.stack_len - 1]
        del self.stack[self.stack_len - 1]
        self.stack_len -= 1
        return temp[0]
    
    def top( self ) -> int:
        return self.stack[self.stack_len - 1][0]

    def getMin( self ) -> int:
        return self.stack[self.stack_len - 1][1]
