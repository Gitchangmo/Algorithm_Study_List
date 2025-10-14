import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
10
max_num = max(nums)

dp_increase = [1] * N
dp_decrease = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):    
        if nums[j] < nums[i]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

result = [0] * N

for i in range(N):
    result[i] = dp_increase[i] + dp_decrease[i] - 1

print(max(result))