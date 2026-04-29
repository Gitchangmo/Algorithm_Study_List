import sys
input = sys.stdin.readline

str = input().strip()
alpha = [-1] * 26

for idx, w in enumerate(str):
    aidx = ord(w) - ord('a')
    if alpha[aidx] == -1:
        alpha[aidx] = idx
print(*alpha)