import sys
input = sys.stdin.readline

str = input().strip()
str = str.upper()
dic = {}
for s in str:
    if s not in dic:
        dic[s] = 1
    else: dic[s] += 1
    
max_word = max(dic.values())
max_keys = [k for k,v in dic.items() if v == max_word]
if len(max_keys) > 1:
    print("?")
else: print(max_keys[0])