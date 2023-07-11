# 07-08-2023 Leetcode 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/

# The candidates do not have negatives, so we can stop once we've blown the limit

# The candidates may contain duplicates, AND THESE ARE VALID.  I am assuming order DOESNT matter, 
# but the question doesnt make that clear. [10,1] is the same as [1,10]

#Sorting seems like a good shortcut. We can exit early knowing the sum is blown irrecoverably

#Recursive backtracking? 
#First instinct is basically recursion implementing an n-nested set of for loops. As long as
# the sum isnt blown, fire up another level of for loops? This seems like madness. O(n**100)
# Second day in a row I have come upon "huh, I dont know how to efficiently generate every permutation"

# Target is really small so we will early exit pretty often. 

# Consider input [1,1,1] with target two. Iterating through it will give us two copies of the same
# sum to 2: [1,1]. Should we store these as a tuple in a set then count that at the end? Seems 
# cumbersome. Now I also have to pass down a building list... 20 minutes in, a bit commited at this point
# Oh wait, we arent counting them. They are expecting a list of lists. Ok, we SHOULD generate and pass



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = set()
        self.candidates = sorted(candidates)
    

        def go_deeper(index:int, prev_sum:int, curr_list:tuple):
            blown = False
            for i in range(index, len(self.candidates)):
                new_sum = prev_sum + self.candidates[i]
                if new_sum > target:
                    return True
                elif new_sum < target:
                    blown = go_deeper(i + 1, prev_sum + self.candidates[i], curr_list + (self.candidates[i],))
                    if blown:
                        return False
                elif new_sum == target: 
                    self.answer.add(curr_list + (self.candidates[i],))
                    
        go_deeper(0,0,tuple())
        
        return [list(x) for x in self.answer]