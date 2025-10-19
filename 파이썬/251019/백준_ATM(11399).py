import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))

times.sort()

sum_times = [0] * (N+1)

for i in range(1, N+1):
    sum_times[i] = sum_times[i-1] + times[i-1]

print(sum(sum_times))