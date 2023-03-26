# 03-25-2023 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/

# WITHOUT UNION BY RANK IT TLEs. Which frankly sucks. 

# So this is definitely just union find. 
# Do quick find to set EVERY nodes parent to 
# Be the root, then just count the number of roots

class du:
    def __init__(self, n:int):
        self.du = [x for x in range(n)]
        self.size = [1] * n
    #Quickfind, recursively finds AND SETS all parents to root of component
    def find(self, x) -> int:
        if self.du[x] == x:
            return x
        
        self.du[x] = self.find(self.du[x])
        return self.du[x]


    def dunion(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            #I keep missing this step. You CANNOT arbitrarily set one to the other, there has 
            #to be some metric to pick correctly or you create false components. 
            
            #AH. Remember, for quick union you dont assign the root of one to the other, Just the
            #PARENT of one to the other.

            #AAAAAAND TLE. You have to optimize union by rank or size. Obnoxious

            # self.du[root_y] = self.du[root_x]

            if self.size[root_x] > self.size[root_y]:
                self.du[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.size[root_y] = 0
            else:
                self.du[root_x] = root_y
                self.size[root_y] += self.size[root_x]
                self.size[root_x] = 0


    def count_roots(self):
        see_du = self.du
        see_size = self.size
        # for i in range(len(self.du)):
        #     self.find(i)
        # roots_count = list(collections.Counter(self.du).values())
        
        #Now for some very basic combinatorics... which escapes me at present
        #Its every combination of pairs where each node in a pair is from 
        #a different set. 

        #I THINK I can do it with a nested for: sum of products as you slide along?
        #There has to be a simpler way but I think this works:
        #per the example 2, we have a group of [1,2,4] and the total is
        # 1x2 + 1x4 + 2x4. 
        # ans = 0
        # # for  i in range(len(roots_count)):
        #     for  j in range(i + 1, len(roots_count)):
        #         ans += roots_count[i] * roots_count[j]            
        # return ans

        unreachable = 0
        total_nodes = 0

        for x in self.size:
            unreachable += total_nodes * x
            total_nodes += x
        return unreachable

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Set the PARENT of each node to itself. 
        union = du(n)

        for x, y in edges:
            union.dunion(x, y)

        return union.count_roots()

