import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

sum_n = [0] * (N+1)

reminder_count = [0] * M

for i in range(1, N+1):
    sum_n[i] += sum_n[i-1] + nums[i]
    reminder_count[sum_n[i] % M] += 1

answer = reminder_count[0]

for i in reminder_count:
    answer += i * (i-1) // 2
print(answer)