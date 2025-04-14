"""
문제 상황: 괄호열을 읽고 계산하여 출력
한계 상황: 괄호와 값 분류 필요
        괄호: (), []
        괄호와 요소: (x): 2배, [x]:3배
        괄호가 잘 닫히면 더하기, 괄호 안에 추가 요소가 있으면 곱하기
예외 상황: 특정 리스트의 값이 여는 괄호 값이 1보다 작을 때 닫는 괄호가 들어오면 0 출력하고 종료
"""

# 입력
array = list(input())

stack = []
valid = True

for a in array:
    if a == '(' or a == '[':
        stack.append(a)
    
    else:
        if not stack:
            valid = False
            break
    
        if a == ')':
            temp = 0 # 이건 뭐임? 숫자잖아
            while stack and isinstance(stack[-1], int): # isinstance 왜 사용함, 뭘 확인하려는 거임
                temp += stack.pop() # 스택에 있는 건 문자인데 왜 숫자형에 더하지
            
            if not stack or stack[-1] != '(': # 이 논리가 이해 안감. stack의 마지막 요소가 (가 아닐 수도 있음?
                valid = False
                break
            stack.pop() # 이건 왜 또 pop해

            if temp == 0: # 왜 얘가 0일 때 2를 더함?
                stack.append(2)
            else:
                stack.append(2*temp)        
            
