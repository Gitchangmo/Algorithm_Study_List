
''' 그리디는 현재 가장 최선의 선택을 하여 최적해를 구하는 알고리즘이다. '''
''' 최소 횟수, 최대 가치, 최소 비용 등을 구하는 문제에 사용 '''
''' 정렬한 뒤 순서대로 처리하면 답이 나오는 경우가 많다. '''
''' *문제에서 매 순간의 최적해가 전체의 최적해가 됨이 보장될 때 사용 가능 '''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0

for coin in reversed(coins):
    if k >= coin:
        num_to_use = k//coin
        count += num_to_use
        k %= coin
    
    if k == 0:
        break

print(count)