# 부분합 이용
# (왼쪽 높이 기억, 그 높이보다 같을 때까지 +1하며 
# 해당 영역 내에 있는 높이 차 하나씩 카운트)
def partial_sum(w, blocks):
    water = 0
    partial_water = 0
    i = 0

    left_height = 0
    while i < w:
        if left_height!=0 and left_height > blocks[i]:
            partial_water += (left_height - blocks[i])
            i += 1
        elif left_height == blocks[i]:
            water += (left_height - blocks[i])
            i += 1
        elif left_height < blocks[i]:
            left_height = blocks[i]
            i += 1

    return water

# 입력
h, w = map(int, input().split())
blocks = list(map(int, input().split()))

result = partial_sum(w, blocks)

# 출력
print(result)