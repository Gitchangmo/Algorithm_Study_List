import sys
input = sys.stdin.readline

memo =[[[0] * 21 for _ in range(21)] for _ in range(21)]  # 메모에 저장할 리스트 생성 3차원

def dp(a,b,c):  
    if a<=0 or b<=0 or c<=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dp(20, 20, 20)
    if memo[a][b][c]:
        return memo[a][b][c]
    if a<b and b<c:
        memo[a][b][c] = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
        return memo[a][b][c]
    
    memo[a][b][c] = dp(a-1,b,c) + dp(a-1,b-1,c) + dp(a-1,b,c-1) - dp(a-1,b-1,c-1)
    return memo[a][b][c]


while(True):
    a, b, c = map(int, input().split())

    if a==-1 and b==-1 and c==-1:
        break

    print(f"w({a}, {b}, {c}) = {dp(a,b,c)}")