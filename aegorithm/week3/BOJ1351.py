"""
문제 상황:
한계 상황: 단순히 쌓아올라가기만 하면 되나? 무조건 시간 초과
        n에 p가 몇 번 들어가는지, q가 몇 번 들어가는지 세고 모두 더하면 되지 않을까?
예외 상황: n이 0인 경우
"""
n, p, q = map(int, input().split())

result = 0
if (n > 0):
    if p > 0:
        result += 1
    if q > 0:
        result += 1
    result += n // p + n // q
    
if result == 0:
    result += 1

print(result)

