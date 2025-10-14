N, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(key=lambda x: -x)
print(arr[k-1])