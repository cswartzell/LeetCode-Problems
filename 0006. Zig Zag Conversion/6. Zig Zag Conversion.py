s = "PAYPALISHIRING"
numRows = 3

if numRows == 1:
    print(s)
n = 2 * numRows - 2
lenstr = len(s)
step_a = 0
step_b = 0

new_str = ""

for i in range(numRows):
    if i > lenstr - 1:
        print(new_str)
    new_str += s[i]
    step_a = n - (i*2)
    step_b = (i*2)

    curr_index = i
    while curr_index < lenstr:
        curr_index += step_a
        if curr_index < lenstr and step_a != 0:
            new_str += s[curr_index]
        curr_index += step_b
        if curr_index < lenstr and step_b != 0:
            new_str += s[curr_index]

print(new_str)