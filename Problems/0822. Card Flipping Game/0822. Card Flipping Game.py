# 06-19-2023 Leetcode 822. Card Flipping Game
# https://leetcode.com/problems/card-flipping-game/description/

# Weirdly phrased but this seems like a set based thing... but with a twist
# Imagine we have 3 cards with backs [2,2,2]. To be "Good" we need NONE of these
# to face 

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int: 
        # cants = set()
        # for i in range(len(fronts)):
        #     if fronts[i] == backs[i]:
        #         cants.add(fronts[i])
        
        # bads = set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i] )
        # goods = set(fronts + backs) - bads

        # return min(goods) if goods else 0 
        
        
        # bads = set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i] )
        # goods = set(fronts + backs) - bads

        return min(goods) if  ( goods := set(fronts + backs) - set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]) ) else 0 