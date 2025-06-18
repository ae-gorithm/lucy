import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# union find + 젤 적은 값을 가진 부모 밑으로 들어감
def find(n):
    while(parent[n] != n): 
        parent[n] = parent[parent[n]]
        n = parent[n]
    return n

def union(x, y, parent):
    if find(x) != find(y): # 달라야 함
        if a[x] == a[y]: # 흠 만약 같다면?
            return
        elif a[x] < a[y]:
            parent[y] = x
        else:
            parent[x] = y
    return parent


# 친구비 계산: 부모들을 모두 더했을 때 k 이하면 최소 비용 출력
# 이상이면 "Oh no" 출력
def count_friends_fee(parent):
    fee = 0
    for i in range(len(parent)-1):
        if i == parent[i]:
            fee += a[i]
    if fee > k:
        print("Oh no")
    else:
        print(fee)

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

parent = [i for i in range(n+1)]
for _ in range(m):
    v, w = map(int, input().split())
    union(v-1, w-1, parent)
count_friends_fee(parent)