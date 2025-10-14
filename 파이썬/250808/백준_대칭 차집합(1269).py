A, B = map(int, input().split())

num = list(map(int,input().split()))
set_A = set(num)

num = list(map(int,input().split()))
set_B = set(num)

newset_A = set_A - set_B
newset_B = set_B - set_A
result = newset_A | newset_B
print(len(result))