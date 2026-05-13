import sys
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().strip()
A, C, G, T = map(int, input().split())

checkList = [A, C, G, T]
curList = [0] * 4

checkSecret = 0

Result = 0

def add(c):
    global checkList, curList, checkSecret

    if c == 'A':
        curList[0] += 1
        if curList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        curList[1] += 1
        if curList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        curList[2] += 1
        if curList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        curList[3] += 1
        if curList[3] == checkList[3]:
            checkSecret += 1

def remove(c):
    global checkList, curList, checkSecret

    if c == 'A':
        if curList[0] == checkList[0]:
            checkSecret -= 1
        curList[0] -= 1
    elif c == 'C':
        if curList[1] == checkList[1]:
            checkSecret -= 1
        curList[1] -= 1

    elif c == 'G':
        if curList[2] == checkList[2]:
            checkSecret -= 1
        curList[2] -= 1
    elif c == 'T':
        if curList[3] == checkList[3]:
            checkSecret -= 1
        curList[3] -= 1


for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    add(DNA[i])

if checkSecret == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    remove(DNA[j])
    add(DNA[i])
    if checkSecret == 4:
        Result += 1

print(Result)