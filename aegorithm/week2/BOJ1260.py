import sys
from collections import deque

# bfs(주변에 있는 것부터 탐색)
def bfs(nodes, start, visited):
    queue = deque([start]) # 시작노드
    visited[start] = True
    print(start, end=' ')
    
    while queue:
        v = queue.popleft()

        for i in sorted(nodes[v]):
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)

# dfs(한 붓 그리기)
def dfs(nodes, start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in sorted(nodes[start]):
        if not visited[i]:
            dfs(nodes, i, visited)

# 입력
n, m, v = map(int, input().split())

nodes = [[] for _ in range(n+1)]
for _ in range(m): # 정점이 아닌 간선 개수만큼 입력
    i, j = map(int, input().split())
    nodes[i].append(j)
    nodes[j].append(i) # 양방향

dfs_nodes = nodes[:] # deepcopy
visited = [0]*(len(nodes)+1)
dfs(dfs_nodes, v, visited)
print()

bfs_nodes = nodes[:] # deepcopy
visited = [0]*(len(nodes)+1)
bfs(bfs_nodes, v, visited)