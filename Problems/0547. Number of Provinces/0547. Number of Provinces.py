# 05-03-2023 leetcode 0547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/

# Basic UnionFind

class unionfind:
    def __init__(self, n: int):
        self.root = [x for x in range(n)]


    def find(self, x: int) -> int:
        if self.root[x] != x:
            x = self.find(self.root[x])        
        return x

    def union(self, x: int, y: int):
        seeit = self.root
        # rootx, rooty = self.find(x), self.find(y)
        rootx, rooty = self.finalFind(x), self.finalFind(y)
        if rootx != rooty:
            if rootx > rooty:   # I think the order matters. We want to use the LATER roots
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
    
    def finalFind(self, x: int) -> int:
        if self.root[x] != x:
            self.root[x] = self.finalFind(self.root[x])        
        return self.root[x]
    
    def countem(self) -> int:
        seeit = self.root

        for i in range(len(self.root)):
            self.finalFind(i)
        return len(set(self.root))


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = unionfind(len(isConnected))
        for city in range(len(isConnected)):
            for neighbor in range(city+1, len(isConnected[city])):
            # for neighbor in range(len(isConnected[city])):
                if isConnected[city][neighbor]:   # A city is its own neighbor... presumably, and this cateches that case implicitly
                    uf.union(city, neighbor)
        return uf.countem()