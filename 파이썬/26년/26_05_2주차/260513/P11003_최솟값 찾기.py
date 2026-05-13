import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
D = list(map(int, input().split()))

Q = deque()

for i in range(N):
    while Q and Q[-1][1] > D[i]:
        Q.pop()
    Q.append((i, D[i]))
    if Q[0][0] <= i - L:
        Q.popleft()
    print(Q[0][1], end=' ')