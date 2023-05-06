# 03-30-2023 Leetcode 2509. Cycle Length Queries in a Tree
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/description/


# Get a and b depth. have the deeper one catch up, counting edges til same depth
# find parents of both and check if  same til root, end early if same


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def get_parent(x) -> int:
            if x % 2:
                return (x - 1) // 2
            return x // 2

        ans = []
        for a, b in queries:
            cycle_len = 2  # even a self edge is a cycle 1
            a_depth = math.ceil(math.log2(a + 1))
            b_depth = math.ceil(math.log2(b + 1))
            while b_depth > a_depth:
                cycle_len += 1
                b = get_parent(b)
                b_depth = math.ceil(math.log2(b + 1))
            while a_depth > b_depth:
                cycle_len += 1
                a = get_parent(a)
                a_depth = math.ceil(math.log2(a + 1))
            while a != b:
                cycle_len += 2
                a = get_parent(a)
                b = get_parent(b)
            ans.append(cycle_len - 1)

        return ans
