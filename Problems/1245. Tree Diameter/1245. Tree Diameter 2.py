# 02-25-2024 Leetcode 1245. Tree Diameter
# https://leetcode.com/problems/tree-diameter/?envType=weekly-question&envId=2024-02-22
# Time: 25 Challenge: 4/10

# Apparently my last submission didnt solve this. I didnt read it, just hit resubmit.
# Good. I have a recollection of how to solve this I think: I dont remember if thats from
# the solution page for this or something similar.

# First note we dont know what the root of the tree is, or rather, it doesnt have one. 
# You can imagine picking any node up and the edgess will all "dangle" from there. 
# The naive solution is to BFS from every node. I suspect what I tried was to dijkstras
# from everynode? You cant dijkstra a longest path. That just ends up being a full BFS.

# The key is to recognize this is a tree: no loops. That means there are leaf nodes. 
# Leaf nodes have a path length beyond them of 0. The parent of the leaf node has a path
# of just one on this leg. Its other leg may be longer, but is also finite. Therefore, we
# count outdegree and start deleting leaf nodes, passing their counts to their parents.
# Their parents then store the max len of its left and right legs and eventually get deleted
# themselves. Eventually we'll get to a center node and the sum of its left and right paths
# will be the answer. Note, there may be more than one and they OUGHT to be equivalent, so 
# it doesnt matter: imagine 4 nodes in a line. Both center nodes have one path len of 1 
# and the other of 2. Both have a sum of 3. 

# NOTE: We are setting a parents leg_len to the max of its existing len (0 if this is the 
# first leg checked, potentially the other leg though). As such, we cant get to the final 
# node and use the same procedure. We need the total of BOTH legs for the final node. We'd 
# need to track it. Instead, we can just get to the final TWO nodes. 
# It is interesting to note that there WILL be a final two. As a tree, there must be when
# deleting nodes one by one. These MUST be adjacent,
# with a single node between them. We can thus just add together both nodes leg lengths as
# those lengths represent the now deleted subtrees. Add one, and return.

# The problem doesnt explicitly say the graph is connnected, but I think it is by definition
# as its a tree right?

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0

        edge_count = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        longest_leg_len = collections.defaultdict(int)
        num_nodes = len(edges) + 1

        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
        for a in neighbors:
            edge_count[len(neighbors[a])].add(a)

            curr_node = edge_count[1].pop()
            parent = neighbors[curr_node].pop() # Only neighbor will be curr_nodes parent
            # del neighbors[curr_node] # Bother to tidy up?
            longest_leg_len[parent] = max(longest_leg_len[parent], longest_leg_len[curr_node] + 1)
            edge_count[len(neighbors[parent])].remove(parent)
            neighbors[parent].remove(curr_node)
            edge_count[len(neighbors[parent])].add(parent)
            num_nodes -= 1

        # Christ is this an ugly line. 
        return longest_leg_len[edge_count[1].pop()] + longest_leg_len[edge_count[1].pop()] + 1            



    # 03-26-2023 Leetcode 1245. Tree Diameter
    # https://leetcode.com/problems/tree-diameter/description/

    #So for a tree, obviously the longest route is going to start at a leaf,
    # run up to the root, then down to another leaf. Seems kinda obvious that
    # this would just be the two deepest leaves, by heights. So lets just
    # sotre the height of the leaves after a DFS and return the sum of the largets two

    #Oh, we arent given a root. Just a undirected graph. Thats actually an interesting 
    #on its own. "Locate the root of a tree given just undirected graph edges". Is it possible?
    #No, all roots are valid, its just a matter or where you origami it. Assuming its acyclical

    #Recursive DFS because I am weaker on that, and generally opt for iterative BFS
    #EXNAY

    #Ok, what about DP: start a dp array with "0" for every n, this is the 
    #longest time it took to get to that node. Every node takes zero time to get 
    #to. Then we BFS from EVERY node, adding one each time we visit an adjacent node.
    # If the existing DP time is larger than the current path we stop. 
    # Return the longest time in the DP array. Its the same solution as the 
    # "longest cycle in a DAG" problem


    #Oh. BFS wins again. Start ANYWHERE. The last node in a complete BFS is guarenteed to
    #be at one of the extreme depths (ALL nodes in that depth are). Then just use ANY
    # one of those and BFS AGAIN. Same thing: now the OTHER extreme nodes will be the 
    # final row of nodes in the BFS. This time just count
    # class Solution:
    #     def treeDiameter(self, edges: List[List[int]]) -> int:
    #         adj_map = collections.defaultdict(list)
    #         for x, y in edges:
    #             adj_map[x].append(y)
    #             adj_map[y].append(x)

    #         def BFS_Distance(node):
    #             curr_row = None
    #             next_row = [node]
    #             visted = set()
    #             distance = -1
    #             extreme_node = None
    #             while next_row:
    #                 curr_row = next_row
    #                 next_row = []
    #                 distance += 1
    #                 while curr_row:
    #                     curr_node = curr_row.pop()
    #                     visted.add(curr_node)
    #                     for next_node in adj_map[curr_node]:
    #                         if next_node not in visted:
    #                             next_row.append(next_node)
    #                             extreme_node = next_node
                    
    #             return extreme_node, distance

    #         extreme_node_1, _ = BFS_Distance(0)
    #         extreme_node_2, diameter = BFS_Distance(extreme_node_1)

    #         return diameter






            #None of this works because you cant just check the existing DP map. You need
            #to true BFS every node if you cant identify the extreme length nodes. 
            #But you CAN identify them, and its brilliant and Im mad i didnt think of it

            # n = range(len(edges) + 1)
            # dp = [0 for _ in n]

            # adj_map = collections.defaultdict(list)
            # for x, y in edges:
            #     adj_map[x].append(y)
            #     adj_map[y].append(x)

            # #Now we could declare diameter = 0 here and write an extra if in the loop
            # #so it gets updated as we discover larger and larger routes. This is LESS efficient
            # #then just doing a linear scan at the end though. A linear scan is one IF for n more nodes
            # #but our loop is n at BEST. maybe n**2. best to save it til later

            # for x in n:
            #     stack = [x]
            #     currr_steps = 0  
            #     visited = set()
            #     while stack:
            #         curr_node = stack.pop()
            #         visited.add(curr_node)
            #         currr_steps += 1
            #         for y in adj_map[curr_node]:
            #             if y not in visited and dp[y] <= currr_steps:
            #                 dp[y] = currr_steps
            #                 stack.append(y)

            # return max(dp)