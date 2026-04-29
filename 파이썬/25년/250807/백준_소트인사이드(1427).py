N = int(input())

N = str(N)

arr = sorted(N, reverse=True)
print(int("".join(arr)))