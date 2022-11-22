s = "()()"

i = 0
new_s = []
while i < len(s):
    peek = s[i]
    if i + 1 < len(s) and s[i : i + 2] == "()":
        new_s.append(int(1))
        i += 1
    else:
        new_s.append(s[i])
    i += 1

while len(new_s) > 1:
    s = new_s.copy()
    new_s = []
    i = 0
    while i < len(s):
        j = 1
        sumd = s[i]
        if s[i] != "(" and s[i] != ")":
            while i + j < len(s) and s[i + j] != "(" and s[i + j] != ")":
                sumd += s[i + j]
                j += 1
        new_s.append(sumd)
        i += j

    s = new_s.copy()
    new_s = []
    i = 0
    while i < len(s):
        if (
            i < len(s) - 2
            and s[i] == "("
            and s[i + 1] != ")"
            and s[i + 1] != "("
            and s[i + 2] == ")"
        ):
            new_s.append(2 * s[i + 1])
            i += 3
            continue
        else:
            new_s.append(s[i])
            i += 1

print(new_s[0])
