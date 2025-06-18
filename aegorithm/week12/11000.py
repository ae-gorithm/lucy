# 결국 완전 탐색일 것 같음
# 유효하면 해당 배열에 추가, 아니면 새로 추가

n = int(input())
catalog = [False]*(10**9)
print(catalog)
for _ in range(n):
    s, t = map(int, input().split())
    is_available = True
    for i in range(len(catalog)):
        for j in range(s, t+1):
            if catalog[i][j]:
                is_available = False
        if is_available:
            for j in range(s, t+1):
                catalog[i][j] = True
            break
    if not is_available:
        new_list = [False]*(10**9)
        for i in range(s, t+1):
            new_list[i] = True
        catalog.append(new_list)
            