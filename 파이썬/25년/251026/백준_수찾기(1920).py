import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
find_nums = list(map(int, input().split()))

nums.sort() # 이분 탐색을 위해 리스트 정렬

for i in range(M):
    mid = 0
    start = 0
    end = len(nums)-1
    found = False
    while start <= end: # start가 end보다 커지는 경우에는 바로 정지
        mid = (start+end) // 2  # 중앙 인덱스값 구하기
        if find_nums[i] < nums[mid]:    # 중앙 인덱스의 숫자가 찾는 숫자보다 크다면
            end = mid - 1               # end 인덱스를 중앙 인덱스보다 -1 뺀 인덱스로 줌
        elif find_nums[i] > nums[mid]:  # 반대로 찾는 숫자보다 작다면? 
            start = mid + 1             # start 인덱스를 중앙 인덱스보다 +1 크게 줌
        else:                           # 만약 찾는 값과 같다면
            found = True                # 찾았다는 flag True로 변경
            break
        # 위 조건들에 의하면 만약 찾는 숫자가 리스트에 없다면 start인덱스가 end인덱스보다 커지기 때문에 종료됨(루프)
    
    if found:
        print(1)
    else:
        print(0)