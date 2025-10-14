N = int(input())
cards = set(map(int, input().split()))

M = int(input())
result = list(map(int, input().split()))

for i, num in enumerate(result):
    if num in cards:
        result[i] = 1
    else: result[i] = 0

print(*result)