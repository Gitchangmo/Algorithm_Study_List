import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bucket = [i for i in range(N+1)]
for _ in range(M):
    ball1, ball2 = map(int, input().split())
    tmp = bucket[ball1]
    bucket[ball1] = bucket[ball2]
    bucket[ball2] = tmp
print(*bucket[1:])
