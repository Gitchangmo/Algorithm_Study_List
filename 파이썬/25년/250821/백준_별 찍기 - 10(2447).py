import sys
input = sys.stdin.readline

N = int(input())

def star(n):
    if n == 1:
        return "*"

    pattern = star(n//3)
    blank = " " * (n//3)

    result = []

    for i in pattern:
        result.append(i+i+i)
    for i in pattern:
        result.append(i+blank+i)
    for i in pattern:
        result.append(i+i+i)
    return result

print('\n'.join(star(N)))
        