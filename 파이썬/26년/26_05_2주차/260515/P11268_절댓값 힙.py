import heapq
import sys

input = sys.stdin.readline

N = int(input())

Q = []

for i in range(N):
    num = int(input())
    if num == 0:
        if Q:
            print(heapq.heappop(Q)[1])      # 우선순위 큐에서 뽑은 최소값의(튜플) 실제 입력값인 num을 [1] 출력
        else:
            print(0)
            
    else:
        heapq.heappush(Q, (abs(num), num))  # 튜플 형태의 (절댓값 num, 입력받은 num)를 큐에 넣어 힙 구조로 정렬한다.
                                            # 이 때, 큐에 넣는 값의 순서대로 정렬의 순서가 정해지므로, 절댓값 기준 정렬 후,
                                            # 그 뒤 num의 양수/음수 비교 후 작은 값 순서대로 정렬한다.
                                            # 우선순위 큐(최소 힙)의 원리를 활용해 해결하는 문제