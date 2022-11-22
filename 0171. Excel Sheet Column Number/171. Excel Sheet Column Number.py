"""02-22-2022 Leetcode 171. Excel Sheet Column Number"""
columnTitle = "BA"

big_A = ord("A") + 1
col_num = 0
for i in range(len(columnTitle) - 1, -1, -1):
    new_char = big_A - ord(columnTitle[i])
    bumped_up = 26 * (len(columnTitle) - i - 1)
    if bumped_up == 0:
        bumped_up = 1
    col_num += new_char * bumped_up
print(int(col_num))
