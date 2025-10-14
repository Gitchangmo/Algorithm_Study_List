N = int(input())

result = 0
for num in range(1, N):
    cur_num = num
    sum = 0
    while num > 0:
        sum += num%10
        num //= 10
    if cur_num + sum == N:
        result = cur_num
        break
print(result)