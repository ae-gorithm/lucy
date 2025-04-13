# 백트래킹
# 만약 합이 K원이 되면 
# 그때의 개수와 현재의 개수 비교하여 최소 개수로 바꾸기
# 현재부터 마지막요소까지 path넣고 백트래킹 돌고 path뺌
def backtrack(coins, k, path, count, start, price_sum):
    
    if price_sum == k:
        count[0] = min(count[0], count(path))
    
    for i in range(start, len(coins)):
        path.append(coins[i])
        backtrack(coins, k, path, count, i + 1, price_sum + coins[i])
        path.pop()

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = [float('inf')]
backtrack(coins, k, [], count, 0, 0)

if count[0] > float('inf'):
    print(count[0])
else:
    print(-1)

# 이거 dp로 푸는 게 좋음