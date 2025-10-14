import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())

    def fact(num):
        result = 1
        for i in range(2, num+1):
            result *= i
        return result

    answer = fact(M) // (fact(M-N) * fact(N))
    result.append(answer)

for i in result:
    print(i)