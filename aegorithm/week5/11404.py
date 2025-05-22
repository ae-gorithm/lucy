# 모든 도시의 쌍에 대해서 도시 A에서 도시 B로 가는데 필요한 비용의 최솟값
# 다익스트라이긴 한데 n*n의 리스트 가짐. 조금 복잡해짐. 
# 간선 가중치가 모두 양수이므로 다익스트라 사용 가능하나 플로이드-워셜이 더 간단하고 안정적이기 때문에 권장됨
# ㄴ 플로이드-워셜의 대표 문제 o(n^3)
import heapq
import sys

def dijkstra(start, graph):
    distance = [INF] * (n+1)
    
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if curr_dist > distance[curr_node]:
            continue

        for node, weight in graph[curr_node]:
            if distance[node] > curr_dist + weight:
                distance[node] = curr_dist + weight

    return distance 

def tmp(graph):
    distance = [[] for _ in range(n+1)]
    
    for i in range(1, n+1):
        distance[i].append(dijkstra(i, graph))

    return distance

# 입력
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float('inf')
result = tmp(graph) # 왜 값이 약간 안 맞지?

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print(result[i][0][j] if result[i][0][j] != INF else 0, end=" ")
    print()