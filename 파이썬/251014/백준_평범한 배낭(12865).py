import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물건 갯수와 최대 배낭 용량 입력

items = [(0,0)]     # 물건의 정보를 담을 리스트 생성 (튜플 형태로 저장)
for i in range(N):
    W, V = map(int, input().split())    # 물건정보 입력받음 무게, 가치
    items.append((W, V))                # 튜플로 저장

dp = [[0] * (K+1) for _ in range(N+1)]  # dp맵 생성 무게가 0일때와 물건정보 인덱스 맞추기 위해 각 +1 함

for i in range(1, N+1): # 각 물건에 대해
    for j in range(1, K+1): # # 배낭의 최대 용량까지
        W, V = items[i] # 해당 물건의 무게와 가치를 저장
        if j >= W:      # 해당 물건의 무게가 배낭의 최대용량보다 작거나 같으면
            dp[i][j] = max(dp[i-1][j], V + dp[i-1][j-W])   # 물건 넣기 전 가치와 물건 넣었을 떄 가치 중 큰값 저장
        else:
            dp[i][j] =dp[i-1][j]    # 용량이 작아 못 넣으니 넣기 전과 동일함
    

print(dp[N][K]) # 모든 물건을 다 확인한 후 최대 가치 값을 출력