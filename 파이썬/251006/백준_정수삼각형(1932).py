import sys
input = sys.stdin.readline

n = int(input())

maps = []   # 입력값을 저장할 삼각형 맵 리스트 생성

for i in range(n):
    nums = list(map(int, input().split()))      # 입력값들을 리스트 형태로 저장
    maps.append(nums)                           # 삼각형 맵에 각 리스트를 단계별로 추가

dp = [[0] * i for i in range(1, n+1)]           # 각 단계 별 최댓값 저장할 dp 리스트 생성

dp[0][0] = maps[0][0]                           # 맨 위는 원소가 1이니 첫번째 입력값 저장

for i in range(1, n):                           # 삼각형의 2층부터 순회
    for j in range(i+1):                        # 2층의 모든 원소 순회
        if j == 0:                                  # 가장 왼쪽 원소를 구할 경우
            dp[i][j] = maps[i][j] + dp[i-1][j]      # 해당 위치 dp는 이전 층의 dp값과 현재 위치 입력값 더한 값
        elif j == i:                                # 가장 오른쪽 원소를 구할 경우
            dp[i][j] = maps[i][j] + dp[i-1][j-1]    # 해당 위치 dp는 이전 층 마지막 dp 값과 현재 위치 입력값 더한 값
        else:                                       # 그 외 가운데 위치 원소 구할 경우
            dp[i][j] = maps[i][j] + max(dp[i-1][j], dp[i-1][j-1])   # 이전 층의 대각선 왼쪽 위 dp랑 바로 위 dp중
                                                                    # 큰값과 현재 입력값 더한 것 중 최대값 저장
if n == 1:
    print(dp[0][0])
else:
    print(max(dp[n-1]))