# 백트래킹 적용 
# 크기가 양수인 부분수열 -> 공집합 제외

# 우선은 path의 합이 s와 같은지 확인하고 같으면 리턴
# for문을 돌면서 start부터 n+1 범위 내에 있는 요소를 backtrack
#     다 돌면 나와서 path에서 가장 최근 걸 뺌
def backtrack(numbers, s, start, path, count, path_sum):

    if path_sum == s and len(path) != 0: # 공집합 없애기
        count[0] += 1
    
    for i in range(start, len(numbers)):
        path.append(numbers[i])
        backtrack(numbers, s, i+1, path, count, path_sum + numbers[i]) # 그 다음 인덱스부터 탐색
        path.pop()


# 입력
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

count = [0] # 참조값으로 넘기기
backtrack(numbers, s, 0, [], count, 0) # 굳이 리턴값 없어도 됨

print(count[0])