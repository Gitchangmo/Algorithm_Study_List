import sys
input = sys.stdin.readline

N, B = input().split()

B = int(B)
square = 0
result = 0
for ch in reversed(N):
    if ch >= '0' and ch <= '9':
        ch = ord(ch) - ord('0')
    elif ch >= 'A' and ch <= 'Z':
        ch = ord(ch) - ord('A') + 10
    result += ch * (B ** square)
    square += 1

print(result)