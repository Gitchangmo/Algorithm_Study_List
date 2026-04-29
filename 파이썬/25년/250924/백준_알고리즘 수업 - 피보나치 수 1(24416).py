import sys
input = sys.stdin.readline

n = int(input())

fibo_arr = [0] * (n+1)

def fibonacci(n):
    global count
    fibo_arr[1] = 1
    fibo_arr[2] = 1

    for i in range(3, n+1):
        fibo_arr[i] = fibo_arr[i-1] + fibo_arr[i-2]
    return fibo_arr[n]

print(fibonacci(n), n-2)