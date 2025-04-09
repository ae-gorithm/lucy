# dp 아닌 그리디... 1부터 시작, 합이 200인걸 출력만 하면됨 -> 시그마 합쓰기
def greedy(s):
    dp = [0]*(s+1)

    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    dp[5] = 1
    dp[6] = 3
    for i in range(s):
        dp[i] = max()
    
    return dp[s]


# 입력
s = int(input())
result = greedy(s)

# 출력
print(result)