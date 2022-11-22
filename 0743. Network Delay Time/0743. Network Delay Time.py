from collections import defaultdict
import heapq

# well this is a basic directed graph question. 
# WITHOUT having studied this at all in Python, I'd start 
# by making the graph with a dict: the nodeID would be the key,
# and the val would be a list of tuples of (connected, send_time).
# We could add a thid val to this tuple, or create a copy of the dict,
# that tracks the current time to reach each node with a signal propogated
# from the given origin spot. Note, a signal may reach a node repeatedly, 
# so we only store the minimum. I guess each time we send a signal to a node
# that has not previously received it, we put its outputs on the stack to check
# if THEYVE all gotten it. Thus our signal is propogated. We could then iterate
# through our graph dict and look that A) all nodes are hit, and if so B) Max 
# time for sent signal (its additive as we store it). OR we could have created 
# a set of just the key nodes, and each time we reach one remove it from this set:
# if the set is non-empty by the time we stop propogating then we know our signal
# failed to reach all nodes. This is a tradeoff of time and space

# Likewise, we could have just kept a running MAX_TIME
# val as we propogate the signal, rather than traversing the list
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Do we need to check for a base case? It looks like there could be just one
        # node, but then there is at least one time. How could there be a time from one node to
        # no other nodes? I guess it points to itself. So the initial send of the first signal 
        # DOESNT count as the first node receiving the signal? No self refernce edges... Constraints
        # are self contradictory and impossible to all be true at once... reported. 
        
        # graph = dict(x:[(y,z,0]) for x something something...) There may be a cool-ass generator but its beyond me
        
        # Build graph in dict and track all nodes.  
        # Almost certainly could be one thing, but I confused myself into claiming this made more sense
        graph = dict()
        node_times = dict()
        for x,y,z in times:
            if x not in node_times:
                node_times[x] = 6001 # could save MAXTIME, set to MAXTIME + 1
            if y not in node_times:
                node_times[y] = 6001  # to eliminate magic numbers    
            if x not in graph:
                graph[x] = [(y,z)]
            else:
                graph[x] += [(y,z)]
        visited = set([k])
        all_nodes = set(x+1 for x in range(n)) 
        # We CAN stop once we've seen all nodes as we are getting there fastest
        # No, we cant. We can stop adding things to the queue... sort of. 
        
        node_times[k] = 0
        stack = [k]
        # heapq.heapify(stack) 
        # This does nothing right? A heap is just a particularly ordered list in this case,
        # but an empty or trivial 1 element list is already a heap, its not like it denotes it
        # to be one. Its not a datatype, or structure, but a way of sorting one. As long as only
        
        while stack: # and visited != all_nodes:
            source = heappop(stack) #POP MIN PRIORITY QUEUE
            if source in graph:
                for target, cost in graph[source]:
                    if  node_times[source] + cost < node_times[target]:
                        visited.add(target)
                        node_times[target] = node_times[source] + cost
                        heappush(stack, target) #Push PRIORITY QUEUE VERSION
        
        return max(node_times.values()) if visited == all_nodes else -1








# While close, there is a fatal flaw here. I was capturing and eliminating
# visited nodes and saving the time for the FIRST signal to arrive there... but
# not the first signal in a time sense, only in an order traversal sense. The visited
# node may be directly linked to the root, but by a slow edge. It could be the signal 
# reaches this node after passing through dozens of others before that first edge signal
# arrives. We NEED to process the signals in speed order, not depth order. THIS is an excellent
# example for using a priority queue. Work throug the queue processing and inserting traversals
# by actual speed (curr_time + transit_time) is how to best simulate the process and efficiently
# track the structure. We can still keep a list of visited nodes, and use that to know when to stop
# processing early, but it as we are now checking "in real time", if we hit all the nodes we now know
# that the fastest paths were used to visit them all. Ties are friendly and do not need to be processed

#         # Build graph in dict and track all nodes.         
#         graph = dict()
#         visitednodes = dict()
#         for x,y,z in times:
#             visitednodes[x] = 0
#             visitednodes[y] = 0
#             if x not in graph:
#                 graph[x] = [(y,z)]
#             else:
#                 graph[x] += [(y,z)]
                
#         max_time = 0 
        
#         def send_sig(curr_node, curr_time):
#             if unvisitednodes:
#                 if curr_node in graph:
#                     for y,z in graph[curr_node]:
#                         if y in unvisitednodes:
#                             unvisitednodes.remove(y)
#                             send_sig(y, curr_time+z)
#                             max_time = max(max_time, curr_time)
                    
#         unvisitednodes.remove(k)
#         send_sig(k, 0)
        
#         return max_time if not visitednodes else -1
