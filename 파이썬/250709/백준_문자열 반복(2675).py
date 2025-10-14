import sys
input = sys.stdin.readline


num = int(input())
answer = []
str = ""
for _ in range(num):
    R, S = input().split()
    R = int(R)
    for i in range(len(S)):
        str += S[i] * R
    answer.append(str)
    str = ""
for item in answer:
    print(item)