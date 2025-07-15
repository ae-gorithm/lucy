# 조합이니까 백트래킹 최대 20이니까 가능함
# 1, 3, 6 => (1, 1), (2, 3), (5, 5) => 8, 9 => 17
# 2, 4, 5 => (2, 2), (3, 4), (4, 4) => 9, 10 => 19  :19 - 17 = 2
import sys
input = sys.stdin.readline

# 조합을 해두고
def backtrack(s, path, start, visited):
    global min_diff
    if len(path) == n // 2:
        result = count_capacity(path)
        min_diff = min(result, min_diff)
        return
        
    for i in range(start+1, n):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack(s, path, i, visited) # start가 아니라 i임
            path.pop()
            visited[i] = False

# 팀 점수
def team_count(team):
    team_sum = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a, b = team[i], team[j]
            team_sum += (s[a][b] + s[b][a])
    return team_sum

# 조합 계산
def count_capacity(path):
    a_count = team_count(path)
    left = list(set([i for i in range(n)]) - set(path))
    b_count = team_count(left)
    
    return abs(a_count - b_count)

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_diff = float('inf')
backtrack(s, [], 0, visited)
print(min_diff)