import sys
input = sys.stdin.readline

# 유효 여부 검증
def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n

# 특정 학생에 대한 가중치를 각각 계산해야 하나?
# 그럼 학생 수만큼 서로 다른 보드를 만들고 계산해야 할 듯
# 특정 학생의 차례가 되면 지금까지의 보드를 바탕으로 가중치 보드를 제작하여 넣기
# 가중치 보드 제작 후 
# 1. 주변에 좋아하는 학생 수, 
# 2. 빈 칸 요소
# 3. 요소 sort 후 r이 가장 작은 거, c가 가장 작은 거 순으로 나열되므로 첫번째 자리를 리턴하여
# 최종 자리 컨펌
# 만족도는 인접한 칸에 앉은 좋아하는 학생 수

def batch(graph, student_num, board):
    tmp_board = [[0] * n for _ in range(n)] # 0-based
    blank_board = [[0] * n for _ in range(n)] # 0-based

    # 좋아하는 학생 수 기준 보드 업데이트 (1번)
    for node in graph[student_num]:
        for i in range(n):
            for j in range(n):
                if board[i][j] == node:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if is_valid(nx, ny, n):
                            tmp_board[nx][ny] += 1
    # 결과 확인(1번)
    result = []
    max_count = -1 # 0 안됨
    index_r = 0
    index_c = 0
    for i in range(n):
        for j in range(n):
            if tmp_board[i][j] > max_count and not board[i][j]:
                index_r = i
                index_c = j
                max_count = tmp_board[i][j]
                result = [(i, j)] # 비우고 자기 자신으로 업데이트
            elif tmp_board[i][j] == max_count:
                result.append((i, j))
    if len(result) == 1:
        board[index_r][index_c] = student_num
        # print(board)
        return board

    # 비어있는 칸 수 계산(2번)          
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if is_valid(nx, ny, n):
                    if board[nx][ny] == 0:
                        blank_board[i][j] += 1
    
    max_blank_count = -1 # 0 안됨
    result.sort() # 2, 3번 동시에 검사하기 위함
    for res in result:
        r, c = res
        if blank_board[r][c] > max_blank_count and not board[r][c]:
            index_r = r
            index_c = c
            max_blank_count = blank_board[r][c]
    
    board[index_r][index_c] = student_num
    # print(board)
    return board

# 만족도 구하기
def sum_preferrence(board, graph):
    sum = 0
    score = [0, 1, 10, 100, 1000]
    for i in range(n):
        for j in range(n):
            count = 0
            student = board[i][j]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if is_valid(nx, ny, n):
                    if board[nx][ny] in graph[student]:
                        count += 1
            
            # 갱신 로직 주의
            sum += score[count]
    return sum 

# 입력
# 첫번째꺼는 학생 번호, 나머지는 해당 학생이 좋아하는 학생 번호
n = int(input())

graph = [[] for _ in range((n*n+1))]
board = [[0] * n for _ in range(n)] # 전체 학생 위치 저장 보드

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n*n):
    array = list(map(int, input().split()))
    student_num = array[0]
    preferrences = array[1:]
    graph[student_num] = preferrences # 그대로 넣기

    # 자리 배치
    board = batch(graph, student_num, board)

# 학생 만족도 구하기(모든 자리 배치 끝난 후 가능)
result = sum_preferrence(board, graph)

print(result)

