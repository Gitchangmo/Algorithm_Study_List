T = int(input())

inputs = [int(input()) for _ in range(T)]

max_num = max(inputs)

is_prime = [True] * (max_num+1)
is_prime[0] = is_prime[1] = False
    
for i in range(2, int(max_num**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, max_num+1, i):
            is_prime[j] = False


result = []

for num in inputs:
    count = 0
    for i in range(2, num//2+1):
        if is_prime[i] and is_prime[num-i]:
            count += 1
    result.append(count)

for i in range(len(result)):
    print(result[i])