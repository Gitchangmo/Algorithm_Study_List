import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

Q = deque()

for i in range(N):
    Q.append(i+1)

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q[0])