# 02-06-2023 Leetcode 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/description/


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # #Surely there is a clever way to do this destructively in place but im getting a little lost
        # new_list = []
        # for i in range(n):
        #     new_list.append(nums[i])
        #     new_list.append(nums[i+n])
        # return new_list

        for i in range(2 * n - 1):
            # Calculate the correct position for nums[i]
            if i < n:
                correct_pos = 2 * i
            else:
                correct_pos = 2 * (i - n) + 1

            # Swap nums[i] with the element at correct_pos
            temp = nums[i]
            nums[i] = nums[correct_pos]
            nums[correct_pos] = temp

        return nums
