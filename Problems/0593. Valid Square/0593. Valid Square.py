from math import sqrt
from typing import List

p1, p2, p3, p4 = [0,0],[1,sqrt(3)],[2,0],[3,sqrt(3)]

if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
    # return False
    print("false")

def d(a: List[int], b: List[int]) -> int:
    return (b[0] - a[0])**2 + (b[1] - a[1])**2
        
# return len(set([d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)])) == 2

ans = set([d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)])
print(len(ans) == 2)