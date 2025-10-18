import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for i in range(N):
    coin = int(input())
    coins.append(coin)

count = 0

for i in range(N - 1, -1, -1):
    coin = coins[i]
    if K >= coin:
        num = K // coin
        count += num

        K %= coin
    if K == 0:
        break
    

print(count)