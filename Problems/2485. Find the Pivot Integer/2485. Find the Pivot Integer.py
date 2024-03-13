# 03-12-2024 Leetcode 2485. Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/?envType=daily-question&envId=2024-03-13
# Time: 10 mins Challenge: 3/10

# sum of ints 1...x is x * (x+1) // 2
# Its the xth triangular number.
# So we binary n and see if triNum(x) == triNum(n)//2


class Solution:
    def pivotInteger(self, n: int) -> int:
        # if n == 1:
        #     return 1

        # target = (n * (n + 1)) // 2

        # L, R = 0, n
        # while L < R:
        #     x = L + (R - L)//2
        #     curr_x = (x * (x + 1)) // 2
        #     prev_x = (x * (x - 1)) // 2

        #     trinum = curr_x + prev_x
        #     if trinum < target:
        #         L = x + 1
        #     elif trinum > target:
        #         R = x - 1
        #     else:
        #         return x

        # return -1

        # return y if ((y := bisect.bisect_left(range(n), n*(n+1)//2, key=lambda x: (x*(x+1)//2) + (x*(x-1)//2)))*(y+1)//2) + (y*(y-1)//2) == n*(n+1)//2 else -1

        # x = lambda x: x*(x+1)//2
        # y = lambda y: y*(y-1)//2
        # return a if x(a:= bisect.bisect_left(range(n), (t:=x(n)), key=lambda b: x(b) + y(b))) + y(a) == t else -1

        # (x:=lambda x: x*(x+1)//2)
        # (z:=lambda z: x(z) + x(z-1))
        # return a if z(a:= bisect.bisect_left(range(n), (t:=x(n)), key=lambda b: z(b))) == t else -1
        # OH GOD IM A MONSTER
        # return a if (z:=lambda z:x(z)+x(z-1))(a:=bisect.bisect_left(range(n),(t:=(x:=lambda x:x*(x+1)//2)(n)),key=lambda b: z(b)))==t else -1

        # (x:=lambda x:x*(x+1)//2)
        return (
            a
            if (x := lambda x: x * (x + 1) // 2)(
                a := bisect.bisect_left(
                    range(n), (t := x(n)), key=lambda b: x(b) + x(b - 1)
                )
            )
            + x(a - 1)
            == t
            else -1
        )
