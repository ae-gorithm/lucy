import sys

def partial_sum(x):
    n = len(x)
    
    # 누적합
    prefix = [0] * (n+1)
    prefix[0] = 0
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + x[i-1]
    
    max_sum = -float('inf')
    for start in range(n+1):
        for end in range(start+1, n+1):
            max_sum = max(max_sum, prefix[end] - prefix[start])        
    return max_sum

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    print(partial_sum(x))