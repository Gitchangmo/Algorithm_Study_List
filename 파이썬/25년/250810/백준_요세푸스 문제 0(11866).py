from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(range(1, N+1))
result = []
cursor = 0

while arr:
    cursor = (cursor + K - 1) % len(arr)
    result.append(arr.pop(cursor))


print("<" + ", ".join(map(str, result)) + ">")