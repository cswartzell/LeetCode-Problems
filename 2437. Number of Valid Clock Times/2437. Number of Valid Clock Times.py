# 03-16-2023 Leetcode 2437. Number of Valid Clock Times
# https://leetcode.com/problems/number-of-valid-clock-times/description/

# class Solution:
#     def countTime(self, time: str) -> int:
#         num_possible = [1,1,1,1]
#         first_can_be_two = False

#         # First digit can always be a one or zero, but can only be a two if the second digit is
#         # ALSO a question mark, or is 3 or less: 2?:XX or 23:XX
#         if time[0] == "?":
#             #ONLY account for 0-1 so far. 2 is handled seperately
#             num_possible[0] = 2
#             if (time[1] == "?" or int(time[1]) <= 3):
#                 first_can_be_two = True

#         #The second digit can be 0-9 UNLESS the first digit is a 2
#         if time[1] == "?":
#             num_possible[1] = 4 if time[0] == "2" else 10

#         #The third digit can be 0-5 regardless of any other factors
#         if time[3] == "?":
#             num_possible[2] = 6

#         #The Fourth digit can be 0-9 regardless of any other factors
#         if time[4] == "?":
#             num_possible[3] = 10

#         # This is the combinations of digits EXCLUDING where the first digit is a two
#         times_sum = math.prod(num_possible)
#         # times_sum = num_possible[0] * num_possible[1] * num_possible[2] * num_possible[3]

#         # If the first digit can be a two, we add the new possibilities.
#         # Weve already acounted for 0-1 in the first digt and since we're adding the
#         # new products, the first digit can only be a 2, so that just multiplies the
#         # product by 1. We can ignore it. The product of the 3rd and 4th digits already
#         # the same, so include those. NOW, either the third digit is a 1, in which case ignore it
#         # or it's 4 or 9. In either case, we cant use the digits 5+, so just use up to 4 in our
#         # product. So: either 1*3rd*4th or 4*3rd*4th. ADD this to the base sum
#         if first_can_be_two:
#             # base_sum += math.prod(num_possible[2:]) * (4 *(num_possible[1] >= 4))
#             if num_possible[1] == 1:
#                 times_sum += num_possible[2] * num_possible[3]
#             else:
#                 times_sum += num_possible[2] * num_possible[3] * 4

#         return times_sum


class Solution:
    def countTime(self, t: str) -> int:
        mm = (6 if t[3] == "?" else 1) * (10 if t[4] == "?" else 1)
        match [t[0], t[1]]:
            case ("?", "?"):
                return mm * 24
            case ("?", ("0" | "1" | "2" | "3")):
                return mm * 3
            case ("?", _):
                return mm * 2
            case (("0" | "1"), "?"):
                return mm * 10
            case ("2", "?"):
                return mm * 4
        return mm
