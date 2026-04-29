N, M = map(int, input().split())

maps = [input().strip() for _ in range(N)]

count_maps = 64

for row in range(N-7):
    for col in range(M-7):
        count_B = 0
        count_W = 0

        for x in range(8):
            for y in range(8):
                cur = maps[row+x][col+y] # 현재 위치 계속 갱신 
                if (x+y) % 2 == 0: # 시작점 : 0, 짝수 위치의 색깔. ------ 결과적으로 B/W중 하나기 때문에 둘 중 하나만 카운트증가
                    if cur != 'B': # 해당 위치 색깔이 B가 아니면 카운트 1증가
                        count_B += 1
                    if cur != 'W': # 해당 위치 색깔이 W가 아니면 카운트 1증가
                        count_W += 1
                else: # 홀수 위치의 색깔 = 짝수 위치의 색깔과 반대
                    if cur != 'B':
                        count_W += 1
                    if cur != 'W':
                        count_B += 1
        
        count_maps = min(count_maps, count_B, count_W)

print(count_maps)