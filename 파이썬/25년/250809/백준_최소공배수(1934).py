T = int(input())

def GCD(A, B):
    while B != 0:
        A, B = B, A%B
    return A

result = []
for i in range(T):
    A, B = map(int, input().split())
    gcd = GCD(A, B)
    LCM = A*B // gcd
    result.append(LCM)

for i in range(T):
    print(result[i])