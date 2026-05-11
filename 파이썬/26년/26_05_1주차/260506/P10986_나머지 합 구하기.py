import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

Sum = [0] * N
Counter = [0] * M

Sum[0] = nums[0]
answer = 0

for i in range(1, N):
    Sum[i] = Sum[i-1] + nums[i]

for i in range(N):
    remainder = Sum[i] % M
    if remainder == 0:
        answer += 1
    Counter[remainder] += 1

for i in range(M):
    if Counter[i] > 1:
        answer += (Counter[i] * (Counter[i] - 1) // 2)

print(answer)