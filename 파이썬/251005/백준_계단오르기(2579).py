import sys
input = sys.stdin.readline

n = int(input())

stairs = [0] * (n)
dp = [0] * n

for i in range(n):
    stairs[i] = int(input())

if n == 1:
    print(stairs[0])
    exit(0)
if n == 2:
    print(stairs[0] + stairs[1])
    exit(0)
    
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n-1])