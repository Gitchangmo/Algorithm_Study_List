import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)

result = 0

while start <= end:
    mid = (start+end) // 2
    if mid == 0:
        break

    count = 0
    for line in lines:
        count += line // mid
        
    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)