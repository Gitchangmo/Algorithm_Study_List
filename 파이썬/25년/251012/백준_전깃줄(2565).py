import sys
input = sys.stdin.readline

N = int(input())

wires = []

for i in range(N):
    A, B = map(int, input().split())
    wires.append((A,B))             # wires 리스트에 튜플 형태로 A, B점 저장함

wires.sort()    # wires를 A점 기준으로 정렬 (아무런 지정없으면 가장 앞 원소 기준)

dp = [1] * N    # LIS를 위한 dp 배열 초기화

B_wires = [wire[1] for wire in wires]  # wires에 튜플 형태로 저장되어 있기 때문에 wire 튜플의 두번째 즉 B라인 점을 모아 저장

# LIS 구하기
for i in range(N):
    for j in range(i):
        if B_wires[j] < B_wires[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))