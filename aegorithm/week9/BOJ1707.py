import sys
# 유니온 파인드?
# find
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

# union
def union(u, v, parent):
    rootU = find(u, parent)
    rootV = find(v, parent)
    if rootU != rootV:
        if rootU < rootV:
            parent[rootU] = rootV
        else:
            parent[rootV] = rootU

# 입력
input = sys.stdin.readline
k = int(input())

for i in range(k):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        
        parent = union(u, v, parent)

# 출력
result = set()
for i in range():
    result.add(parent[i])

if len(result) > 1:
    print("NO")
else:
    print("YES")