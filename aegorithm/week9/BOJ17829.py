import sys
import math
# 영역 분기는 2*2 크기의 정사각형으로
# 8*8의 행렬이 주어진다고 했을 때 1회(정사각형 16개) -> 2회(정사각형 4개) -> 3회(정사각형 1개)
# start(n, m)을 기준으로 [0, 1], [1, 0], [1, 1] 요소 검사하면 됨 
# -> 영역 내 두번째로 큰 숫자를 현재 영역의 대표로 저장
def pooling(cnn, x, y):
    orders = []

    neighbors = [[0, 0], [0, 1], [1, 0], [1, 1]]
    for i in range(4):
        nx = x + neighbors[i][0]
        ny = y + neighbors[i][1]
        orders.append(cnn[nx][ny])
    orders.sort() # 오름차순
    return orders[2]

#n은 2의 n승으로... pow 였나?
input = sys.stdin.readline
n = int(input())
cnn = [list(map(int, input().split())) for _ in range(n)]

# 영역 분기
# count = 1, 매 라운드가 지날 때마다 +1하면 공간 복잡도 활용 가능할 것 같음
# for i in range(0, n, 2*count) 이렇게 하면 괜춘할 듯? 이중 for문 사용
# 근데 이러면 기존 값들이 업데이트되지 않을 수도 있다는 단점이 있음
# 새로운 배열을 만들어 저장할 것
k = int(math.log2(n))
size = n

for _ in range(k):
    new_size = size // 2
    new_mat = [[0]*new_size for _ in range(new_size)]

    for i in range(0, size, 2):
        for j in range(0, size, 2):
            ni = i // 2 # 축소 영역으로 사상시키기
            nj = j // 2 # 마찬가지
            new_mat[ni][nj] = pooling(cnn, i, j)
    
    cnn = new_mat
    size = new_size

print(cnn[0][0])
