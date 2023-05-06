# huh, its just the nth fibanocci number. Well, here goes
a, b, c = 0, 1, 1

for i in range(n - 1):
    a = b
    b = c
    c = a + b
return c
