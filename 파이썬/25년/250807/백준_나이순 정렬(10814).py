N = int(input())

arr = []

for i in range(N):
    age, name = input().split()
    arr.append((int(age), name, i)) # 튜플 형태로 저장

arr.sort(key= lambda x:(x[0], x[2]))

for age, name, _ in arr: # arr 리스트 순회
    print(age, name)