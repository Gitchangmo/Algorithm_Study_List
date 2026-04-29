import sys
input = sys.stdin.readline

str = input().strip()

start = 0
end = len(str)-1
is_true = 1
while(start < end):
    if str[start] == str[end]:
        start+=1
        end-=1
    else: 
        is_true = 0
        break
print(is_true)