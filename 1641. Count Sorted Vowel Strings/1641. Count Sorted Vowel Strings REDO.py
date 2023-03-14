1641. Count Sorted Vowel Strings

# Seems like straigh combinatronics to me
# 1 char: a e i o re.U 5 choose 1
# 2 char: 5 starting with a, 4 starting with e, 3 with i, 2 with o, 1 with u 
# 3 chars: 5 times the above starting with a,
#          4 times 4 with e 

#So for each new char, you get the whole number of the previous sum for the As
# the whole number of previous sum from E onwards for E...
# it turns out its the binomial coeficients. Look that up on OEIS, get a simple formula
# boom. This isnt cheating, this is how you solve real world problems

#Now lets assume they are going to be dicks and not allow outside research. 
# No way am I deriving this myself. I even had to check and adjust the formula
# as it only works for n > 3. Solution? Just add 3 to each term, its the same sequence

#This can be solved by DP. Have a DP array of only len 5. At first, there is 1 way
# for a word of len 1 for each letter. Next, there are 5 ways for a, 4 ways for E
# three ways for i.... this amounts to the sum of the sum of the dp array from 0 to 4
# iteratively


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # return (n+4)*(n+3)*(n+2)*(n+1)//24 

        dp = [1,1,1,1,1]
        for _ in range(n - 1):
            for i in range(4): #we can cheat as the last one will ALWAYS == 1: sum[1] = 1 forever
                dp[i] = sum(dp[i:])
        return sum(dp)
