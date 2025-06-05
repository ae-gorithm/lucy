import sys
# 백트래킹인데 path 2개

def back_track(sours, bitters, start, s_count, b_count):
    global min_count
    if start >= len(sours):
        return
        
    for i in range(start, len(sours)):
        s_count *= sours[i]
        b_count += bitters[i]
        
        current_count = abs(s_count - b_count) # math가 아니라 내장 함수 
        if current_count < min_count:
            min_count = current_count
        
        back_track(sours, bitters, i + 1, s_count, b_count) # i + 1

        b_count -= bitters[i]
        s_count /= sours[i]
    return min_count


# 어짜피 n은 10이긴 한데...
input = sys.stdin.readline

n = int(input())
sours, bitters = [], []
for _ in range(n):
    s, b = map(int, input().split())
    sours.append(s)
    bitters.append(b)

min_count = float('inf')
result = back_track(sours, bitters, 0, 1, 0)
print(int(result))