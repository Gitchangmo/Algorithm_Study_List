import sys
input = sys.stdin.readline

N = int(input())

answer = [0] * N                            # 수열의 오큰수 저장할 리스트
stack = []
A = list(map(int, input().split()))         # 수열 값 입력 [A1, A2, A3 ...]

for i in range(N):                          # 수열 갯수 N만큼 반복 순서대로 idx 접근
    while stack and A[stack[-1]] < A[i]:    # 스택이 비어있지 않고, 스택의 최상단에 저장된 값의(인덱스) 수열 인덱스가 현재 수열 값보다 작다면?
        answer[stack.pop()] = A[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

for i in answer:
    sys.stdout.write(str(i) + " ")


''' 이 풀이에서 중요한 점은 stack에 수열의 인덱스를 저장하여 사용한다는 것과 '''
''' 오큰수를 찾았을 때는, answer에 답을 추가하는 과정에서 stack.pop()을 해주어야 무한루프에 안 빠짐 '''