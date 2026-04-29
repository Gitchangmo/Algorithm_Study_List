from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

Q = deque()
result = []


for i in range(N):
    if A[i] == 0:
        Q.append(B[i])

if not Q:
    result.extend(C)
    
elif Q:
    for num in C:
        result.append(Q.pop())
        Q.appendleft(num)

print(*result)