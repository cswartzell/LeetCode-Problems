"""03-13-2022 LeetCode 1249. Minimum Remove to Make Valid Parentheses"""
s = "lee(t(c)o)de)"

p_count = 0
x = 0
while x < len(s):
    vis = s[x]
    if s[x] == "(":
        p_count += 1
    if s[x] == ")":
        p_count -= 1
        if p_count < 0:
            p_count += 1
            s = s[:x] + s[min((x + 1), len(s)) :]
            x -= 1
    x += 1

p_count = 0
x = len(s) - 1
while x >= 0:
    vis = s[x]
    if s[x] == ")":
        p_count += 1
    if s[x] == "(":
        p_count -= 1
        if p_count < 0:
            p_count += 1
            s = s[:x] + s[min((x + 1), len(s)) :]
            # x += 1
    x -= 1
# return s
print(s)
