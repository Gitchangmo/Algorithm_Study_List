N, M = map(int,input().split())

numTOname = {}
nameTOnum = {}

for i in range(1, N+1):
    pocketmon = input()
    numTOname[i] = pocketmon
    nameTOnum[pocketmon] = i

result = []
for i in range(M):
    name = input()
    if name.isdigit():
        name = int(name)
        result.append(numTOname[name])
    elif name.isalpha():
        result.append(str(nameTOnum[name]))

print('\n'.join(result))