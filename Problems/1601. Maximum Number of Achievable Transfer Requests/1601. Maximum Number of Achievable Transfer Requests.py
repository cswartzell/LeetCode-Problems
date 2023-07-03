# 07-02-2023 1601. Maximum Number of Achievable Transfer Requests
# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/

# Observations:
# A transfer is a transfer. We only care about max,does it matter
# whom starts a chain? Imagine there is a ring of like 30 transfers so each
# Building has 1 in and one out. The first building only has a second request
# to go to a building outside the ring that has a person that wants to go to the 
# original building. We would then be able to do both things. hmm. 
# I THINK we can be a bit greedy but im not sure. Every edge is a request
# and so none are exclusive. 

# Pretty clearly each building is going to have ins and outs, and can only 
# transfer the minimum of those two (At best, not guarenteed). 

# I think this is startingh to look like a unionfind thing. Or really its
# cycles. In order to have a guy leave, another guy must replace him. The
# only way for that to happen is a closed ring. I think we want to find all
# such cycles and process them from largest to smallest. Or does processing
# matter? 

#Is there a scenario that works thats not a closed cycle? I dont think so. 

# I think the answer is simply the sum of the lengths of all cycles. 

# So each building is dicitonary entry, and its data is a Counter. Each
# counter entry is the number of employees that want to going to building
# X. Or we could just do a list for each request. We start a chain (list)
# from any random building. This is a DFS. There are only two outcomes:

# A) there is no cycle. The chain deadends. On any deadend, backtrack
# deleting the last request. If there are different choices, proceed.

# B) There is a cycle SOMEWHERE on the chain. Doesnt have to be the whole
# chain. Backtrack from this last node that joins the cycle deleting AND
# COUNTING requests til we get back to the first copy of it. This will
# count the cycle. Proceed. 

# This should delete all dead ends and count all cycles for a given chain.
# As we are removing deadends, we are processing each request only once, ever.
# Not bad. 

# Well shoot. Order matters. You DO want to do bigger cycles before smaller. 
# Damn. I have to then find EVERY cycle first, then start processing?

# We may be able to go further and eliminate huge swaths of work: Say a building
# has 1000 out requests, but one in request. If we FIND a cycle that we DO
# process that includes hits node, then its one in request is fulfilled. As
# it has no further ins, no further outs are possible. We can remove the node
# entirely. 

# DO NOTE that people can request to transfer to the building they are in
# and this COUNTS as a transfer for some stupid reason. When we are doing
# our adjacency graph, count these and dont add them. 



#I think I am just going to have to look at the answer: And damn... 0/1
#knapsack. DO consider every request.

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.max_transfers = 0
        self.buildings_net = [0 for _ in range(n)]
        
        def transfer(request: int, transfers_granted: int):
            # check if chain valid
            if request == len(requests):
                if any(self.buildings_net):
                    return 
                self.max_transfers = max(self.max_transfers, transfers_granted)
                return
            #grant request x and move on
            self.buildings_net[requests[request][0]] -= 1
            self.buildings_net[requests[request][1]] += 1
            transfer(request + 1, transfers_granted + 1)

            #Deny request (backtrack) and move on
            self.buildings_net[requests[request][0]] += 1
            self.buildings_net[requests[request][1]] -= 1     
            transfer(request + 1, transfers_granted)

        transfer(0,0)
        return self.max_transfers



















        # self.max_transfers = 0
        # self.buildings_net = [0 for _ in range(n)]
        # # self.nonzero_buildings = 0
        # self.nonzero_buildings = set()


        # def transfer(request: int, transfers_granted: int):
        #     # check if chain valid
        #     if request == len(requests):
        #         #for x in self.buildings_net:
        #         #   if x == 0:
        #         #       continue
        #         # if self.nonzero_buildings == 0:
        #         if not self.nonzero_buildings:
        #             self.max_transfers = max(self.max_transfers, transfers_granted)
        #         return 

        #     #grant request x and move on
        #     # if requests[request][0] != requests[request][1]:
        #     #     if self.buildings_net[requests[request][0]] == 0:
        #     #         self.nonzero_buildings += 1
        #     #     elif self.buildings_net[requests[request][0]] == 1:
        #     #         self.nonzero_buildings -= 1
        #     #     if self.buildings_net[requests[request][1]] == 0:
        #     #         self.nonzero_buildings += 1
        #     #     elif self.buildings_net[requests[request][1]] == -1:
        #     #         self.nonzero_buildings -= 1

        #     self.buildings_net[requests[request][0]] -= 1
        #     self.buildings_net[requests[request][1]] += 1
            
        #     if self.buildings_net[requests[request][0]] == 0 and requests[request][0] in self.nonzero_buildings:
        #         self.nonzero_buildings.remove(requests[request][0])
        #     else:
        #         self.nonzero_buildings.add(requests[request][0])
        #     if self.buildings_net[requests[request][1]] == 0 and requests[request][1] in self.nonzero_buildings:
        #         self.nonzero_buildings.remove(requests[request][1])
        #     else:
        #         self.nonzero_buildings.add(requests[request][1])

        #     transfer(request + 1, transfers_granted + 1)

        #     #Deny request (backtrack) and move on
        #     # if requests[request][0] != requests[request][1]:
        #     #     if self.buildings_net[requests[request][1]] == 0:
        #     #         self.nonzero_buildings += 1
        #     #     elif self.buildings_net[requests[request][1]] == 1:
        #     #         self.nonzero_buildings -= 1
        #     #     if self.buildings_net[requests[request][0]] == 0:
        #     #         self.nonzero_buildings += 1
        #     #     elif self.buildings_net[requests[request][0]] == -1:
        #     #         self.nonzero_buildings -= 1

        #     self.buildings_net[requests[request][0]] += 1
        #     self.buildings_net[requests[request][1]] -= 1
            
        #     if self.buildings_net[requests[request][0]] == 0 and requests[request][0] in self.nonzero_buildings:
        #         self.nonzero_buildings.remove(requests[request][0])
        #     else:
        #         self.nonzero_buildings.add(requests[request][0])
        #     if self.buildings_net[requests[request][1]] == 0 and requests[request][1] in self.nonzero_buildings:
        #         self.nonzero_buildings.remove(requests[request][1])
        #     else:
        #         self.nonzero_buildings.add(requests[request][1])

        #     transfer(request + 1, transfers_granted)

        # transfer(0,0)
        # return self.max_transfers