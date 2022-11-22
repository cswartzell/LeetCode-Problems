"""05-11-2022 Leetcode 1641. Count Sorted Vowel Strings"""

#I think its really trying to teach backtracking and I just keep ignoring 
# it, or what is likely: backtracking without knowint it. 
class Solution:
    def countVowelStrings(self, n: int) -> int:

# Lets try to decern the pattern...        
# length 1 = 5 = 5
# length 2 = 5+4+3+2+1 = 15
# length 3 = (5+4+3+2+1)+(4+3+2+1)+(3+2+1)+(2+1)+(1) = 35
# length 4 = 70
# length 5 = 126
# length 6 = 210
# OEIS says its the binomial coeficient binomial (n+1)*(n+2)*(n+3)*(n+4)/24
# This is vowels = 5 "combination with repetition" or multiset 

# and this is why you read the prompt... This is a pretty straightforward
# method of generating said list... which it did not ask for. It asked for the
# SIZE of said list, which can just be figured out with math. Of course the 
# following works if I just return len(ans), but thats quite silly. Why bother
# generating the whole list. 
  
        # return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24;

        
    
#         vowels = ["a", "e", "i", "o", "u"]
#         m = {"a":0, "e":1, "i":2, "o":3, "u":4}
        
#         ans = ["a", "e", "i", "o", "u"]
        
#         for _ in range(n-1):
#             new_ans = []
#             for x in ans:
#                 for y in vowels[m[x[-1]]:]:
#                     new_ans.append(x + y)
#             ans = new_ans

#         return len(ans)