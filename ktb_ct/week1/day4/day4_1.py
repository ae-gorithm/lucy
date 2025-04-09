# 입력
count = 0
result = []
for _ in range(10):
    off, on = map(int, input().split())
    count -= off
    count += on
    result.append(count)

# 출력
print(max(result))
