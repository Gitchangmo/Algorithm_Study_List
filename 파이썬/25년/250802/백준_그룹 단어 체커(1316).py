import sys
input = sys.stdin.readline

num = int(input())

count = 0
for _ in range(num):
    str = input().strip()
    check = set() 
    prev_char = ''
    
    is_group = True

    for ch in str:
        if ch != prev_char:
            if ch in check:
                is_group = False
                continue
            check.add(ch)
        prev_char = ch
        
    if is_group:
        count += 1
    
print(count)