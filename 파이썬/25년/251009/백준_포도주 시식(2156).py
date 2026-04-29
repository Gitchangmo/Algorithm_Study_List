import sys
input = sys.stdin.readline

n = int(input())

wines = []
for _ in range(n):
    wine = int(input())
    wines.append(wine)

dp = [0] * 10001

if n == 1:
    print(wines[0])
    exit(0)

dp[0] = wines[0]
dp[1] = wines[0] + wines[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])

print(dp[n-1])