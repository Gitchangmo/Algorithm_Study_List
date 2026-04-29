import sys
from decimal import Decimal, ROUND_HALF_UP
input = sys.stdin.readline

N = int(input())
arr = []
count = [0] * (N+1)

for _ in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

offset = 4000
count = [0] * 8001
for num in arr:
    count[num+offset] += 1

max_num = max(count)
modes = [i-offset for i, v in enumerate(count) if v == max_num]
mode = modes[1] if len(modes) > 1 else modes[0]

print(int((Decimal(sum(arr)) / Decimal(N)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
)
print(arr[N//2])
print(mode)
print(arr[-1] - arr[0])