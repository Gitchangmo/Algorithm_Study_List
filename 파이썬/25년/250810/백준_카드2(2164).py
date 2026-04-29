from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Q = deque()

for i in range(1, (N+1)):
    Q.append(i)

while 1 < len(Q):
    Q.popleft()
    Q.append(Q.popleft())

print(Q.pop())