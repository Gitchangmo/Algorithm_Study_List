
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)
    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root


N = int(input())

parent = [i for i in range(N+1)]

union_parent(parent, 4, 5)

if find_parent(parent, 4) == find_parent(parent, 5):
    print("같은 집합입니다.")
else:
    print("다른 집합입니다.")