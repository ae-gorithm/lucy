import sys
input = sys.stdin.readline

# 연결요소는 무조건 dfs
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


# 입력 graph받기
n, m = map(int, input().split())

graph = [[] for i in range(n+1)] #1-based
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False]*(n+1) #1-based
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1
print(count)