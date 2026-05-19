import sys

input = sys.stdin.readline

N = int(input())
num_list = []

for i in range(N):
    num = int(input())
    num_list.append(num)

for i in range(N-1):
    for j in range(N-1-i):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp

for i in range(N):
    print(num_list[i])