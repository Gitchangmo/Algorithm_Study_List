import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}

for _ in range(N):
    word = input().strip()
    if len(word) < M:   
        continue
    dict[word] = dict.get(word, 0) + 1

sorted_dict = sorted(dict.items(), key= lambda item: (-item[1], -len(item[0]), item[0]))

for i in sorted_dict:
    print(i[0])