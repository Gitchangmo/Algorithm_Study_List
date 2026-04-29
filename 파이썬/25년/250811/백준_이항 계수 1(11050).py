import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def fact(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

answer = fact(N) // (fact(N-K) * fact(K)) # 이항계수 공식 : n! / (k! * (n-k)!)

print(answer)