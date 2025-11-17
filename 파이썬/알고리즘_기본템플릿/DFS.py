import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int,input().split())

graph = [[] for _ in range(V+1)]
matrix = [[0] * (V+1) for _ in range(V+1)]

# 인접리스트 ===============================
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

print(graph)
# ex.
# [[], [2, 3, 5], [1, 4], [1, 5], [2, 6], [1, 3, 6], [4, 5]]
# =========================================

# 인접행렬 =================================
for _ in range(E):
    start, end = map(int, input().split())
    matrix[start][end] = 1
    matrix[end][start] = 1

for i in range(E):
    print(matrix[i])
# ex.
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 1, 1, 0, 1, 0]
# [0, 1, 0, 0, 1, 0, 0]
# [0, 1, 0, 0, 0, 1, 0]
# [0, 0, 1, 0, 0, 0, 1]
# [0, 1, 0, 1, 0, 0, 1]
# [0, 0, 0, 0, 1, 1, 0]
# =========================================

# 스택 + 인접행렬 방식
stack = [1] # 첫번째부터 시작해서
visited = []

while stack:
    current = stack.pop()           # 스택에서 pop해서 현재 노드로 사용
    if current not in visited:      # 현재 노드가 방문한 기록이 없다면
        visited.append(current)     # 방문 기록에 추가
    
    for destination in range(V+1):  # 현재 노드의 행을 순회하면서 갈 수 있는 노드(destination)을 탐색
        if matrix[current][destination] and destination not in visited: # 갈 수 있는 노드가 있고 그 노드가 방문기록이 없다면
            stack.append(destination)  # 스택에 추가(다음 목적지 노드들)
        
print("경로 : ", *visited)

# 스택 + 인접리스트 방식
stack = [1]
visited = []

while stack:
    current = stack.pop()           # 스택에서 pop해서 현재 노드로 사용
    if current not in visited:      # 현재 노드가 방문한 기록이 없다면
        visited.append(current)     # 방문 기록에 추가

    for destination in graph[current]:  # 인접리스트에서 현재 노드가 방문할 수 있는 목적지들 탐색
        if destination not in visited:  # 해당 목적지가 방문했던 적이 없다면
            stack.append(destination)   # 스택에 추가 (다음 목적지 노드들)

print("경로 : ", *visited)

# 재귀 + 인접 행렬 방식
def dfs(n):
    if n not in visited:
        visited.append(n)

    for destination in range(V+1):
        if matrix[n][destination] and destination not in visited:
            dfs(destination)

visited = []

dfs(1)

print("경로 : ", *visited)
