n = int(input())

dic = {}
for i in range(n):
    name, state = input().split()
    if state == 'enter':
        if name not in dic:
            dic[name] = state
    else:
        if name in dic:
            del dic[name]

dic = sorted(dic, reverse=True)

for name in dic:
    print(name)