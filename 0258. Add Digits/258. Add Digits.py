num = 38

num_sum = 0
while True:
    num_sum += num % 10
    num = num // 10
    if num == 0:
        if num_sum <= 9:
            print(num_sum)
            break
        num = num_sum
        num_sum = 0
