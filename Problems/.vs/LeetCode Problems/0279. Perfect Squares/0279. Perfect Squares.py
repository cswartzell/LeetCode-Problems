#11-21-2022 LeetCode 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/



class Solution:
    def numSquares(self, n: int) -> int:
        squares = [x**2 for x in range(1, min(101, math.ceil(math.sqrt(n))+1))]

        zdp = [10**5] * (n+1)
        zdp[0] = 0
        zdp[1] = 1

        def find_sum(a:int):
            # Already solved this
            if zdp[a] != 10**5:
                return zdp[a]

            min_sum = 10**5
            lgst_sqr_idx = bisect.bisect_left(squares, a)
            if lgst_sqr_idx == len(squares) or squares[lgst_sqr_idx] > a: 
                lgst_sqr_idx -= 1
            for sqr_idx in range(lgst_sqr_idx, -1, -1):
                min_sum = min(min_sum, 1 + find_sum(a - squares[sqr_idx]))
            
            zdp[a] = min_sum
            return zdp[a]

        for a in range(2, n + 1):
            zdp[a] = find_sum(a)

        return zdp[n]

#Interesting. A compositions thing. Noting first that 
#n is max 1000, so thats only a handful of perfect squares
#to search from. Hell, we could even precompute the sums
#of x copies of the ith square through 10000 directly, so
#there is less multiplication. 

#This point I am a little stuck. Thats... a lot of combinations
#we could run through. 

#Oh, note that there is ALWAYS a combination of n copies of 1**2,
#which is just n. So much so that we can remove it from the list?
#This ALSO means ANY perfect square less than n CAN be included in 
#some sum, as we can always fill out the remainder with at least 1's.

#Ok. Given this, can we just start with the largest square below n,
#subtract it and repeat to get our starting point. Its almost like leaving
#behind j pointers...

#hmm, the biggest gulf between numbers is 61 (between 900-961). We can 
#quickly reduce these gaps by precomputing some inbetweeners. For instance
# the gap between 841-900 is bisected by 441*2 = 882, cutting the gap
#from 59 down to 41.   

#ONCE AGAIN I've had to look this up. Getting pretty frustrated.
#This is a DP question, and I started to build a chart to try to figure it out
#Its very akin to the change making problem, noting if we build UP from a 
#base case of zero, and check the current index of our dp array, we can
#either add a ONE to the last result, or if a "larger" coin would fit,
#add one to the value for the current index minus this larger "coin". If
#TWO coppies of said larger coin could be used to get closer, then the
#current index will be somewhat after the index of the sum OF the two coins,
#which would be one higher than the value of the single coin...
#It IS straightforwad DP, but tricky to note what the base case is. We need
#to check the current index value agains ALL "coins" that are equal to or
#less than the current value/index

#There are some AWESOME better answers after this, including math based theories
#showing its NEVER more than 4, and there are formulas that can kind of tell you
#if its 3, assuming its not 1 or two. 1 is easy. Is it Two? No way to know but
#to check. 

#That being said, I'd never be able to remember or explain those on the fly.
#Better to try for the DP solution. Having seen it, Ill now just attempt to
#recreate it blind as a basic reinforcement challenge. I was MAYBE getting
#somewhere with noting we could just subtract the last largest square and use
#a precomputed table for the sum of composites for THAT number. I just "forgot"
#that you must do this starting from the bottom. I then DID exactly that, by
#listing in excel the composites, but I didnt note the similarity to the 
#coin proiblem and missed the fundamental step of what we were comparing. 


# class Solution:
#     def numSquares(self, n: int) -> int:
#       # list of square numbers that are less than `n`
#         square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
#         level = 0
#         queue = {n}
#         while queue:
#             level += 1
#             #! Important: use set() instead of list() to eliminate the redundancy,
#             # which would even provide a 5-times speedup, 200ms vs. 1000ms.
#             next_queue = set()
#             # construct the queue for the next level
#             for remainder in queuet
#                 for square_num in square_nums:    
#                     if remainder == square_num:
#                         return level  # find the node!
#                     elif remainder < square_num:
#                         break
#                     else:
#                         next_queue.add(remainder - square_num)
#             queue = next_queue
#         return level