
# Represent as bitmask. There are 9 operations possible for any state,
# which generates up to 9 new states.
# Operations are just a xor of a particular mask 
# There are only 2^9 = 512 states, with 9 transitions, so thats only like 4600
# XORS to perform at max. Technically its way less as there are all kinds of symmetries
# (a single 1 in a corner is the same state rotated 4 times), but its almost certainly
# more costly to try to deal with reflections and rotations rather than just
# check every state and transition using XOR

# 110   
# 100
# 000
# 110100000

# 111   
# 010
# 000
# 111010000

# 011   
# 001
# 000
# 011001000

# 100
# 110
# 100
# 100110100

# 010   
# 111
# 010
# 010111010

# 001   
# 111
# 001
# 001111001

# 000   
# 100
# 110
# 000100110

# 000   
# 010
# 111
# 000010111

# 000   
# 001
# 011
# 000001011

# transitions = [0b110100000, 0b111010000, 0b011001000, 0b100110100, 0b010111010, 0b001111001, 0b000100110, 0b000010111, 0b000001011]
# Oh wait. Its not necesarrily a 3x3. Just at MOST a 3x3. I need to generate the transitions dynamically
# Once we have the transitions, we just djikstras

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        start_state = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col]:
                    start_state |= 1<<(m - 1 - row) * n + (n - 1 - col)
        if start_state == 0:
            return 0

        transitions = []
        for curr_row in range(m):
            for curr_col in range(n):
                transition = 0
                for row_d, col_d in [(0,0),(-1,0), (0, 1), (1, 0), (0, -1)]:
                    if 0 <= curr_row + row_d < m and 0 <= curr_col + col_d < n:
                        transition |= 1 << ((m - 1 - (curr_row + row_d)) * n) + (n - 1 - (curr_col + col_d))
                transitions.append(transition)

        stack = collections.deque()
        stack.append((0, start_state))
        seen = {start_state}

        while stack:
            curr_ops, curr_state = stack.popleft()
            for transition in transitions:
                new_state = curr_state ^ transition
                if new_state == 0:
                    return curr_ops + 1
                if new_state not in seen:
                    seen.add(new_state)
                    stack.append((curr_ops + 1, new_state))
        
        return -1
