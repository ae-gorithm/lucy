# 나머지 구함
def multiple(a, b, c):
    return pow(a, b, c)

# 입력
a, b, c = map(int, input().split())
result = multiple(a, b, c)

# 출력
print(result)