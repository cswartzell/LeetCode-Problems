# 04-04-2024 Leetcode 752. Open the Lock
# https://leetcode.com/problems/open-the-lock/
# Time: 20 mins, Challenge: 4/10


# Blind Redo
# Because of the locks, we cannot simply work one wheel at a time: take for instance a target of 1555
# but lets assume there are locks for all 1XXX combinations other than 555. We therefore CANNOT set
# the first wheel to 1 as step 1. Take our example further: target is 1555, start is 0000, 
# and ALL OTHER COMBINATIONS are locked. We cant even begin. So can we move the wheels
# independently and just sum results or not? Its going to take the same number of turns to get 
# the first wheel to 1 regardless of when we do it so does it matter when we count so long as
# getting there is possiblle?

# We can BFS it trivially. I'm wondering if we have to. I have a visual intuition: Imagine its 
# a lock with just 2 digits. Its combination space is a grid. No imagine the deadlocks being walls;
# so long as the start isnt entirely isolated from the target, there is a route to get to the end. It 
# however may NOT be taxicab distance but a complex path. Now extend this to 4d. I think we DO need to
# BFS it, like navigating a 4d maze.

# Now whether to use strings or ints? Ints may be faster but then there is cumbersome conversions all over.
# lets just keep it as strings and use a dict rather than ord(offset) nonsense

# Holy shit. Not a single error. Not one syntax mistake. I typed this perfectly and it worked
# perfectly on the first run. That never happens. Never. This isnt even trivial, I threw in the lambda
# just for funsies. Its top 9% too, so not bad. 

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # increase = {"0":"1","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"9","9":"0"}
        # decrease = {"9":"8","8":"7","7":"6","6":"5","5":"4","4":"3","3":"2","2":"1","1":"0","0":"9"}
        increase = {chr(x):chr((x+1)%10) for x in range(10)}
        decrease = {chr(x):chr(abs(x-1)%10) for x in range(10)}
        
        _deadends = {deadend for deadend in deadends}
        _target = [char for char in target]
        
        check = lambda state: "".join(char for char in state) 

        queue = [[0,["0","0","0","0"]]]
        while queue:
            curr_moves, curr_state = queue.popleft()
            for wheel in range(4):
                up = curr_state[::]
                up[wheel] = increase[curr_state[wheel]]
                if up == _target:
                    return curr_moves + 1
                elif check(up) not in _deadends:
                    _deadends.append(check(up))
                    queue.append([curr_moves + 1, up])

                down = curr_state[::]
                down[wheel] = decrease[curr_state[wheel]]
                if down == _target:
                    return curr_moves + 1
                elif check(down) not in _deadends:
                    _deadends.append(check(down))
                    queue.append([curr_moves + 1, down])
                
        return -1



# 11-26-2022 LeetCode 752. Open the Lock
# https://leetcode.com/problems/open-the-lock/description/

#is... is this a 4d BFS? It could be? Just note the deadlocks
#in 4d space, and starting at the first position start making
#our way toward the target?

#It should just be the 4d manhattan distance... but as the wheels
#go backwards not quite. There'd have to be a hell of a lot of
#deadlocks to make a significant difference: like "every number
#where the last wheel is a 3 except the target and when the second
#wheel is an 8"

#I guess we can compress it down to 2d? 100x100=10000. Just multiply
#the first and third wheels BY 10 and add them respectively to the
#second and forth wheels. Doesnt reduce the space but may be fewer
#counters and loops and such

#Well, we know some things, like a lower bound: The sum of the
#four dials is the minimum moves. No wait, we can go backwards...
#The lower bound is the sum of the 4 dials least moves...

#Spins to get X Digits (starting from 0)
#Digits: 0 1 2 3 4 5 6 7 8 9
#Spins:  0 1 2 3 4 5 4 3 2 1
# min(x, 10-x)

#Spins to go from x->y: min( max(x,y)-min(x,y), 10-max(x,y)-min(x,y) )
#so sum this for 0->target for each dial


