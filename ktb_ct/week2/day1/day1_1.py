# 피보나치 반복문으로 쌓아나가기
def fibo(n):
    array = [0]*(n+1)

    array[0] = 0
    
    if n > 0:  # 인덱스 에러 주의
        array[1] = 1
    for i in range(2, n+1):
        array[i] = array[i-2] + array[i-1]

    return array[n]

# 입력
n = int(input())
result = fibo(n)

print(result)