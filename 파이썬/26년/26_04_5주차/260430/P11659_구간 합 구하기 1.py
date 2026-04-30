import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

num_list = [0] * (N+1)

for i in range (1, N+1):
    num_list[i] = num_list[i-1] + nums[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(num_list[j] - num_list[i-1])