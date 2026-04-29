N = int(input())

dic = {}
cards = list(map(int, input().split()))
for num in cards:
    dic[num] = dic.get(num, 0) + 1

M = int(input())
arr = list(map(int, input().split()))

result = []
for num in arr:
    result.append(dic.get(num, 0))

print(*result)