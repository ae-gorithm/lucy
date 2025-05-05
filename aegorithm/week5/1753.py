# heapq 이용(최소힙), 방향 그래프
# 왜 다익스트라인가? => 최단 경로 탐색 알고리즘이기 때문
# 특정 하나의 정점에서 다른 모든 정점으로 가는 최단 경로 알려줌
# 출발 노드 설정 -> 출발 노드 기준 최소 비용 노드 -> 방문하지 않은 노드 최소 비용
#                                       -> 특정 노드로 가는 비용 고려 갱신
# 시간복잡도 o(log2 V)

import heapq
import sys

def dijikstra(graph, start):
    distance = [float('inf') for _ in range(V+1)]

    distance[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > distance[current_node]: # 더 짧은 경로가 있다면 무시
            continue

        for neighbor, weight in graph[current_node]:
            dist = current_dist + weight

            if distance[neighbor] > dist: # 오타 주의
                distance[neighbor] = dist
                heapq.heappush(queue,(dist, neighbor))


    return distance

# 입력
input = sys.stdin.readline
V, E = map(int, input().split()) # 대소문자 주의
K = int(input())

graph = [[] for _ in range(V+2)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

#print(graph)

result = dijikstra(graph, K)

for i in range(1, len(result)):
    print("INF") if result[i] == float('inf') else print(result[i])
