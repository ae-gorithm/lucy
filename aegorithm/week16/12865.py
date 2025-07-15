# 2차원 dp
# 최소 0, 최대 k만큼의 배낭
# w만큼 제외
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ws = [0]  # 1-based: 음수 인덱싱 방지1
vs = [0]
for _ in range(n):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):   # 물건
    for w in range(k+1):  # 용량
        if w < ws[i]:     # 음수 인덱싱 방지2
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-ws[i]] + vs[i]) 

print(dp[n][k])