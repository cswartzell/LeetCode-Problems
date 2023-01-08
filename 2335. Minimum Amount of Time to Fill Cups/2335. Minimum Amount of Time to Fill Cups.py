# 01-07-2022 LeetCode 2335. Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/

#THE DUMBEST ANSWER!

#So, min(largest two) + min(smallest) + remaining smallest right?
#No! We want to maximize the number of times we pour two, we dont
#want to be left with a bunch of single pourst at the end.
#take [4,4,5]. Your first guess might be , fill the middle and end 
# for 4 seconds, then the 5th pour and first of the 0 cup, then
# 3 more seconds of cup 0. This can instead be 2 in cup 0 and 2,
# 3 in cup 1 and 5, 1 in cup 0 and 1, then just TWO more in cup 0
# for a total of seven, NOT eight.

#Surely this is basic math but it eludes me... I can obviously create
#some kind of algo that pulls one from each of the two largest stacks
#til there is only one stack left but that seems silly. 

#wow. I feel dumb. I mean... I guess im going to use a max heap and
#pop two, subtract one from each, then push them again?

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # amount.sort()
        # return amount[1] + max(amount[0], amount[2] - amount[1])
        
        seconds = 0

        amount = list(-x for x in amount if x != 0)

        heapq.heapify(amount)
        while len(amount) > 1:
            seconds += 1
            big = -1 * heapq.heappop(amount)
            mid = -1 * heapq.heappop(amount)
            if mid -1 > 0:
                heapq.heappush(amount, -1 * (mid - 1))      
            if big -1 > 0:
                heapq.heappush(amount, -1 * (big - 1))      
            
        return seconds - heapq.heappop(amount) if amount else seconds
       
       