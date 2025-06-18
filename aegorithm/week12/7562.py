import sys
from collections import deque

# 유효성 체크
def is_valid(x, y, l):
    return 0 <= x < l and 0 <= y < l

# 나이트 이동: 최단 경로 bfs
def move_knight(l, sx, sy, tx, ty, visited):
    visited[sx][sy] = True
    queue = deque([(sx, sy, 0)])

    while queue:
        cx, cy, count = queue.popleft()
        if cx == tx and cy == ty:
            return count
        for i in range(8):
            mx, my = moves[i]
            nx, ny = cx + mx, cy + my
            if is_valid(nx, ny, l) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count+1))

input = sys.stdin.readline

t = int(input())
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (2, 1), (2, 1), (1, 2)]
# 2 2 2 2 -1
# -1 -1 1 -1 2
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split()) # start
    tx, ty = map(int, input().split()) # target
    visited = [[False] * l for _ in range(l)]
    print(move_knight(l, sx, sy, tx, ty, visited))
  