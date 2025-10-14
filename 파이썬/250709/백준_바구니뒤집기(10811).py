import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)] # 바구니 번호는 1부터시작, 하지만 인덱스는 -1씩 작음

for _ in range(M):
    start, end = map(int, input().split()) # 바구니번호
    arr[start-1:end] = arr[start-1:end][::-1] # 입력 값(바구니번호)에서 -1을 빼야 인덱스가 맞음

print(*arr)