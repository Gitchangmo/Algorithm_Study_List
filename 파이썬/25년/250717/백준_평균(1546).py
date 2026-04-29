import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
sum = 0
max_score = max(arr)
for i in arr:
    sum += i/max_score*100
    
print(sum/N)