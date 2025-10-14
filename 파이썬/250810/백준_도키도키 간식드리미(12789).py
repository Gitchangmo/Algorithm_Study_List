import sys
input = sys.stdin.readline

stack = []
next = 1

N = int(input())

line = list(map(int, input().split()))

for num in line:
    stack.append(num)
    while stack and stack[-1] == next:
        stack.pop()
        next += 1
    
if next != (N+1):
    print('Sad')
else: print('Nice')
    