import sys
input = sys.stdin.readline

S = '0' + input().strip()
q = int(input())

count = [[0] * len(S) for _ in range(26)]

for alpha in range(26):
    for idx in range(1, len(S)):
        num = ord(S[idx]) - ord('a')
        if alpha == num:
            count[alpha][idx] = count[alpha][idx-1] + 1
        else:
            count[alpha][idx] = count[alpha][idx-1]
        
for i in range(q):
    alpha, s, e = input().split()
    s, e = int(s), int(e)
    
    idx = ord(alpha) - ord('a')
    print(count[idx][e+1] - count[idx][s])
