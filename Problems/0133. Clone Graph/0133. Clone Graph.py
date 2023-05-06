# 04-09-2023 REDO

# 11-27-2022 LeetCode 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/

# While this looks dead simple, I have some questions.
# The "value is the same as the index, uh... I guess if this
# was a list, but its not a list" seems... odd. I guess I have to
# use the value in a "seen" Hashmap, but nothing prevents a node in
# a graph from having the same value AND neighbors as another node,
# but being importantly distinct right? You cant just say "well they
# are the same node" and compress them, if say Number of Nodes was
# an important measure.


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        # ONE PASS WITH DEFAULTDICT:
        if not node:
            return node

        # new_nodes = collections.defaultdict(Node)
        # processed = {node.val}
        # nodes = [node]

        # while nodes:
        #     curr_node = nodes.pop()
        #     new_nodes[curr_node.val].val = curr_node.val
        #     for curr_neighbor in curr_node.neighbors:
        #         new_nodes[curr_node.val].neighbors.append(new_nodes[curr_neighbor.val])
        #         if curr_neighbor.val not in processed:
        #             processed.add(curr_neighbor.val)
        #             nodes.append(curr_neighbor)

        # return new_nodes[node.val]

        # #ONE PASS WITH DICT:
        # if not node:
        #     return node

        # new_nodes = dict()
        # processed = {node.val}
        # nodes = [node]

        # while nodes:
        #     curr_node = nodes.pop()
        #     if curr_node.val not in new_nodes:
        #         new_nodes[curr_node.val] = Node(curr_node.val)
        #     for curr_neighbor in curr_node.neighbors:
        #         if curr_neighbor.val not in new_nodes:
        #             new_nodes[curr_neighbor.val] = Node(curr_neighbor.val)
        #         new_nodes[curr_node.val].neighbors.append(new_nodes[curr_neighbor.val])
        #         if curr_neighbor.val not in processed:
        #             processed.add(curr_neighbor.val)
        #             nodes.append(curr_neighbor)

        # return new_nodes[node.val]

        # TWO PASSES
        # Count total nodes:
        seen = {node.val}
        nodes = [node]
        while nodes:
            curr_node = nodes.pop()
            for neighbor in curr_node.neighbors:
                if neighbor.val not in seen:
                    seen.add(neighbor.val)
                    nodes.append(neighbor)

        # make a list of new nodes, with their indexes being their values. Neighbor lists are blank for now
        new_nodes = [Node(i) for i in range(len(seen) + 1)]
        seen = {node.val}
        nodes = [node]
        # Traverse the existing graph and use the neighbors of curr node to link up nodes and neighbors
        # via index in our new node list
        while nodes:
            curr_node = nodes.pop()
            for curr_neighbor in curr_node.neighbors:
                new_nodes[curr_node.val].neighbors.append(new_nodes[curr_neighbor.val])
                if curr_neighbor.val not in seen:
                    seen.add(curr_neighbor.val)
                    nodes.append(curr_neighbor)

        return new_nodes[1]
