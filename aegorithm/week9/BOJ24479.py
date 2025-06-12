import sys
#sys.setrecursionlimit(10**7)

# dfs
def dfs(r, graph, visited, count):
    global result

    next_idx = [0] * (n+1)
    stack = [r]

    while stack:
        u = stack[-1]
        idx = next_idx[u]

        if idx < len(graph[u]):
            v = graph[u][idx]
            next_idx[u] += 1
            if not visited[v]:
                visited[v] = True
                result[v] = count
                count += 1
                stack.append(v)
        else:
            stack.pop()

# 입력
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    # 양방향
    graph[u].append(v)
    graph[v].append(u) # 대입이 아니라 삽입...]

for i in range(1, n+1):
    graph[i].sort() # 마지막에 한 번씩만 정렬 => 힙큐보다 유리할 수 있음

result = [0] * (n+1)
result[r] = 1
visited[r] = True
dfs(r, graph, visited, 2)

for i in range(1, len(result)):
    print(result[i])