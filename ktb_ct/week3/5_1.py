string = input()

# 1234
# 0 4
LENGTH = len(string)
left = 0
right = LENGTH - 1
mid = (left + right) // 2

FLAG = True
while(True):
    if left > mid:
        break
    if string[left] == string[right]:
        left += 1
        right -= 1
        continue
    else:
        FLAG = False
        break

print(1) if FLAG == True else print(0)