import sys
input = sys.stdin.readline

dict = {}
for _ in range(10):
    num = int(input())

    ans = num % 42
    dict[ans] = 1

else : print(len(dict))