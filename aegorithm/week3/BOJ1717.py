"""
문제 상황: 1. 입력 0 -> 합집합 연산
         2. 입력 1 -> 두 원소가 같은 집합에 포함되었는지 확인하는 연산
한계 상황: 초기에는 n개의 다른 집합이 있으나 이를 점차 합쳐나가야 함 -> 어느 집합으로 합칠 건지?
         queue에 넣어야 하나?
         단순히 queue만 돌면 시간초과 o(n*m)
         logn 연산 필요... 유니온 파운드 => 트리 구조
         make-set(x): x를 유일한 원소로 하는 새로운 집합을 만듬
         union(x, y): 두 집합을 합침
         find(x): x가 속한 집합의 대표값 반환
예외 상황: a와 b가 같은 경우에는 바로 " YES " 출력
"""
import sys
input = sys.stdin.readline

def find(x):
    if array[x] != x:
        array[x] = find(array[x])
    return array[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        array[y_root] = x_root
    return

n, m = map(int, input().split())

array = [i for i in range(n+1)] # 초기화 잘하기
for _ in range(m):
    number, a, b = map(int, input().split())

    if number == 0:
        union(a, b)
    elif number == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")