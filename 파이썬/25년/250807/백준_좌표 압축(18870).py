N = int(input())

arr = list(map(int, input().split()))

new_arr = list(set(arr))
new_arr.sort()
dict = {}
for i in range(len(new_arr)):
    dict[new_arr[i]] = i

print(*(dict[i] for i in arr))
