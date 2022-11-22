"""03-10-2022 Leetcode 247. Strobogrammatic Number II"""
n = 5

strobo_list = []
temp = []
for i in range(n):
    temp.append(1)
strobo_list.append(temp)

evodd = ((n - 1) % 2) / 2
mid = (n - 1) / 2
