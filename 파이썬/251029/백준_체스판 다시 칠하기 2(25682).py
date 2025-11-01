import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

map = [list(input().strip()) for _ in range(N)]

sum_w = [[0] * (M + 1) for _ in range(N + 1)]  # W색 기준 틀린 누적합
sum_b = [[0] * (M + 1) for _ in range(N + 1)]  # B색 기준 틀린 누적합

for i in range(1, N + 1):
    for j in range(1, M + 1):
        cur_ch = map[i - 1][j - 1] # 현재 문자(색)

        cost_W = 0
        cost_B = 0

        if (i + j) % 2 == 0: # 짝수일 때
            if cur_ch == 'B':   # 글자가 B라면 
                cost_W = 1      # W 비용 1증가
            if cur_ch == 'W':   # 글자가 W라면
                cost_B = 1      # B 비용 1증가
        else:
            if cur_ch == 'W':
                cost_W = 1
            if cur_ch == 'B':
                cost_B = 1

        sum_w[i][j] = sum_w[i-1][j] + sum_w[i][j-1] - sum_w[i-1][j-1] + cost_W  # 누적합 계산 2차원
        sum_b[i][j] = sum_b[i-1][j] + sum_b[i][j-1] - sum_b[i-1][j-1] + cost_B  # 누적합 계산 2차원

min_paint = K * K

for r in range(1, N - K + 2):
    for c in range(1, M - K + 2):

        R, C = r + K - 1, c + K - 1
        cost_W = sum_w[R][C] - sum_w[r-1][C] - sum_w[R][c-1] + sum_w[r-1][c-1] # W로 시작되는 패턴의 비용
        cost_B = sum_b[R][C] - sum_b[r-1][C] - sum_b[R][c-1] + sum_b[r-1][c-1] # B로 시작되는 패턴의 비용

        min_paint = min(min_paint, cost_W, cost_B)

print(min_paint)