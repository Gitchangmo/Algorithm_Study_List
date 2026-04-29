import sys
input = sys.stdin.readline

N = 9

maps = [list(map(int, input().split())) for _ in range(N)]

col_check = [[False] * 10 for _ in range(9)]
row_check = [[False] * 10 for _ in range(9)]
box_check = [[False] * 10 for _ in range(9)]

zeros = []

for r in range(N):
    for c in range(N):
        if maps[r][c] == 0:
            zeros.append((r,c))
        else:
            num = maps[r][c]
            box_idx = (r//3) * 3 + (c//3)
            col_check[c][num] = True
            row_check[r][num] = True
            box_check[box_idx][num] = True

len_zeros = len(zeros)

def dfs(index):
    if index == len_zeros:
        for i in range(N):
            print(*maps[i])
        sys.exit(0)

    r, c = zeros[index]
    box_idx = (r//3) * 3 + (c//3) 
    
    for num in range(1, 10):
        if not col_check[c][num] and not row_check[r][num] and not box_check[box_idx][num]:
            maps[r][c] = num
            col_check[c][num] = True
            row_check[r][num] = True
            box_check[box_idx][num] = True
            
            dfs(index+1)

            maps[r][c] = 0
            col_check[c][num] = False
            row_check[r][num] = False
            box_check[box_idx][num] = False
        

dfs(0)