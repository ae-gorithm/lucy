from collections import deque

# 코너 케이스—단지에 집이 단 하나인 경우 주의

# valid 영역 내
def is_valid(n, x, y):
    return 0 <= x < n and 0 <= y < n

# queue에 연결된 집 개수 기록(1단지씩)
# dfs
def dfs(n, board, visited, x, y, count):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_valid(n, nx, ny):
            if board[nx][ny] == 1 and not visited[nx][ny]:
                count[0] += 1
                dfs(n, board, visited, nx, ny, count)


n = int(input())
board = [list(map(int, input())) for _ in range(n)]

result = []
visited = [[False]*(n) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = [0]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            dfs(n, board, visited, i, j, count)
            result.append(count[0]+1) # 무조건 결과에 추가(한 단지에 집이 하나만 있는 경우도 포함)
            count[0] = 0

result.sort() # 오름차순 정렬... 문제 잘 읽기
print(len(result))
for res in result:
    print(res)