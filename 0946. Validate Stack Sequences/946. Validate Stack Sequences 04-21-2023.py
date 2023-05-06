# 04-21-2023 Leetcode 946. Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/description/

# I think we can simulate a stack by simply keeping a pointer "stack_top" that
# points to the relative index in pushed. I COULD add something like a hashset or
# dict of val:index to make checking/traversal O(1) but this duplicatest the list.
# Its a tiny list of only 1000 though so maybe I should?

# Algo: look at the next item in popped. 
#If not already pushed:
# push (move idx) until stack_top points at the relative value in pushed. Or rather, the 
# idx before that May need to make a 0th idx. Or just use an offset and admit defeat. Anyhow,
#If Already Pushed then it MUST be the stack top or we cant get to it. return False if not


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [-1]
        pushed_i = 0

        for pop in popped:   
            #cant use negative index on an empty list... obnoxious. 
            #I think we can just put in a dummy value, since we actually dont care about
            #the eventual state of the stack, and it can be leftover at the end          
            while stack[-1] != pop:
                if pushed_i == len(popped):
                    return False
                stack.append(pushed[pushed_i])
                pushed_i += 1
            else: 
                stack.pop()
        
        return True
                    