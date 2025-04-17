"""
문제 상황:
한계 상황: 단순히 쌓아올라가기만 하면 되나? 무조건 시간 초과
         재귀적 정의를 그대로 사용하되 메모이제이션 적용
         배열 대신 딕셔너리를 적용할 것(키가 연속적이지 않은 경우 딕셔너리가 적합)
"""
def A(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = A(n//p) + A(n//q)
    return memo[n]

n, p, q = map(int, input().split())

memo = {}

print(A(n))

