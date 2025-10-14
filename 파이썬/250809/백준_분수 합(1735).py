def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

nume, deno = (a1*b2) + (a2*b1), b1*b2

gcd = GCD(nume, deno)

print((nume//gcd), (deno//gcd))
    