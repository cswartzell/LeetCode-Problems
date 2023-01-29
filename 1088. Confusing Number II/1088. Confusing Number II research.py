# An insade exploration of various techniques in solving this. I got it down to one
# reasonably functional line. There is some gold in there... the three uses of str.replace()
# consecutively chained to swap two chars is pretty absurd. Reinforcing itertools usage with
# product repetition and chain to flatten lists, using lstrip() to remove leading zeros,
# the legitimate benefits of using string instead of numbers here for slicing and editing,
# sum(1 for x in ...) to count occurances of a conditional in a generator,
# using len(str(n)) to get the number of digits of n... A lot of good, clever tricks,
# absolutely butchered together to form one unreadable pile. Fun to do. Obviously absurd.

# ans = sum([1 for x in set("".join(x).lstrip("0") for x in itertools.chain(*[itertools.product(["0", "1", "6", "8", "9"], repeat=i) for i in range(1, len(str(n)) + 1)])) if x != x.replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int(x) <= n])
# final_ans = sum([1 for x in set("".join(x).lstrip("0") for x in [itertools.product(["0", "1", "6", "8", "9"], repeat=i) for i in range(1, len(str(n)) + 1)]) if x != x.replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int(x) <= n])


# Here is my real answer, a straight forward iterative stack solution that builds
# prefixes and keeps count when they are valid

import itertools


class Solution:
    def confusingNumberII(self, n: int) -> int:
        temp_n = n

        num_digits = len(str(n))
        # num_digits = 0
        # while temp_n:
        #     num_digits += 1
        #     temp_n //= 10

        ans = ["6", "9"]
        stack = []
        num_confusing_nums = 2
        # were actually going to use strings here to take advantage of concat and reverse
        new_stack = ["1", "6", "8", "9"]
        valid_digits = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        for i in range(num_digits - 1):
            stack = new_stack
            new_stack = []
            for j in stack:
                for k in valid_digits:
                    new_num = j + k
                    new_stack.append(new_num)
                    confused_num = "".join([valid_digits[x] for x in new_num[::-1]])
                    if int(new_num) > n:
                        # ans += new_stack
                        return num_confusing_nums
                    if new_num != confused_num:
                        num_confusing_nums += 1

        return num_confusing_nums


# full_list = len(
#     [
#         y
#         for y in [
#             "".join(x)
#             for x in (
#                 ["6", "9"]
#                 + list(
#                     itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"])
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#                 + list(
#                     itertools.product(
#                         ["1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                         ["0", "1", "6", "8", "9"],
#                     )
#                 )
#             )
#         ]
#         if y != y.replace("6", "X").replace("9", "6").replace("X", "9")[::-1]
#         and int(y) <= n
#     ]
# )
# print(full_list)


# thing = len([y for y in ["".join(x) for x in ( \
#            ["6", "9"] \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            )] if y != y.replace('6', 'X').replace('9', '6').replace('X', '9')[::-1] and int(y) <= n])


# thing = len([y for y in ["".join(x) for x in ( \
#            ["6", "9"] \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"], ["0", "1", "6", "8", "9"])) \
#            )] if y != y.replace('6', 'X').replace('9', '6').replace('X', '9')[::-1] and int(y) <= n])
# print(thing)

# listy = ["6", "9"] + list(itertools.product(["1", "6", "8", "9"], ["0", "1", "6", "8", "9"]))
# listy = list(itertools.product(["0", "1", "6", "8", "9"] for _ in range(1)))
# listy = list(itertools.product(["0", "1", "6", "8", "9"], repeat=len(str(n))))

# listy = list(itertools.product(["0", "1", "6", "8", "9"], repeat=len(str(n))))
# thing = len(["".join(x) for x in list(itertools.product(["0", "1", "6", "8", "9"], repeat=len(str(n)))) if x != x.replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int("".join(x)) <= n])6

# thing = len([y for y in ["".join(x) for x in list(itertools.product(["0", "1", "6", "8", "9"], repeat=len(str(n))))] if y != y.replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int(y) <= n])
# mump = list(itertools.product(["1", "6", "8", "9"], repeat=len(str(n))))
# mumpsy = [x for x in mump if x != "".join(x).replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int("".join(x)) <= n]

# repeats = list(
#     itertools.chain(
#         *[
#             list(itertools.product(["0", "1", "6", "8", "9"], repeat=i))
#             for i in range(1, 4)
#         ]
#     )
# )
#
# pass
# mumpsy = [
#     x
#     for x in repeats
#     if "".join(x)
#     != "".join(x).replace("6", "X").replace("9", "6").replace("X", "9")[::-1]
#     and int("".join(x)) <= n
# ]
# pass

# converted = set("".join(x).lstrip("0") for x in list(itertools.chain(*[list(itertools.product(["0", "1", "6", "8", "9"], repeat=i)) for i in range(1, 4)])))

# converted = set("".join(x).lstrip("0") for x in list(itertools.chain(*[list(itertools.product(["0", "1", "6", "8", "9"], repeat=i)) for i in range(1, 4)])))
# mumpsy = sorted([int(x) for x in converted if x != x.replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int(x) <= n])

n = 195
# final_ans = len([x for x in set("".join(x).lstrip("0") for x in list(itertools.chain(*[list(itertools.product(["0", "1", "6", "8", "9"], repeat=i)) for i in range(1, len(str(n))+ 1) ]))) if x != x.replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int(x) <= n])
# final_ans = sum([1 for x in set("".join(x).lstrip("0") for x in itertools.chain(*[itertools.product(["0", "1", "6", "8", "9"], repeat=i) for i in range(1, len(str(n)) + 1)])) if x != x.replace("6", "X").replace("9", "6").replace("X", "9")[::-1] and int(x) <= n])
# final_ans = [
#     x
#     for x in set(
#         "".join(x).lstrip("0")
#         for x in itertools.chain(
#             *[
#                 itertools.product(["0", "1", "6", "8", "9"], repeat=i)
#                 for i in range(1, len(str(n)) + 1)
#             ]
#         )
#     )
#     if x != x.replace("6", "X").replace("9", "6").replace("X", "9")[::-1]
#     and int(x) <= n
# ]

# pass
