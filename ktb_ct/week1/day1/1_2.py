"""
도전 상황: n개의 수 n-1개의 연산자, 결과가 최대인 것과 최소인 것 구함
한계 상황: 식의 계산은 연산자 우선 순위 무시하고 앞에서부터 진행 
         나눗셈은 정수 나눗셈으로 몫만 취함
         음수로 나누는 경우도 있음: 양수로 바꾼 뒤 몫을 취하고 몫을 음수로 바꿈

         n은 최대 11이므로 dfs 가능? 2의 11승?
예외 상황: 
"""
# dfs
def dfs(numbers, count, add, sub, mul, div, depth, max_depth):
    if depth == max_depth + 1:
        result.append(count)
        return # return은 재귀 함수의 조기 종료를 위해서만 사용하기
    
    if add:
        # return을 하면 안됨. 첫번째 재귀 호출 후 즉시 종료됨(단 하나의 경로만 따라가게 됨)
        # 모든 경로의 결과를 누적해야 하는 경우에는 각 분기마다 바로 return을 사용하지 않아야 올바른 탐색이 이루어짐
        dfs(numbers, count + numbers[depth], add - 1, sub, mul, div, depth + 1, max_depth)
    if sub:
        dfs(numbers, count - numbers[depth], add, sub - 1, mul, div, depth + 1, max_depth)
    if mul:
        dfs(numbers, count * numbers[depth], add, sub, mul - 1, div, depth + 1, max_depth)
    if div:
        if count < 0:
            dfs(numbers, -(-count // numbers[depth]), add, sub, mul, div - 1, depth + 1, max_depth)
        else:
            dfs(numbers, count // numbers[depth], add, sub, mul, div - 1, depth + 1, max_depth)

# 입력
n = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

max_depth = sum(opers)
result = []
dfs(numbers, numbers[0], opers[0], opers[1], opers[2], opers[3], 1, max_depth)

# 출력
# n이 작다면 결과 수가 많지 않기 때문에 min, max를 사용하는게 효과적이고 이해하기 편함
# 대신 dfs 경우의 수가 크다면 직접 비교 권장
print(max(result))
print(min(result))