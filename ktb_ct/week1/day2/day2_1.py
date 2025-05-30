"""
문제 상황: n을 이진수로 나타냈을 때의 1의 위치 모두 출력(최하위 비트부터)
한계 상황: n은 1부터 10의 6승.
         바텀업으로 올라가면서 2의 n승짜리로 나눴을 때의 몫을 취하고 1이면 result에 넣기
예외 상황:
"""

t = int(input())
for _ in range(t):
    n = int(input())
    pos = 0
    positions = []
    
    while n:
        if n & 1: # 비트 연산자 사용: 최하위 비트가 1인지 확인
            positions.append(str(pos))
        n //= 2 # 바텀업 방식이 맞음. 최하위 비트부터 시작해서 순차적으로 위쪽으로 이동하는 구조
        # 2의 0, 1, 2라고 생각하면 됨
        pos += 1
    
    print(" ".join(positions))
