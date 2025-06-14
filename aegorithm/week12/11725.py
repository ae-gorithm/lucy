# 최적화: queue 사용, visited를 별도로 두지 않고 parents에 0을 기본값으로 두고 사용하기
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
parents[1] = 1

while queue:
    parent = queue.popleft()
    for node in graph[parent]:
        if parents[node] == 0:
            parents[node] = parent
            queue.append(node)

for i in range(2, len(parents)):
    print(parents[i])
