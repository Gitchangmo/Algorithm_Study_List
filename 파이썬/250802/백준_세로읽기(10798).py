import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(5)]

result = ''

for col in range(15): # 최대 길이 15까지 반복
    for row in range(5): # 입력한 문자열 5개이니 5번 반복 
        if col < len(arr[row]): # 현재 열 번호가 행의 길이보다 작을 때만 -> 이 조건을 만족안하면 열 인덱스가 해당 행의 인덱스를
                                # 벗어나는 크기기 때문에 패스함
            result += arr[row][col] # 현재 행,열의 값 더함
print(result)