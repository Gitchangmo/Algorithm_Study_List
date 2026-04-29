import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

result = []
for _ in range(n):
    num = int(input())
    while not is_prime(num):
        num += 1
    result.append(num)

for i in range(len(result)):
    print(result[i])