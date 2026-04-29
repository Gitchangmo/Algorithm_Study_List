import sys
input = sys.stdin.readline

result = []

while True:
    line = input().rstrip('\n')

    stack = []
    flag = True
    if line == ".":
        break
    
    for w in line:
        if w == '(':
            stack.append(w)
        elif w == '[':
            stack.append(w)
        elif w == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            stack.pop()
        elif w == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            stack.pop()

    if flag and not stack:
        result.append('yes')
    else: result.append('no')

for i in result:
    print(i)