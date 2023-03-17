# 03-16-2023 Leetcode 2192. All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

# Ok, so as with all graph problems, step 1 is to make an dict of edges.

# Also, man I really just need to memorize how union find is implmenetd. I get
# the concept, but have faield to recreate it several times. Pretty sure this can
# simply be solved as union find

# Interesting. In an acyclical graph there HAS to be at least one node in any path
# that is a root; as in it has no ancestors. It seems trivial but may be important.
# If every node had an ancestor, than it would conain a cycle. The graph can contain
# MORE than one of these of course.

# the problem DIDNT state than there ARENT isolated nodes that lack any edges.
# We can ignore these however, they arent their own ancestors, dont contribute,
# and dont throw off the above conclusion.

# Can we locate these root nodes, process them in BFS, add to ancestor set as we go,
# and be done? I sure as heck cant rigorously prove it, but i suspect so.
# Every child must have a parent. Each of these parents CAN be children too, but
# as the graph is acyclical, there MUST be a progenerator. Therefore, if we ONLY
# start with the progenerators, we should cover every route to every child.

# I think we should then BFS from the progenorators.
# No WAIT. We know there are progenerators, this is what is required FOR union find.
# Lets take this opportunity to actually finally learn that algo.


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Ok, highly dubious of this solutions, but maybe not awful?
        # traverses every edge AT LEAST ONCE, but possibly many times.
        # The sorting method at the end may also be dubious, but I think its
        # necessary. We cant really input them into sorted order anyhow
        # Collecting them as a set as we go makes sense, but we need to
        # return a list of lists in the end.

        # What I really want is the exact reverse of this logic. Start with the children
        # and say "this gets all its parents ancestors, plus the parent", then work UP
        # Thus the ancestor sets further down get DYNAMICALLY filled in as we move UP.
        # Currently I am passing the same info down possibly many many times manually

        # NON UNION FIND:
        from_to = collections.defaultdict(list)
        to_from = collections.defaultdict(list)
        ancestors = collections.defaultdict(set)

        for fromm, to in edges:
            from_to[fromm].append(to)
            to_from[to].append(fromm)

        next_node_set = set(x for x in from_to.keys() if x not in to_from.keys())
        curr_node_set = set()

        while next_node_set:
            curr_node_set = next_node_set
            next_node_set = set()

            while curr_node_set:
                curr_node = curr_node_set.pop()
                for child in from_to[curr_node]:
                    ancestors[child] = ancestors[child].union(ancestors[curr_node])
                    ancestors[child].add(curr_node)
                    next_node_set.add(child)

        return [sorted(list(ancestors[x])) for x in range(n)]

        # from_to = collections.defaultdict(list)
        # to_from = collections.defaultdict(list)
        # ancestors = collections.defaultdict(list)
        # visited = set()

        # for fromm, to in edges:
        #     from_to[fromm].append(to)
        #     to_from[to].append(fromm)

        # #Get LEAVES
        # next_node_set = set( x for x in to_from.keys() if x not in from_to.keys() )
        # curr_node_set = set()

        # while next_node_set:
        #     curr_node_set = next_node_set
        #     next_node_set = set()

        #     #Ok, now ancestors is a

        #     while curr_node_set:
        #         curr_node = curr_node_set.pop()
        #         for parent in to_from[curr_node]:
        #             ancestors[curr_node].append(ancestors[parent])
        #             ancestors[curr_node].append([parent])
        #             if parent not in visited:
        #                 next_node_set.add(parent)

        # def flatten(x):
        #     result = []
        #     for el in x:
        #         if el == []:
        #             continue
        #         elif hasattr(el, "__iter__"):
        #             result.extend(flatten(el))
        #         else:
        #             result.append(el)
        #     return list(set(result))

        # return [sorted(flatten(ancestors[x])) for x in range(n)]
