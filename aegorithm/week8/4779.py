import sys

# dfs인 듯 파고 들어가니까, n은 0부터 12까지
# dfs에서는 문자열을 3개로 나누고, 가운데 요소는 공백 처리, 나머지에서는 또 문자열 3개로 반복
# 종료 조건은 문자열을 더 이상 나눌 수 없을 경우(depth가 0일 경우)
def dfs(array, depth):
    if depth == 0:
        return array
    
    length = len(array) // 3

    part1 = dfs(array[0:length], depth - 1)
    part2 = [" "] * length
    part3 = dfs(array[length*2:], depth - 1)

    return part1+part2+part3
    

# n 입력 시 3의 n승으로 치환 필요
# input = sys.stdin.readline 한 줄 입력 후 엔터 기다림
# sys.stdin: EOF까지 전부 한 번에 읽기 때문에 적합. 

try:
    for line in sys.stdin:
        n = int(line.strip())     # 공백 문자 제거
        array = ["-"] * (3 ** n)
        result = dfs(array, n)
        print("".join(result))
except:
    pass




