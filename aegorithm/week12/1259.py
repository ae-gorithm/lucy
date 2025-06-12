# 20000 => nlogn, n
# 투 포인터를 사용해도 될 것 같고
# 두 개를 하나로 합쳐서 set을 붙였을 때 떨어지는 것만큼 전체 합에서 빼도 좋을 것 같음

A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_count = len(a) + len(b)  # 8
common_count = len(set(a + b)) # 6
print(common_count*2-total_count)