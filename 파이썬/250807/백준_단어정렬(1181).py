N = int(input())

arr = []
for _ in range(N):
    word = input()
    arr.append(word)

arr = list(set(arr))
arr.sort(key= lambda x: (len(x), x))

for i in range(len(arr)):
    print(arr[i])