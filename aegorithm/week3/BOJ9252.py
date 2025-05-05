"""
문제 상황: 최장 공통 부분 수열 -> 두 수열이 주어졌을 때 모두의 부분 수열이 되는 것 중 가장 긴 것을 출력
한계 상황: 최대 1000글자 o(n^2)여도 시간 초과 안남
        투포인터해야 할듯. 하나씩 번갈아가며 증가시키기
예외 상황: lcs 여러 개면 아무거나 출력(아마 일치하는게 하나인 경우를 이야기하는 듯하다), lcs 길이가 0이면 문자열은 출력하지 않음
"""
"""
def lcs(string1, string2):
    sequence = []

    left, right = 0, 0

    while(left != (len(string1) + 1), right != (len(string2) + 1)):
        left += 1 # 
        

string1 = list(input())
string2 = list(input())

lcs(string1, string2)
print(len(result))
if(len(result) != 0):
    print("".join(result))
"""