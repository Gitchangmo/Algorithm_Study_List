
''' M보다 크지 않은 카드 세 개의 합을 찾는 문제 '''
''' 브루트 포스는 무식하게 모든 경우를 다 시도하는 방법 '''

N, M = map(int, input().split())

cards = list(map(int, input().split()))

best_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            current_sum = cards[i] + cards[j] + cards[k]
            
            if current_sum <= M:
                best_sum = max(current_sum, best_sum)

print(best_sum)