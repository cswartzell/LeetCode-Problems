# 04-21-2023 Leecode https://leetcode.com/problems/best-poker-hand/solutions/
#https://leetcode.com/problems/best-poker-hand/solutions/

#Im going to extend this to all hands. Also, as their is a strict order, 
# Lets use a switch statement

#Order: 
# Royal Flush > Straight Flush > 4 of a Kind > Full House > Flush > Straight > 3 > 2 > High Card

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        #Ace is high for all types of hands EXCEPT a 5 high straight, which acccording to hoyle, is legit
        #lets change all 1s to 14s as ace is high in every other case, and manually check for 5 high straight

        #Of course it doesnt really matter as we arent returning the cards themselves
        
        ranks = [x if x != 1 else 14 for x in ranks]
        hranks = collections.Counter(ranks)
        hsuits = collections.Counter(suits)

        
        flush = len(hsuits) == 1
        royal = sum(ranks) == 60
        straight = royal or sum(ranks) == min(ranks)*5 + 10 or set(ranks) == {14,2,3,4,5}
        counts = sorted(hranks.values())

        # if royal and flush:
        #     return "Royal Flush"
        # if straight and flush:
        #     return "Straight Flush"
        # if counts[-1] == 4:
        #     return "Four of a Kind"
        # if counts[0] == 2 and counts[1] == 3:
        #     return "Full House"
        if flush:
            return "Flush"
        # if straight:
        #     return "Straight"
        # if counts[-1] == 3:
        if counts[-1] > 2:
            return "Three of a Kind"
        if counts[-1] == 2:
            return "Pair"
        else: 
            return "High Card" 