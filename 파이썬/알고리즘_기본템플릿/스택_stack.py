stack = []

stack.append(1)
print(stack) # [1]

stack.append(2)
print(stack) # [1, 2]

if stack:
    print(stack.pop()) # 2
    print(stack) # [1]

if stack:
    top = stack[-1] # 최상단 1. 가장 먼저 들어간 수

if not stack:
    print("stack is empty")