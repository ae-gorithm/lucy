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


## 유니온 파인드로 해보기(묶여있는 노드들) - 최소 신장 트리의 전신 => 무조건 좋지는 않음
# 장점: depth를 자동으로 1로 만들어줌. 빠르게 찾을 수 있음
# 단점: array로 나타내라 했을 때는 사용할 수 없을지도

# 그렇다. 근데 경로 찾는 알고리즘은 따로 있음


### bfs: 루트에서 멀리 있을 것 같을 때 사용, 그러나 힙 메모리 많이 씀. 이때 dp나 프루닝