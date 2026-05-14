import sys
input = sys.stdin.readline

n = int(input())

stack = []
stack_idx = 1
answer = []
result = True
nums = []

for i in range(n):
    n = int(input())
    nums.append(n)

for num in nums:
    if num > stack_idx:
        while stack_idx <= num:
            stack.append(stack_idx)
            stack_idx += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        stack_num = stack.pop()
        if num < stack_num:
            print("NO")
            result = False
            break
        answer.append('-')

if result:
    for i in answer:
        print(i)