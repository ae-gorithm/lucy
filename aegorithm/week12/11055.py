# 백트래킹: 2^n, 2^1000 > 100,000,0000
# dp:
# 이전 요소보다 큰지 검사
def dynamic_programming(dp, n, a):
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j]+a[i])

n = int(input())
a = list(map(int, input().split()))
dp = a[:]
dynamic_programming(dp, n, a)
print(max(dp))