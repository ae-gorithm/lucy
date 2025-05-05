"""
문제 상황: 주어진 정점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램 작성 dp min(직접 경로, 간접 경로)
        최소 힙 log n heapq 사용해서 힙 연산 처리 
        heappush(heap, item) / heappop(heap) -> heap은 일반 리스트
한계 상황: 방향 그래프임
예외 상황: 시작점 자신은 0으로 출력, 경로가 존재하지 않는 경우 
"""
import sys
import heapq

# V*V INF로 모두 초기화
def dijkstra(start, graph, dist):
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq) # 우선순위큐(현재까지의 거리)
        if d > dist[u]:
            continue
        for v, w in graph[u]: # 그래프상 거리
            if d + w < dist[v]: 
                dist[v] = d + w
                heapq.heappush(pq, (d + w, v))
    return dist


# 입력
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())

INF = 10 ** 18 ## 무한대
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [INF] * (V+1)
dist[K] = 0
dijkstra(K, graph, dist)

# 출력
for i in range(1, len(dist)):
    print('INF') if dist[i] == INF else print(dist[i])