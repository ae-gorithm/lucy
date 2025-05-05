# dx = [1, 0], dy = [0, 1]만 존재하는 dp
# 각 dp가 [n, n]에 도착할 때마다 count += 1
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

def jump(x, y):
    global count
    if x == n-1 and y == n-1:
        count += 1
        return
    for i in range(2):
        nx = x + dx[i] * board[x][y]
        ny = y + dy[i] * board[x][y]
        
        if is_valid(nx, ny):
            jump(nx, ny)
    return


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

count = 0
dx = [1, 0]
dy = [0, 1]
jump(0, 0)
print(count)