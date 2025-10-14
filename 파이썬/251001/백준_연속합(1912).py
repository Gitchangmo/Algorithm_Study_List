import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cur_max = arr[0]        # 맨 처음 원소를 최댓값으로
final_max = arr[0]      # 맨 처음 원소를 최댓값으로

for i in range(1, n):   # 1부터 끝까지 반복 (첫 원소는 제외)
    cur_max = max(arr[i], cur_max+arr[i])   # 현재 원소값과, 현재 최댓값 + 현재원소값 중 큰값으로 변경
                                            # 현재 원소가 -라면 당연히 최댓값에 포함 못되니 제외
    final_max = max(cur_max, final_max)     # 최종 최댓값과 현재 갱신된 최댓값을 비교해 큰값으로 변경

print(final_max)

"""
이 문제 원리는, 첫 원소부터 누적해서 연속된 값의 최댓값을 찾는건데,
첫원소와 다음원소를 더한 값과 다음 원소값을 비교해서 최댓값을 구할 때,
다음 원소가 -라면 현재 최댓값과 더했을 때 그것보다 더 커질 수가 없기 때문에
이전 원소까지의 누적된 최댓값이 현재 최댓값으로 갱신됨
그리고 최종 최댓값과 현재 최댓값을 비교해서 항상 실행 중 가장 큰 값만 저장하게 됨
"""