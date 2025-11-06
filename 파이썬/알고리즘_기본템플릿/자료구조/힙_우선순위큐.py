import heapq

''' 최댓값, 최솟값을 항상 O(logN)의 속도로 빠르게 찾아내고 삭제하는 자료구조이다. '''
''' 다익스트라 알고리즘의 핵심이 되는 자료구조. '''

# --- 최소힙 ---
min_heap = []

heapq.heappush(min_heap, 4) 
print(min_heap) # [4]
heapq.heappush(min_heap, 2)
print(min_heap) # [2, 4]
heapq.heappush(min_heap, 6)
print(min_heap) # [2, 4, 6]

if min_heap:
    small = heapq.heappop(min_heap)
    print(small) # 2


# --- 최대힙 ---
max_heap = []

heapq.heappush(max_heap, -3)
print(max_heap) # [-3]
heapq.heappush(max_heap, -8)
print(max_heap) # [-8, -3]
heapq.heappush(max_heap, -1)
print(max_heap) # [-8, -3, -1]

if max_heap:
    max = heapq.heappop(max_heap)
    print(-max) # 8