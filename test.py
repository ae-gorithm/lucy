import copy
# 최대 개수 구하기 -> brute_force 가로: for(세로 for(가로)), 세로: for(가로 for(세로))
def count_candy(array, n):
    max_count = 0
    # 가로
    for j in range(n):
        current_count = 1 # 한 개의 사탕 자체도 하나의 연속된 부분...
        for i in range(1, n):
            if(array[i][j] == array[i-1][j]):
                current_count += 1
                if(current_count > max_count):
                    max_count = current_count
            else:
                current_count = 1
    
    # 세로
    for i in range(n):
        current_count = 1
        for j in range(1, n):
            if(array[i][j] == array[i][j-1]):
                current_count += 1
                if(current_count > max_count):
                    max_count = current_count
            else:
                current_count = 1
    return max_count

# 사탕 switch
def switch_candy(array, x, y, nx, ny):
    array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
    return array

# 유효성 검사
def is_valid(n, x, y):
    return 0 <= x < n and 0 <= y < n

# 보드에서 n^2 -> switch 로직 -> 최대 개수 구함 -> return
def bomboni(array, n):
    max_candy = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if(is_valid(n, nx, ny)):
                    tmp_array = copy.deepcopy(array) # 이거 위치 유의
                    new_array = switch_candy(tmp_array, x, y, nx, ny)
                    current_max_candy = count_candy(new_array, n)
                    
                    if(current_max_candy > max_candy):
                        max_candy = current_max_candy
    return max_candy

# 입력
n = int(input())
array = [list(input()) for _ in range(n)]

max_candy = bomboni(array, n)

# 출력
print(max_candy)