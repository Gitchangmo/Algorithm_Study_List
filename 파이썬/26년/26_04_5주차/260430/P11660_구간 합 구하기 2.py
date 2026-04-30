import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maps = []

for _ in range(N):
    nums = list(map(int, input().split()))
    maps.append(nums)

prefix = [[0] * (N+1) for _ in range(N+1)]

for row in range(1, N+1):
    for col in range(1, N+1):
        prefix[row][col] = prefix[row-1][col] + prefix[row][col-1] - prefix[row-1][col-1] + maps[row-1][col-1]
    
for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    print(prefix[X2][Y2] - prefix[X1-1][Y2] - prefix[X2][Y1-1] + prefix[X1-1][Y1-1])
    