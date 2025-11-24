import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lines = [int(input()) for _ in range(N)]    # 가지고 있는 랜선들 입력

start = 1           # 가장 짧은 랜선길이 1부터 시작
end = max(lines)    # 가진 랜선 중 가장 긴 랜선의 길이까지

result = 0          # 동일하게 자를 수 있는 최대 길이

while start <= end: 
    total = 0
    mid = (start + end) // 2 # 중간 길이 부터 시작

    for line in lines:  # 현재 가진 모든 랜선들을 
        total += line // mid # 방금 만든 mid(중간 길이)로 나누어서 몫을 모두 더함
    if total >= K:      # 그렇게 자른 랜선의 갯수들이 목표 갯수 K보다 크다면? -> 더 길게 자를 수 있다는 것이기 때문에
        start = mid + 1 # 방금 mid보다 1 더 큰 길이부터 시작해 다시 최대 길이값 찾음
        result = mid    # 일단 지금까지의 가장 큰 값을 mid기 때문에 저장해둠(임시 저장)
    else:               # 만약 랜선의 합들이 목표갯수가 안된다?
        end = mid - 1   # 너무 길게 잘랐다는 뜻이니 1 더 작은 수까지 해서 적정값 다시 찾기
    
print(result)