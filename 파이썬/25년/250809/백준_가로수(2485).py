def GCD(A, B):
    while B != 0:
        A, B = B, A%B
    return A

N = int(input())

arr = []
gap = []
for _ in range(N):
    num = int(input())
    arr.append(num)

for i in range(1, len(arr)):
    gap.append(arr[i] - arr[i-1])

gcd = gap[0]
for num in gap[1:]:
    gcd = GCD(gcd, num)

result = 0
for num in gap:
    result += num // gcd -1

print(result)