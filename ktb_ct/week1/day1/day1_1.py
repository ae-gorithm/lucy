# for문을 통해 나누었을 때 0이 되는 것을 하나씩 count, k번째 수를 출력
# 약수
def find_k(n, k):
    count = 0
    for i in range(1, n+1): # 범위 주의
        if n % i == 0:
            count += 1
        if count == k:
            return i
    if count < k:
        return 0

# 입력
n, k = map(int, input().split())
result = find_k(n, k)

print(result)