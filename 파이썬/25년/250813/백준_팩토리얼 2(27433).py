import sys
input = sys.stdin.readline


def fact(n):
    if n < 2:
        return 1
    return n * (fact(n-1))

N = int(input())

print(fact(N))