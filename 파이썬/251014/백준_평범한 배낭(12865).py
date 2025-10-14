import sys
input = sys.stdin.readline

N, K = map(int, input().split())

items = []
for i in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [[0] * N for _ in range(K+1)]

for W, V in items:
    print(W, V)

for i in range(K+1):
    print(dp[i])