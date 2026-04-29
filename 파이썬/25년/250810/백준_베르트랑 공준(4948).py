import sys
input = sys.stdin.readline

result = []

while True:
    prime_list = []
    n = int(input())
    if n == 0:
        break
    prime = []
    prime = [True] * (2*n+1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(2*n**0.5)+1):
        for j in range(i*i, 2*n+1, i):
            prime[j] = False
    
    for i in range(n+1, (2*n+1)):
        if prime[i]:
            prime_list.append(i)
    result.append(len(prime_list))
for i in range(len(result)):
    print(result[i])