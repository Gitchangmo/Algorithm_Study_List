import sys
input = sys.stdin.readline

num = int(input())
count = 0
maps = [[0] * 100 for _ in range(100)]

for _ in range(num):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            maps[x+i][y+j] = 1

for col in range(100):
    for row in range(100):
        if maps[col][row] == 1:
            count += 1
print(count)