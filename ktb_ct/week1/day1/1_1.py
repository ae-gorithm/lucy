""" 약수 세기 
바텀업을 통해 나눴을 때 나머지가 0이 되면 count += 1
count가 k와 같으면 바로 출력
"""
def find_k(n, k):
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            if count == k:
                print(i)
                return
    print(0)

# 입력
n, k = map(int, input().split())
find_k(n, k)