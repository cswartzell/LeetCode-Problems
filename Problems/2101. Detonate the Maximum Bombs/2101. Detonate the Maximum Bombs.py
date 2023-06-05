# 05-03-2023 Leetcode 2101. Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/submissions/

# UnionFind? Or at least DP. Its interesting because they can overlap
# one another, but dont HAVE to.

# Equation for a circle r**2 = (x-x1)**2 + (y-y1)**2
# So another bomb B is in range of bomb A if sqrt( (Ax-Bx)**2 + (Ay-By)**2 ) <= Ar
# So its union find, and we can just do a nested iterator, and only call union if the
# Above is true. NOTE the relationship is NOT reciprocal. Just because A can detonate B
# does NOT mean B can detonate A!

#BAH! its not Acyclical. Meaning you cant memoize. You Seem to need to check each starting point.
# I wasted so much time failing to remmember this




class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        canReach = collections.defaultdict(set)
        # edges = []

        for bombA in range(len(bombs)):
            for bombB in range(len(bombs)): #Must check ALL as the relationship isnt reciprocal
                if sqrt( (bombs[bombA][0]-bombs[bombB][0])**2 + (bombs[bombA][1]-bombs[bombB][1])**2 ) <= bombs[bombA][2]: #This CORRECTLY adds "bomb A can detonate bomb A"
                    canReach[bombA].add(bombB)
        
        maxChain = 0
        for bombA in range(len(bombs)): 
            visited = {bombA}
            stack = [bombA]

            while stack:
                currBomb = stack.pop()
                for nextBomb in canReach[currBomb]:
                    if nextBomb not in visited:
                        visited.add(nextBomb)
                        stack.append(nextBomb)
            maxChain = max(maxChain, len(visited))

        return maxChain

