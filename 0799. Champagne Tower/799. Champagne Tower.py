"""03-05-2022 Leetcode 799. Champagne Tower"""

poured = 23
query_row = 33
query_glass = 17
cups = []
for i in range(query_row + 1):
    cups.append([])
    for j in range(0, i + 1):
        cups[i].append(0.0)

# ok, so we COULD create the pyramid row by row AS we pour, and once
# there is no overflow we could stop making rows at that point. This could mean much better
# space efeciency if the requested row/glass is huge, but the pour is small
# We'd simply return 0 if the row/glass doesnt exist in our pyramid


overflow = poured
cups[0][0] += overflow
overflowed = True
for row in range(query_row + 1):
    if overflowed:
        overflowed = False
        for cup in range(row + 1):
            if cups[row][cup] > 1:
                overflowed = True
                overflow = (cups[row][cup] - 1) / 2
                cups[row][cup] = 1.0  # can be removed after done with vis inspection
                if row < query_row:
                    cups[row + 1][cup] += overflow
                    cups[row + 1][cup + 1] += overflow
    else:
        break

print(cups[query_row][query_glass])


# #Well I'm doing this pretty stupid. This simulates the glasses poured one at a time... why?
# # we can literally just send them all at once, and the exact same reasoning works. Running again
# with just sending them all at once.... and it works logicwise but the stack is FAR too huge
# and it crashes and burns. Try again without sending the stack each time? this should be by reference
# anyway so it shouldnt be that big...

# def pourOne(cups, amount, row, cup):
#     cups[row][cup] += amount
#     if cups[row][cup] > 1:
#         overflow = cups[row][cup] - 1
#         cups[row][cup] = 1.0
#         if row < query_row: #if there is a row to flow to, otherwise spill that shit on the ground
#             pourOne(cups, overflow / 2, row + 1, cup)
#             pourOne(cups, overflow / 2, row + 1, cup + 1)

# pourOne(cup_stack, poured, 0, 0)

# print(cup_stack[query_row][query_glass])
