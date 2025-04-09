from collections import deque
# 우선순위큐

# 입력
t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    importances = list(map(int, input().split()))

    queue = deque()
    for i in range(len(importances)):
        queue.append((i, importances[i]))
    
    count = 0
    while queue: 
        current = queue.popleft()

        if any(current[1] < other[1] for other in queue): # any 문법 기억하기
            queue.append(current) # 위치 이동 반영(단순 정렬로는 안됨)
        else:
            count += 1
            if current[0] == m:
                print(count)
                break