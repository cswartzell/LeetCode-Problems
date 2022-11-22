class Solution:
    # @cache                  #Recursive method is shitty O(2**n without caching), now its O(n)
    def fib(self, n: int) -> int:
        # Recursive, but with caching
        return self.fib(n - 2) + self.fib(n - 1) if n >= 2 else n

        # iterative: MUCH faster.


#         if n == 0:
#             return 0

#         x = 1
#         for _ in range(1,n):
#             y,x = x, x+y
#         return x

# #binet
# return(    round(    (((1+5**0.5)/2)**n)/5**0.5    )    )


# lulz
# fibs = {0:0,1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,11:89,12:144,13:233,14:377,15:610,16:987,17:1597,18:2584,19:4181,20:6765,21:10946,22:17711,23:28657,24:46368,25:75025,26:121393,27:196418,28:317811,29:514229,30:832040}
# return fibs[n]
