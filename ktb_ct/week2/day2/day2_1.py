# 브루트포스
def backtrack(dwarfs, start, path, result, found_flag):
    if found_flag[0]: # 리스트를 사용한 상태 공유
        return
    if len(path) == 7:
        if sum(path) == 100:
            result.extend(sorted(path)) # 리스트에 여러 요소 한 번에 추가
            found_flag[0] = True
        return
    for i in range(start, len(dwarfs)):
        path.append(dwarfs[i])
        backtrack(dwarfs, i + 1, path, result, found_flag)
        path.pop()

def found_dwarfs(dwarfs):
    result = []

    found_flag = [False]
    backtrack(dwarfs, 0, [], result, found_flag)
    return result


# 입력
dwarfs = [int(input()) for _ in range(9)]

result = found_dwarfs(dwarfs)

for res in result:
    print(res)