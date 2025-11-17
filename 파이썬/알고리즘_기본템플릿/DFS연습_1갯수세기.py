# 맵의 크기 N이 주어졌을 때,
# 해당 맵에서 1이 연속되어 붙어있는 구간의 1 개수를 구하기
# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000


def DFS(r, c):
    global cnt
    maps[r][c] = 0 # 현재 위치가 1이었으니 0으로 바꾸고
    cnt += 1       # 카운터 1 증가

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr<0 or nr>=N or nc<0 or nc>=N: # 이동 결과 맵밖을 나가면
            continue
        if maps[nr][nc] == 0: # 이동한 위치가 0 이면
            continue
        DFS(nr, nc) # 1인 방향으로 다시 DFS 재귀적 호출 *여기서 재귀가 끝났더라도 탐색해야할 다른 방향 남아있다면 다시 탐색 진행
                    # 모든 방향 탐색하고 모든 재귀적 호출을 마치면 최상위 DFS를 종료하고 main으로 돌아감

dr = [-1, 0, 1, 0] # 행의 위치를 조절 위/아래
dc = [0, 1, 0, -1] # 열의 위치를 조절 오른쪽/왼쪽

N = int(input())

maps = [list(map(int, input())) for _ in range(N)]

# 맵을 순차적으로 돌면서 1인 구간 찾기
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            cnt = 0
            DFS(i, j) # 모든 재귀 호출을 마치고 저장된 cnt값을 출력
            print(cnt)

