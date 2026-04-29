import sys
input = sys.stdin.readline

N = int(input())

Q = []
result = []
cursor = 0

for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        Q.append(order[1])
    elif order[0] == 'pop':
        if cursor >= len(Q):
            result.append(-1)
        else: 
            result.append(Q[cursor])
            cursor += 1
    elif order[0] == 'size':
        result.append(len(Q) - cursor)
    elif order[0] == 'empty':
        if cursor >= len(Q):
            result.append(1)
        else: result.append(0)
    elif order[0] == 'front':
        if cursor >= len(Q):
            result.append(-1)
        else: result.append(Q[cursor])
    elif order[0] == 'back':
        if cursor >= len(Q):
            result.append(-1)
        else: result.append(Q[-1])

for i in result:
    print(i)