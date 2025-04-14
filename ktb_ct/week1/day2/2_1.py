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
        if n & 1:
            positions.append(str(pos))
        n //= 2
        pos += 1
    
    print(" ".join(positions))
