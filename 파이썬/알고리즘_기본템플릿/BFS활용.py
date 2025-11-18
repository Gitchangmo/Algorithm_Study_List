def BFS(r, c):
    Q = []
    Q.append((r, c))
    dist[r][c] = 1  # 첫 시작점은 1로 지정 (깊이 : 1)

    # 다음 길이 없을 때까지 진행을 해서 첫 좌표로부터의 깊이를 구한다
    while Q:
        cur_r, cur_c = Q.pop(0) # 큐에서 가장 먼저 넣은 좌표를 빼옴
        
        for i in range(4):      # 4방향 탐색 진행
            nr = cur_r + dr[i]  # 다음 행 좌표 지정(y축)
            nc = cur_c + dc[i]  # 다음 열 좌표 지정(x축)

            if nr < 0 or nr >= N or nc < 0 or nc >= N:   # 맵 밖으로 나가면 해당 좌표 건너뜀
                continue
            if arr[nr][nc] == 0 or dist[nr][nc] != 0:    # 해당 좌표가 0이거나(길없음) 이미 방문한 길이라면 건너뜀
                continue

            Q.append((nr, nc))  # 해당 좌표에서 갈 수 있는 모든 다음 목적지 저장(4방향 탐색 중 길이 있는 방향)
            dist[nr][nc] = dist[cur_r][cur_c] + 1   # 다음 목적지인 좌표들의 깊이를 1만큼 더해줌

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]   # 맵을 생성
dist = [[0] * N for _ in range(N)]      # 방문기록을 저장하는 지도 초기엔 모두 0

for i in range(N):
    for j in range(N):  # 모든 좌표를 순차적으로 탐색 
        if arr[i][j] == 1 and dist[i][j] == 0:  # 해당 좌표가 1이고(길임) 방문한 적이 없다면
            BFS(i, j)   # BFS 진행 (해당 좌표로부터 최대 깊이 탐색)

for d in dist:
    print(*d)