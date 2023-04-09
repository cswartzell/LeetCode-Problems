# 04-04-2023 Leetcode 365. Water and Jug Problem
# https://leetcode.com/problems/water-and-jug-problem/description/


# if they are the same, you can only take one measurement: jug

# if not the same, one is larger than the other
# Things you can measure:
# Big Jug
# any multiple of little jug < big jug, including trivially Small Jug
# big jug % little jug
# big jug MINUS any multiple of small jug


class Solution:
    def canMeasureWater(self, a_cap: int, b_cap: int, target: int) -> bool:
        # return (targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0) and (targetCapacity <= jug1Capacity + jug2Capacity)

        # Lets try a simulation. At any point we may take one of SIX actions:
        # A) fill jug A or B to full from supply (regardless of current state)
        # B) empty jug A or B TO supply (regardless of current state)
        # C) Por from A to B or B to A STOPPING on filling the receiver jug (we can dump excess per rule B in a later step)
        # If at any point jug A, B, or A+B = target capacity we can stop.
        # Now just BFS it, keeping a list of seen tuples where the tuple means we have seen that combination of (jugA, jugB)
        # before. Obviously getting there a second time is pointless

        a, b = 0, 0
        seen = {(0, 0)}
        q = [(0, 0)]
        while q:
            a, b = q.pop()
            if a == target or b == target or a + b == target:
                return True
            # Empty a
            if (0, b) not in seen:
                seen.add((0, b))
                q.append((0, b))
            # Empty b
            if (a, 0) not in seen:
                seen.add((a, 0))
                q.append((a, 0))

            # Fill a
            if (a_cap, b) not in seen:
                seen.add((a_cap, b))
                q.append((a_cap, b))
            # Fill b
            if (a, b_cap) not in seen:
                seen.add((a, b_cap))
                q.append((a, b_cap))

            # Pour a to b
            if (max(0, a - (b_cap - b)), min(b_cap, a + b)) not in seen:
                seen.add((max(0, a - (b_cap - b)), min(b_cap, a + b)))
                q.append((max(0, a - (b_cap - b)), min(b_cap, a + b)))
            # Pour b to a
            if (min(a_cap, a + b), max(0, b - (a_cap - a))) not in seen:
                seen.add((min(a_cap, a + b), max(0, b - (a_cap - a))))
                q.append((min(a_cap, a + b), max(0, b - (a_cap - a))))

        return False
