import sys
input = sys.stdin.readline

N = int(input())

maps = [[True] * N for i in range(N)]

visited = []
count = 0

def dfs(start):
    if start in visited:
        return
    if start == start-1 or start == start+1:
        return
    for x in range(N):
        visited.append(x)

        dfs(x)