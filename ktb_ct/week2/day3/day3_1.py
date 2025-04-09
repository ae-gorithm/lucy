#def gcd(a, b):
#    while(b > 0):
#        a, b = b, a% b
#    return a
import math

# 입력
a, b = map(int, input().split())

# 최대 공약수
result = math.gcd(a, b)
print(result)

# 최소 공배수
print(a * b // result) # 두수의 곱 // 최대 공약수, 혹은 lcm