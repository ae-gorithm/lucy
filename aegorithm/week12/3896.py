import sys
import math
input = sys.stdin.readline

MAX = 1299710
is_prime = [True] * (MAX) # 0, 1은 소수 아님, 이후는 기본 소수로 가정
is_prime[0] = False
is_prime[1] = False

# 우선은 [[0] for i in range(1299710)] 해두고, 소수라면 그 [현재 소수 - 그 전 소수]만큼 기록
# 소수를 판별하는 방법은 그 수를 for문을 통해 하나씩 나누면서 한번이라도 나눠지는게 있으면 소수
# 그 수의 제곱근에 해당하는 값까지만 나눠지게 하기 => 시간 초과

# 에라토스테네스의 체 적용하기 => 자세히 설명
for i in range(2, int(MAX ** 0.5)+1): # sqrt 사용안하고 바로 ** 0.5 가능
    if is_prime[i]: # i가 소수이면
        for j in range(i*i, MAX, i): # i의 배수들은 무조건 소수가 아님
            is_prime[j] = False 

t = int(input())
for _ in range(t):
    k = int(input())
    
    if is_prime[k]:
        print(0)
        continue

    left = k
    while not is_prime[left]:
        left -= 1
    
    right = k
    while not is_prime[right]:
        right += 1

    print(right - left)

