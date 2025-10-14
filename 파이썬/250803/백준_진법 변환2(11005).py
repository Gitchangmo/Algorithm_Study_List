import sys
input = sys.stdin.readline

N, B = map(int, input().split())
result = ''

while N > 0:
    share = N // B
    remain = N % B

    N //= B

    if 0 <= remain <= 9:
        remain = chr(ord('0') + remain)
    elif 10 <= remain <= 35:
        remain = chr(ord('A') + remain - 10)
    result = remain + result

print(result)