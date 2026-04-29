N = int(input())
result = -1
count = 0
for i in range(N // 5, -1, -1):
    new = N - (i * 5)
    count += 1
    if new % 3 == 0:
        result = i + (new // 3)
        break
print(result)
print(count)