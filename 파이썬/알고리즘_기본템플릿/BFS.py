V, E = map(int, input().split()) # V : 정점 갯수, E : 간선 갯수

matrix = [[0] * (V+1) for _ in range(V+1)]  # 정점+1의 크기의 2차원 행렬 생성

for _ in range(V+1):
    start, end = map(int, input().split())  # 시작점, 끝점 입력
    
    matrix[start][end] = 1  # 양방향 인접행렬 생성
    matrix[end][start] = 1  # 양방향 인접핼렬 생성

Q = [1]         # 큐를 생성 (시작점 1과 함께)
visited = []    # 방문 기록리스트 생성

while Q:
    current = Q.pop(0)  # 큐에서 가장 먼저 들어간 원소 가져오기
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):  # 해당 정점에서 모든 정점까지 순회하며 목적지 찾기
        if matrix[current][destination] and destination not in visited: # 현재 정점에서 해당 목적지가 방문 리스트에 없다면
            Q.append(destination)   # 다음 목적지를 Q에 저장
        
print("이동 경로 : ", *visited)