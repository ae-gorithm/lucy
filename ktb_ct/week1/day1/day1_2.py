import sys
input = sys.stdin.readline


# 백트래킹 함수 정의
def dfs(index, current_result, add, sub, mul, div):
    global max_result, min_result

    # 모든 숫자를 다 사용했다면 결과 업데이트
    if index == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    next_num = numbers[index]

    # 각 연산자가 남아있는 경우 백트래킹
    if add:
        dfs(index + 1, current_result + next_num, add - 1, sub, mul, div)
    if sub:
        dfs(index + 1, current_result - next_num, add, sub - 1, mul, div)
    if mul:
        dfs(index + 1, current_result * next_num, add, sub, mul - 1, div)
    if div:
        # 나눗셈: 음수일 때 처리 주의
        if current_result < 0:
            dfs(index + 1, -(-current_result // next_num), add, sub, mul, div - 1)
        else:
            dfs(index + 1, current_result // next_num, add, sub, mul, div - 1)
            
# 입력
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최댓값, 최솟값 초기화
max_result = -int(1e9)
min_result = int(1e9)

# DFS 시작 (0번째 숫자에서 시작)
dfs(1, numbers[0], add, sub, mul, div)

# 결과 출력
print(max_result)
print(min_result)
