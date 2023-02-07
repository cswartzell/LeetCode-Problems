# 02-06-2023 Leetcode 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/

# wow do i hate this one.

# Nope. Simple sliding/exapanding window counter.
# if the len of the counter is 2 or less, advance the right pointer
# if the len of the counter (num of elements) is 3, move the left pointer
# deleting fruit until the len(fruit_types) drops to two.
# Make sure to update the curr_max fruits collected, probably at the discovery
# discovery of the third fruit. Hell, we could just do it every time len == 2


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr_max = 0
        fruits_collection = collections.defaultdict(int)
        right, left = 0, 0

        # may need to rethink ending condion. This may leave off last fruit.
        while right < len(fruits):
            fruits_collection[fruits[right]] += 1
            right += 1

            # no need to make sure l is < r, that should be true if len(fruits_collection) is positive
            while len(fruits_collection) > 2:
                fruits_collection[fruits[left]] -= 1
                if fruits_collection[fruits[left]] == 0:
                    del fruits_collection[fruits[left]]
                left += 1

            # this could probably be called less often. We know when were deleting fruits we cant possibly
            # have a LARGER collection of fruit. At best we are deleting one and adding one, netting 0
            # its possible we are deleting MORE fruit
            curr_max = max(curr_max, sum(fruits_collection.values()))

        return curr_max

        # #collect first fruit type...
        # left_hand_fruit = fruits[0]
        # left_hand_num = 1
        # left_hand_last_i = 0
        # #til second type discovered
        # right_hand_fruit = 0
        # right_hand_num = 0
        # right_hand_last_i = 0

        # i = 1
        # while i < len(fruits) and fruits[i] == left_hand_fruit:
        #     left_hand_num += 1
        #     left_hand_last_i = i
        #     i += 1
        # #Collect first of second type of fruit
        # if i < len(fruits):
        #     right_hand_fruit = fruits[i]
        #     right_hand_num = 1
        #     right_hand_last_i = i

        # curr_max = max(curr_max, left_hand_num + right_hand_num)

        # i += 1
        # while i < len(num):
        #     #another left fruit
        #     if fruits[i] == left_hand_fruit:
        #         left_hand_num += 1
        #         left_hand_last_i = i
        #     #another right fruit
        #     elif fruits[i] == right_hand_fruit:
        #         right_hand_fruit = fruits[i]
        #         right_hand_num = 1
        #     else:
        #         curr_max = max(curr_max, left_hand_num + right_hand_num)

        #     i += 1
