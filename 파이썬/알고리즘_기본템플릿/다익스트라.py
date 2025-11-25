import heapq

def dijkstra(node_num, edges):

    dist = [999999999] * (node_num + 1) # 최솟값 찾는 거라서 최대한 큰값 저장 or 무한대값
    dist[1] = 0 # 시작점의 거리는 0으로 선언

    adj = [[] for _ in range(node_num+1)] 
    # adj = [[]] * (node_num+1) 이런 형태로 선언 금지! 왜냐면 각 리스트에 참조를 할때 2차원 배열형태에서
    # 각 행의 원소에 접근할 때 행별로 같은 주소를 참조하게 됨
    # 본 코드의 형태는 각 행의 원소들도 개별적으로 참조가 가능한데
    # 위 형태로 선언하게 되면 각 행의 개별 원소는 참조가 안되어 행 자체가 같은 하나의 주소로 참조가 됨. 

    for start, end, weight in edges:        # 그래프 연결 정보에서 시작점, 목적지, 가중치를 가져옴
        adj[start].append([weight, end])    # 각 시작점에 [가중치, 목적지] 형태로 저장

    heap = [(0, 1)] # 힙에 현재 시작점 정보 저장

    while heap: # 힙이 빌때까지 반복
        cur_dist, cur_node = heapq.heappop(heap)    # 현재노드의 거리(가중치)와 현재 노드를 꺼내옴 힙에서

        if cur_node == node_num:        # 현재 노드가 최종 목적이 노드와 같다면
            return dist[cur_node]       # 최종 목적지까지의 거리 반환
        if dist[cur_node] < cur_dist:   # 현재 노드까지의 거리가 현재 노드의 거리(가중치)보다 작다면
            continue    # 현재 노드는 패스. 건너뜀

        for weight, next_node in adj[cur_node]:     # 현재 노드에서 갈 수 있는 노드들을 차례로 순회해서
            if dist[next_node] > (best_dist := weight + dist[cur_node]):    # 다음 노드까지의 거리가
                                                    # (현재 노드까지의 거리 + 현재 노드의 거리(가중치)보다 크다면
                dist[next_node] = best_dist # 다음 노드까지의 거리를 방금 비교한 거리로 업뎃
                heapq.heappush(heap, (best_dist, next_node))    # 그리고 힙에 그 새로운 거리와 다음 노드 푸시


print(dijkstra(5, [[1,2,3],[3,5,1],[1,5,10],[4,5,3],[2,4,1],[3,4,4],[1,3,2]]))