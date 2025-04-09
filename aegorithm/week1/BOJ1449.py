# 좌우 0.5 -> 적어도 하나의 구멍을 막는데 1 필요
# 그리디(테이프 길이 L)에 따라 달라짐
# 덮을 수 있는 최대 길이를 구하고, 카운트
def count_tape(n, l, array):
    count = 0
    
    i = 0
    while i < n:
        count += 1
        
        end = array[i] + l - 0.5

        while i < n and array[i] <= end:
            i += 1
    return count


# 입력
n, l = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = count_tape(n, l, array)

# 출력
print(result)