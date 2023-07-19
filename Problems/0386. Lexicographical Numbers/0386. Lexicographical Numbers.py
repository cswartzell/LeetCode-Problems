# 07-17-2023 Leetcode 386. Lexicographical Numbers
# https://leetcode.com/problems/lexicographical-numbers/description/

# Ugh, I think I am missing something as this seems OBNOXIOUS

# 1 comes before 10, but 101 comes before 11 and 1001 comes before 101
# and yet 10 comes before 100. When tied, the SHORTETER number is first

#so for n of 2500
# 1 10 100 1000...1009 101 1010...1019 102 1020 ... 1099 11 110 1110...1119
# ugh, so the length bounces up and down up and down...

# Every time we carry, we truncate TO the digit we are about to carry to
# but for ripple carry we do this backward:
# for 19999999 when we go to add that last 1 we truncate all the way down to 2
# then 20, then 200, then ... So we add it backwards
# So we should just add recursively, multiplying by ten each time, then just adding 
# 0-9 as postfix as long as we are under n 

#Wait, I am an idiot. This is a basic recursion problem. Each level just appends 0-9,
# one at a time, and recurses down after adding its digit. Start with 1, add 0 and recurse
# now we have 10, add zero and recurse, now 100. 1000 is to big so pass back up: 10 again, so
# append 1 to get 101 etc


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.ans = []

        def dig_it( curr ):
            self.ans.append(curr)
            curr *= 10
            j = 0
            while curr + j <= n and j < 10:
                dig_it(curr + j)
                j += 1
    
        for first_digit in range(1,10):
            if first_digit <= n:
                dig_it(first_digit)
        return self.ans

        
        #         self.ans = []

        # def dig_it( curr ):
        #     seeit = self.ans
        #     if curr <= n:
        #         self.ans.append(curr)
        #     curr *= 10
        #     j = 0
        #     while curr + j <= n and j < 10:
        #         dig_it(curr + j)
        #         j += 1
    
        # for first_digit in range(1,10):
        #     dig_it(first_digit)
        # return self.ans


# FAILED
# loop for each starting digit
# multiply and add to ans by k powers of 10 such that the result is less than n
# count k up.
# When larger than target, we have: Our first digit, the current power of 10
# now start counting REMAINDER where remainder is all numbers under 10**k
# At each step add First digit * 10**k + remainder
# at the end of each of THOSE loops, decrement N.
# All the while checking we havent blown the target
        
        
        
        
        # ans = []
        
        # for first_digit in range(1, 10):
        #     k = 0
        #     while first_digit * 10**k < n:
        #         ans.append(first_digit * 10**k)
        #         k += 1
        #     k -= 1

        #     while k > 0:
        #         remainder = 0

        #         while remainder < 10**k and first_digit*10**k + remainder < n:
        #             remainder += 1
        #             ans.append(first_digit * 10**k + remainder)

        #         k -= 1
        
        # return ans