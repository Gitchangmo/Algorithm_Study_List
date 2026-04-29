import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
x_sum = []

for i in range(N):
    maps.append([0] + list(map(int, input().split())))
    temp = [0] * (N+1)
    for j in range(1, N+1):
        temp[j] = temp[j-1] + maps[i][j]
    x_sum.append(temp)

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    answer = 0
    for j in range(y1-1, y2):
        answer += x_sum[j][x2] - x_sum[j][x1-1]
    print(answer)