import sys
# 연속된 수열이므로 백트래킹이 아니라 dfs 사용? => recursive 
# 배열 원소가 모두 양수 => 투 포인터 사용: 오른쪽 포인터가 늘어나면 값이 무조건 증가한다는 특성을 기대하는 경우.
# 만약 배열 원소가 모두 양수가 아니라면? 누적합 사용
def two_pointer(n, m, a):
    
    start = 0
    current_sum = 0
    count = 0

    for end in range(n):
        current_sum += a[end]

        while start <= end and current_sum > m:
            current_sum -= a[start]
            start += 1

        if current_sum == m:
            count += 1
    return count

# 입력(빠른 입력 사용)
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 호출
result = two_pointer(n, m, a)

# 출력
print(result)