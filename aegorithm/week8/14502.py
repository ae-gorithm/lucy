import copy
from collections import deque 
from itertools import combinations
# 모든 경우의 수를 탐색해봐야 함
# 문제 상황: 벽은 바이러스 근처가 아니어도 세워질 수 있음
#     월 마리아를 세운 뒤 한 번 더 검증해 봐야 함
# 순서: 벽 3개 세우기(이전과 겹치지 않게) -> 바이러스 퍼트리기 -> 안전 영역 구하기

# 안전 영역 구하기는 그냥 전체 영역에서 1인 것만 세면 됨(최대 n*m)
def count_safe_zone(after_run_virus):
    safe_count = 0
    for i in range(n):
        for j in range(m):
            if after_run_virus[i][j] == 0:
                safe_count += 1
    return safe_count

# 바이러스 퍼트리는 건 2를 기준으로 연구소 크기 내에서 벽을 만날 때까지 0인 것을 2로 바꿈(최대 n*m)
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m

def run_virus(tmp_region): # bfs(전파 깊이가 분명하게 queue 사용 필요)
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([])

    for x in range(n):
        for y in range(m):
            if tmp_region[x][y] == 2:
                queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if is_valid(nx, ny) and not visited[nx][ny] and tmp_region[nx][ny] == 0:
                tmp_region[nx][ny] = 2
                queue.append((nx, ny))
                visited[nx][ny] = True

    return tmp_region

def combinate(comb, blanks, start, depth, result):
    if depth == 3:
        result.append(comb[:])
        return 
    for i in range(start, len(blanks)):
        comb.append(blanks[i])
        combinate(comb, blanks, i+1, depth+1, result)
        comb.pop()

def hi_virus(region): 
    max_safe_area = -float('inf')
    blanks = [(i, j) for i in range(n) for j in range(m) if region[i][j] == 0]

    # 최대 시도 횟수는 어떻게 정하냐? safe_zone의 개수에서 3개를 구하는 만큼
    # 조합만큼만 반복하면 됨
    #for walls in combinations(blanks, 3): 이렇게 하면 편하긴 한데 직접 조합을 구현해보자
    wall_combination = []
    combinate([], blanks, 0, 0, wall_combination)

    for walls in wall_combination:
        tmp_region = copy.deepcopy(region)
        for x, y in walls:
            tmp_region[x][y] = 1
        infected = run_virus(tmp_region)
        safe = count_safe_zone(infected)

        max_safe_area = max(safe, max_safe_area)

    return max_safe_area


# 입력
n, m = map(int, input().split())
region = [list(map(int, input().split())) for _ in range(n)]

result = hi_virus(region)

# 출력
print(result)