import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [1] * N             # 각 원소들은 자기 자신 자체로 이미 1개의 수열을 가지기 때문에 1로 초기화해줌

for i in range(1, N):    # 1부터 모든 원소 순회
    for j in range(i):   # i번째 전까지의 원소를 순회함 (현재 원소의 앞에 위치한 모든 원소들)
        if seq[j] < seq[i]:     # 순서대로 순회하면서 현재 원소보다 작은지 비교함. 현재원소보다 작은 게 있다면
            dp[i] = max(dp[i], dp[j] + 1)   # 현재 원소의 값을 변경 (현재원소보다 작은 특정원소의 값에 1을 더한것과 비교)
                                            # 최댓값 저장
print(max(dp))
