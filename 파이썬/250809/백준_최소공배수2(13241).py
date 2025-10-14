def GCD(A, B):
    while B != 0:
        A, B = B, A%B
    return A

A, B = map(int, input().split())
gcd = GCD(A, B)
LCM = A*B // gcd

print(LCM)