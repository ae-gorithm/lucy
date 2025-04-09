# 그냥 [시작범위:끝범위+1]로 바로 출력하면 될 듯 -> 오노... 시간초과
# 누적합 사용시 시간복잡도 O(1)... 바로 고

# 입력
n, m = map(int, input().split())
numbers = list(map(int, input().split()))


prefix = [0] * (n+1) # 누적합
for i in range(n):
    prefix[i+1] = prefix[i] + numbers[i]

for _ in range(m):
    i, j = map(int, input().split())

    result = prefix[j] - prefix[i-1] # ㅇㅇ
    print(result)