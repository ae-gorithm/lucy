# 이진수 변환 for i in range if n // pow(2, i) > 0: n %= pow(2, i) list.append(n // pow(2, i))
#  대략 i = 23부터 시작하면 됨 여분으로 25부터 시작하기
def binary(n):
    positions = []
    i = 0
    while n:
        if n % 2 == 1:
            positions.append(i)
        n //= 2
        i += 1
    return positions


# 입력
t = int(input())

result = []
for _ in range(t):
    n = int(input())
    list = binary(n)
    list.sort()
    result.append(list)

for res in result:
    print(" ".join(map(str, res)))