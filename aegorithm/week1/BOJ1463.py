# dp로 풀어볼까?
def dp(n):
    dp = [float('inf')]*(n+1) # 1-based
    dp[1] = 0

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        if(i % 2 == 0):
            dp[i] = min(dp[i], dp[i//2] + 1)
        if(i % 3 == 0):
            dp[i] = min(dp[i], dp[i//3] + 1)
    
    return dp[n]

# 입력
n = int(input())
result = dp(n)


# 출력
print(result)