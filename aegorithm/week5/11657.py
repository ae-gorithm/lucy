# 일단 다익스트라이긴한데 시간이 0이면 순간 이동, 음수이면 타임머신?... 당황
# ㄴ 벨만-포드 알고리즘을 사용해야 함(시간이 음수이기 때문에 다익스트라를 이용할 수는 없음)
# o(n*m)
# 결과: 무한히 타임머신: -1 출력, 끝 / 그게 아니면 (가능: 순서대로 출력), (불가능: -1 출력)
import heapq # heappush(리스트, 넣을 항목), heappop()
import sys

def dijkstra(graph, start):
    INF = float('inf')
    distance = [INF] * (N+1)
    distance[start] = 0

    # N-1번 반복(모든 간선에 대해 거리 갱신 수행)
    for i in range(N - 1):
        for u in range(1, N+1):
            for v, w in graph[u]:
                if distance[u] != INF and distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
    
    # 음수 사이클 확인 (1번 더 돌려서 갱신되면 사이클 있음)
    for i in range(N - 1):
        for u in range(1, N+1):
            for v, w in graph[u]:
                if distance[u] != INF and distance[v] > distance[u] + w:
                    return -1, distance

    return 0, distance


# 입력
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())

    graph[A].append((B, C))

# 다익스트라로 도전
count, result = dijkstra(graph, 1)

# 출력
# 무한 타임 머신 여부 어떻게 찾지? count 개수가 N의 제곱보다 커지면 무한으로 간주하기
if count == -1:
    print(-1)
# 무한 타임 머신이 아니면
else:
    for i in range(2, len(result)):
        print(result[i] if result[i] != float('inf') else -1)