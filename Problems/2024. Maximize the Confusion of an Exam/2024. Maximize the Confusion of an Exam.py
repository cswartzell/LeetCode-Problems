# 07-06-2023 Leetcode 2024. Maximize the Confusion of an Exam
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/

# Basic sliding window? Do it twice? Possible to do in one go?
# Ah, it is possible to do it in go. As the choice is binary
# the window cant have k more T's than F's while ALSO having
# K more F's than T's. We are either valid (the diference in count
# between the two is less than K) or we are invalid, and we dont care
# which we are off by. We ALWAYS slide the right side of the window, and
# if we are invalid we ALSO slide the left, subtracting whatever just left.

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        T_count, F_count = 0, 0
        L, R = 0, 0  

        while R < len(answerKey):
            T_count += answerKey[R] == "T"
            F_count += answerKey[R] == "F"
            R += 1

            if  min(F_count, T_count) > k :
                T_count -= answerKey[L] == "T"
                F_count -= answerKey[L] == "F"
                L += 1

        return R - L


        # while R < len(answerKey):
        #     if answerKey[R] == "T":
        #         T_count += 1
        #     else:
        #         F_count += 1
        #     R += 1

        #     if  min(F_count, T_count) > k :
        #         if answerKey[L] == "T":
        #             T_count -= 1
        #         else:
        #             F_count -= 1
        #         L += 1

        # return R - L



        # #Check True runs:
        # while R < len(answerKey):
        #     F_count += int(answerKey[R] == "F")
        #     R += 1
        #     if F_count > k:
        #         F_count -= int(answerKey[L] == "F")
        #         L += 1
        # longest_T_run = R-L
        
        # L, R = 0, 0  
        # #Check False runs:
        # while R < len(answerKey):
        #     T_count += int(answerKey[R] == "T")
        #     R += 1
        #     if T_count > k:
        #         T_count -= int(answerKey[L] == "T")
        #         L += 1 
        # longest_F_run = R-L
        
        # return max(longest_T_run, longest_F_run)



        # L, R = 0, 1  
        # #Check True runs:
        # while R < len(answerKey):
        #     F_count += int(answerKey[R] == "F")
        #     R += 1
        #     while F_count > k:
        #         F_count -= int(answerKey[L] == "F")
        #         L += 1
        #     longest_T_run = max(longest_T_run, R-L)
        
        # L, R = 0, 1  
        # #Check False runs:
        # while R < len(answerKey):
        #     T_count += int(answerKey[R] == "T")
        #     R += 1
        #     if T_count > k:
        #         T_count -= int(answerKey[L] == "T")
        #         L += 1
        #     longest_F_run = max(longest_F_run, R-L)

        # return max(longest_T_run, longest_F_run)