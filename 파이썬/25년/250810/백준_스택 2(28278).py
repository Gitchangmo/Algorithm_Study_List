import sys
input = sys.stdin.readline

N = int(input())

stack = []
cnt = -1
result = []

for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        result.append(stack.pop() if stack else -1)
    elif order[0] == 3:
        result.append(len(stack))
    elif order[0] == 4:
        result.append(0 if stack else 1)
    elif order[0] == 5:
        result.append(stack[-1] if stack else -1)

for i in result:
    print(i)