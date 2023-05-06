from ast import List
from collections import Counter

# class Solution:
def minDominoRotations(tops, bottoms) -> int:
    t_c = Counter()
    b_c = Counter()
    dubs = Counter()
    rots = 2001

    for i in range(len(tops)):
        if tops[i] == bottoms[i]:
            double = tops[i]
            dubs[tops[i]] += 1
            if len(dubs) > 1:
                return -1
        else:
            t_c[tops[i]] += 1
            b_c[bottoms[i]] += 1

    len_minus_dubs = len(tops) - dubs[double]

    for i in range(1, 7):
        if t_c[i] + b_c[i] == len_minus_dubs and ((len(dubs) == 0) or (i in dubs)):
            rots = min(rots, t_c[i], b_c[i])
    return rots if rots < 2001 else -1


a = [1, 1, 1, 1, 1, 1, 1, 1]
b = [1, 1, 1, 1, 1, 1, 1, 1]

r = minDominoRotations(a, b)