#Ok, so lets think about this just like our standard 2d BFS, but 4d:
#Each cell has 8 neighbors instead of 4 (+1/-1 for each dimension): Easy
#Each step toward a neighbor adds one to curr_step, stored part of 5d tuple 
#on the stack.
#Instead of checking bounds, we need to wrap: (cur_pos_d + offset + 10)%10
#Thus (9 + 1 + 10) % 10 = 0 and (0 - 1 + 10) % 10 = 9
#We only add to our stack if the neighborind cell is 2 or MORE than current cell
#We should set all cells other than deadlocks arbitrarily high to start with
#We simply dont add deadlocks to the stack ever
#This is flood fill from a SINGLE start location. We dont need to loop or check
#new locations. Everything possible to access will be accessible FROM the start
#locations (or is blocked off ancd can be ignored). Therefore, we only need to
#seed a stack and go from there. No need to loop through multiple seeds.
#Once the stack is empty... and it may be a while, we simply return the value
#(steps taken) to reach the target. If the target is still the preset value
#then there is no way to reach the target from START. 

#Simple in its complexity? Insane? It seems like there is maybe a FAR
#simpler way of doing this right? Its in the BFS problem set though, so
#thats a pretty strong hint. 


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 5d tuple, 4 neigbhbor dimensions. steps[4] is curr_steps to get to cell

        # Base Case- The lock is stuck to start.
        if "0000" in deadends:
            return -1

        # The OTHER base case: The target is the start.
        if target == "0000":
            return 0

        #Setup grid, even though there is aparently no need. As we are doing
        #BFS, we WILL be visiting all nodes in order, as fast as possible.
        #This is only necessary if there were multiple start points. I
        #chose to do it this way as I suspect I can reuse this code in the future


        #Instead, we can merely use the queue to store adjacent nodes to our
        #seed node and proceed from there. As long as we are popping left, we
        #will reach our target (if possible) eventually, and in as few steps 
        #as is possible. We would need a "visied" hashmap, and really thats more
        #or less the same as an indexed 4d array right?         
        
        #We may have to process the entire set of other nodes
        #that are the same steps away from START as TARGET, but no nodes that are
        #further
        #If the target isnt found by the time we run out of steps, return -1
       
        space = [
            [[[10000 for _ in range(10)] for _ in range(10)] for _ in range(10)]
            for _ in range(10)
        ]
        #Markout dead positions
        for dl0, dl1, dl2, dl3 in deadends:
            space[int(dl0)][int(dl1)][int(dl2)][int(dl3)] = -2
        #Notate the target
        space[int(target[0])][int(target[1])][int(target[2])][int(target[3])] = -1

        asteps = deque()
        asteps.append( (0, 0, 0, 0, 0) )
        while asteps:
            curr_pos = asteps.popleft()
            curr_steps = curr_pos[4]
            for d0, d1, d2, d3 in [
                (-1,  0,  0,  0),
                ( 1,  0,  0,  0),
                ( 0, -1,  0,  0),
                ( 0,  1,  0,  0),
                ( 0,  0, -1,  0),
                ( 0,  0,  1,  0),
                ( 0,  0,  0, -1),
                ( 0,  0,  0,  1),
            ]:
                cd0, cd1, cd2, cd3 = (
                    (curr_pos[0] + d0 + 10) % 10,
                    (curr_pos[1] + d1 + 10) % 10,
                    (curr_pos[2] + d2 + 10) % 10,
                    (curr_pos[3] + d3 + 10) % 10,
                )
                if space[cd0][cd1][cd2][cd3] == -1:
                    return curr_steps + 1
                if (
                    space[cd0][cd1][cd2][cd3] != -2
                    and space[cd0][cd1][cd2][cd3] > curr_steps + 1
                ):
                    space[cd0][cd1][cd2][cd3] = curr_steps + 1
                    asteps.append((cd0, cd1, cd2, cd3, curr_steps + 1))

        
        return space[int(target[0])][int(target[1])][int(target[2])][int(target[3])]
