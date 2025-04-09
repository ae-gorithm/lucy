# 나무를 sort한 후 상위부터 내려오면서 채집
# 이진 탐색 사용

# 체크
def check(m, mid, trees):
    tree_count = 0
    for tree in trees:
        if tree > mid:
            tree_count += tree - mid
    
    if tree_count >= m:
        return tree_count
    else:
        return 0

# 이진 탐색
def binary_search(m, trees):
    left = 0
    right = max(trees)

    max_height = 0
    
    while left <= right: # 주의
        mid = (left + right) // 2
        if check(m, mid, trees):
            max_height = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_height

# 입력
n, m = map(int, input().split())
trees = list(map(int, input().split()))
result = binary_search(m, trees)

# 출력
print(result)