#1
# import sys
# input = sys.stdin.readline

# num = int(input())
# answer = []
# for _ in range(num):
#     A, B = map(int, input().split())
#     answer.append(A+B)

# for i in range(num):
#     print(f"Case #{i+1}: {answer[i]}")

#2
# import sys
# input = sys.stdin.readline

# num = int(input())
# A = []
# B = []
# for _ in range(num):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)

# for i in range(num):
#     print(f"Case #{i+1}: {A[i]} + {B[i]} = {A[i] + B[i]}")

#3
# import sys
# input = sys.stdin.readline
# num = int(input())

# arr = list(map(int, input().split()))
# find_num = int(input())
# print(arr.count(find_num))

#4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(N+1)]

for _ in range(M):
    ball1, ball2 = map(int, input().split())
    