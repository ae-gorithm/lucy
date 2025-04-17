"""
문제 상황: n보다 크고 2n보다 작거나 같은 소수 찾기
         입력이 많으니 sys.stdin.readline 활용하고 0이 들어올 경우 소수 찾기 작업 종료
한계 상황: 소수 찾기 시 약수의 중간값까지만 찾기 -> o(루트n) -> 전체 탐색해도 o(n)에 불과함
         에라토스테네스의 체 -> o(n log log n) + 슬라이스 합
         소수라고 생각되는 수를 기준으로 그 수의 배수를 모두 지우고 지워지지 않은 것들을 계속 소수라고 생각하면서 그 수의 배수를 지우는 방식
예외 상황: 
"""

import sys
input = sys.stdin.readline

MAX = 123456 * 2
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i): 
            is_prime[j] = False # i가 소수라면 i의 배수들은 모두 소수가 아니기 때문

while(True):
    n = int(input()) # 위치 주의
    if n == 0:
        break
    count = sum(is_prime[n+1: 2*n+1]) # n+1 ~ 2n
    print(count)