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


# 백트래킹에서 가장 중요한 것은 어떤 조건에서 재귀를 빠져나올 것인가임

### 백트래킹으로 하면은 2의 20승
### 부분수열의 합2: 투 포인터
#### 두 부분으로 나눠서 각각 정렬 후 왼쪽은 최소 포인터, 오른쪽은 최대 포인터
### 0보다 크면 큰 쪽을 줄임, 0보다 작으면 작은 쪽을 올림
#### 정답이면 동수만큼을 while문으로 찾아서 l(왼쪽동수)*n(오른쪽동수)만큼 더해줌