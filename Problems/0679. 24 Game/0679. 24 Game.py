# 03-05-2024 Leetcode 0679. 24 Game
# https://leetcode.com/problems/24-game/
# Time: 90=180 minutes off and on, Challenge: 8/10

# I wonder if we could create an exhaustive list of ways to get to 24. Probably not
# by hand and thats not the answer. There are 4**4 potential hands, 256 hands. Very 
# few. 1,1,1,1 is right out. 

# Given a hand, how many posibilities are there? Think about listing it in RP:
# I think its just (4*4*4*4) for cards, and (4*4*4) for operations. Thats only
# 16,384. Fairly calculable? Oh, easier, its without repalacement. Its just 4! = 24 
# arrangements of cards, still 4^3 =64 ops. Thats 24*64= 1536 possible statements to
# evaluate. Trivial. Whatch for div by zero!  

#We have to keep pemdas in mind... Oh, and division by zero

# Adding and subtracting are never enough. We must perform at least one multiplicateion,
# but as the example shows, this could include division by a fraction: 4/(1/3)*2

# Bah... I dont want to write a calculator. Python has an Evaluate funciton we could lean on
# does it take RP?

# Its not even that simple: we have to take grouping in mind: (8-4) * (7-1) is different than (8-(4*7)-1)
# In RP this is the difference between (8 4 - 7 1 - *) and (8 4 7 * - 1 -), so we have to evalutate WHERE
# to place the ops too. This makes it slightly more complicated. For RP we MUST have 2 numbers first, then
# it could be an op or a number in SOME orders after that:
# nnooo, nonoo, noono, onnoo, onono 
# I think the above combo is exhaustive: we must have at least one more num than op, reading left to right
# To be clear, evaluating in RP, we now have 4! num permutations with 4^3 choices of ops, and 5 ways 
# to distribute them. Thats 4!*4^3*5 = 14*64*5 = 7680 statements to evaluate. We can stop once we find
# ONE that == 24 though. Processing them all still seems *fairly* trivial. Ugh, I am going to have to write
# the stupid RP calc arent I?

# Ok, first step: it must contain at least a 3 or 4. 2*2*2*2 is only 16. it DOESNT have to have 
# a 4 though, 3+3 * 2 * 2 = 4



class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def num_permutations(n, A):
            if n == 1: yield A
            else:
                for i in range(n-1):
                    for hp in num_permutations(n-1, A): 
                        yield hp
                    j = 0 if (n % 2) == 1 else i
                    A[j],A[n-1] = A[n-1],A[j]
                for hp in num_permutations(n-1, A): 
                    yield hp

        op_permutations = []
        ops = {"+", "-", "/", "*"}
        for X in ops:
            for Y in ops:
                for Z in ops:
                    op_permutations.append([X, Y, Z])


        def RP_eval(exp):
            stack = []
            for i in range(len(exp)):
                if exp[i] in ops:
                    op = exp[i]
                    B = stack.pop()
                    A = stack.pop()
                    if op == "+":
                        stack.append(A+B)
                    elif op == "-":
                        stack.append(A-B)
                    elif op == "*":
                        stack.append(A*B)
                    elif op == "/" and B != 0:
                        stack.append(A/B)
                    else:
                        return 0
                else:
                    stack.append(exp[i])
            return stack[0]

        for np in num_permutations(len(cards), cards):
            for op in op_permutations:
                if np == [8,3,8,3] and op == ["/","-","/"]:
                    pass
                # NNNNOOO
                exp1 = [np[0],np[1],np[2],np[3],op[0],op[1],op[2]]
                # NNNONOO
                exp2 = [np[0],np[1],np[2],op[0],np[3],op[1],op[2]]
                # NNNOONO
                exp3 = [np[0],np[1],np[2],op[0],op[1],np[3],op[2]]
                # NNONNOO
                exp4 = [np[0],np[1],op[0],np[2],np[3],op[1],op[2]]
                # NNONONO
                exp5 = [np[0],np[1],op[0],np[2],op[1],np[3],op[2]]
                
                for exp in [exp1, exp2, exp3, exp4, exp5]:
                    test = RP_eval(exp) - 24 
                    if abs(RP_eval(exp) - 24) < 0.001:
                        return True

        return False


        #get permutations using INCORRECT Heap's Method:
        # def heap_it(cards, n, holder):
        #     if n == 1:
        #         holder.append([*cards])
        #         return
        #     for i in range(n):
        #         heap_it(cards, n-1, holder)
        #         if i < n-1:            
        #             if i&1:
        #                 cards[0], cards[n-1] = cards[n-1], cards[0]
        #             else:
        #                 cards[i], cards[n-1] = cards[n-1], cards[i]
        # num_permutations = []
        # heap_it(cards, 4, num_permutations)
        
        # for np in num_permutations:
        #     for op in op_permutations:
        #         exp = [np[0],op[0],np[1],op[1],np[2],op[2],np[3]]
        #         if eval("".join(exp)) == 24:
        #             return True
