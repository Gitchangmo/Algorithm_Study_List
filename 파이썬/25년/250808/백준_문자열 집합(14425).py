N, M = map(int, input().split())

result_set = set()
for _ in range(N):
    str1 = input()
    result_set.add(str1)

count = 0

for _ in range(M):
    str2 = input()
    if str2 in result_set:
        count += 1
    
print(count)