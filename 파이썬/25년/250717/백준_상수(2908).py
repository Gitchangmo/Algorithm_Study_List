import sys
input = sys.stdin.readline

arr = list(input().split())

for idx, num in enumerate(arr):
    arr[idx] = num[::-1]

print(max(arr))