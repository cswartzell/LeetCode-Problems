# Pretty badly worded. Firstly, we have meetings between only two people, but
# person x can meet with multiple people individually... at the same time.
# As a person can receieve and share the secret in the same meeting, this means
# we can connect all people meeting at a given time: if x meets with y and x meets
# with z at time 9, and z meets with b at time 9, then x, y, z, and b are all in
# the same meeting. Identify meeting groups by time. Process them in order.
# Keep a bool array for who knows. No wait, we can just do a set. Make the meeting
# groups sets too and we can just use union to add people in the know:

# The people in the know are K. For a given group G, if the intersection of G and K
# isn't empty, someone knows. K = K union G. Perhaps faster than interstection is the
# any() function. If any member of G is in K. any() exits early. 

# In order to find out who is in meeting at a given time, this is simple union find. 
# We'll just ust the lowest n as the "group leader" for that meeting.

# Ok, so first things first: sort the pairings by time. We can do this in O(n) rather than
# nlogn. Then disjoint unions per time, storing these as sets of group members in a list for
# that time (there may be more than one group). Then iterate through the times, spreading 
# the secrete to group members and increasing the in the know set.

# Easy enough?

# Close. Mem limit exceeded for once. I think Im making it more complicated than it needs to be.
# I was trying to avoid sorting just to pretend to be smarty pants, but its cosing inordinate memory.
# By sorting I dont need to save a whole list of roots for each time. I can deal with each time marker
# as it comes up, and completely do away with previous states other than in the know. 

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:        
        def root(x):
            while roots[x] != x:
                roots[x] = root(roots[x])
            return x

        def union(x,y):
            x_root = root(x)
            y_root = root(y)
            if x_root > y_root:
                roots[x_root] = y_root
            else: 
                roots[y_root] = x_root

        in_the_know = {0, firstPerson}
        _meetings = sorted(meetings, key= lambda x: x[2])
        idx = 0

        while idx < len(_meetings):
            curr_time = _meetings[idx][2]
            roots = [*range(n)]
            while idx < len(_meetings) and _meetings[idx][2] == curr_time:
                x, y, _ = _meetings[idx]
                union(x,y)
                idx += 1

            groups = collections.defaultdict(set)
            for person in range(n):
                groups[root(roots[person])].add(person)                
        
            for group in groups.values():
                for person in group:
                    if person in in_the_know:
                        in_the_know |= group
                        break
        
        return list(in_the_know)
        
        roots_at = collections.defaultdict(lambda : [*range(n)])

        def root(x):
            while roots[x] != x:
                x = roots[x]
            return x

        def union(x,y):
            x_root = root(x)
            y_root = root(y)
            if x_root > y_root:
                roots_at[x_root] = y_root
            else: 
                roots_at[y_root] = x_root


        #unionfind per time
        for x, y, time in meetings:
            union(x,y, time)            

        groups_at = collections.defaultdict(list)
        for time in roots_at.keys():    
            # For the given time, place each memeber into a meeting indexed by its group leader
            groups = collections.defaultdict(set)
            for x in range(n):
                groups[roots_at[time][root(x, time)]].add(x)

            # add each of these group sets to the list of sets at the given time
            for group in groups.values():
                groups_at[time].append(group)

        in_the_know = {0, firstPerson}

        # Process meetings in time order
        for time in sorted(groups_at.keys()):
            # For a given time, groups are independent. Add groups that have at least
            # one in_the_know member to the club
            for group in groups_at[time]:
                if any(x in in_the_know for x in group):
                    in_the_know |= group

        return list(in_the_know)
